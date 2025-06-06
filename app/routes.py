from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return jsonify({"message": "API Penalizaciones Activa Prueba Yaa"}), 200

@main.route("/transacciones")
def transacciones_dummy():
    return jsonify({"data": "Aquí irán los datos de transacciones"}), 200
