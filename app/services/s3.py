
import boto3
import re
from collections import defaultdict

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

