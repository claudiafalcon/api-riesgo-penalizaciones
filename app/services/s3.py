
import boto3
import re
from collections import defaultdict
import os

s3 = boto3.client("s3")
bucket = "etl-riesgo-penalizaciones-data"
pattern = re.compile(r"([^/]+)/day=(\d{2}-\d{2}-\d{4})/data(_part\d+)?\.(json|parquet)$")

def list_files_by_day(file_type="json"):
    paginator = s3.get_paginator("list_objects_v2")
    response_iterator = paginator.paginate(Bucket=bucket)

    result = defaultdict(lambda: defaultdict(lambda: {"json": 0, "parquet": 0}))

    for page in response_iterator:
        for obj in page.get("Contents", []):
            key = obj["Key"]
            match = pattern.match(key)
            if match:
                collection, date, _, ext = match.groups()
                if ext == file_type:
                    result[collection][date][ext] += 1

    # Ordenar por fecha
    sorted_result = {
        col: dict(sorted(days.items(), key=lambda d: tuple(map(int, reversed(d[0].split("-")))))
        ) for col, days in result.items()
    }
    return sorted_result


def generate_presigned_url(key: str, expiration: int = 3600) -> str | None:
    try:
        response = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket, "Key": key},
            ExpiresIn=expiration
        )
        return response
    except Exception as e:
        print(f"❌ Error generando URL firmada: {e}")
        return None

import boto3
from datetime import datetime, timedelta

s3 = boto3.client("s3")
BUCKET_NAME = "etl-riesgo-penalizaciones-data"

def generate_presigned_urls_by_range(coleccion, tipo, inicio, fin):
    urls = []
    start = datetime.strptime(inicio, "%Y-%m-%d")
    end = datetime.strptime(fin, "%Y-%m-%d")

    current = start
    while current <= end:
        date_str = current.strftime("day=%d-%m-%Y")
        prefix = f"{coleccion}/{date_str}/"
        filename = f"{prefix}data.{tipo}"

        try:
            url = s3.generate_presigned_url(
                "get_object",
                Params={"Bucket": BUCKET_NAME, "Key": filename},
                ExpiresIn=3600
            )
            urls.append({"fecha": date_str, "url": url})
        except Exception as e:
            print(f"❌ Error con {filename}: {e}")

        current += timedelta(days=1)

    return urls

def list_presigned_urls_for_day(folder: str, tipo: str = "parquet", expiration: int = 3600) -> list:
    prefix = f"{folder}/data"
    pattern = re.compile(rf"{re.escape(folder)}/data(_part\d+)?\.{tipo}$")

    paginator = s3.get_paginator("list_objects_v2")
    page_iterator = paginator.paginate(Bucket=bucket, Prefix=prefix)

    urls = []
    for page in page_iterator:
        for obj in page.get("Contents", []):
            key = obj["Key"]
            if pattern.match(key):
                url = generate_presigned_url(key, expiration)
                if url:
                    urls.append(url)
    return urls