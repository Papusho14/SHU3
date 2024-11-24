from flask import Flask, jsonify, request
from conn import conectar_bd
from datetime import datetime
import mysql.connector

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    if not data:
        return jsonify({"Error": "No se enviaron datos en la solicitud."}), 400
    try:
        worker_id = int(data.get('worker_id'))
        specially = data.get('specially')
        worker_name = data.get('worker_name')
        register_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        update_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    except (ValueError, TypeError):
        return jsonify({"Error": "El numero de empleado debe ser un número y los demás campos deben ser válidos."}), 400   

    if not all([id, worker_id, specially, worker_name]):
        return jsonify({"Error": "Todos los campos son obligatorios."}), 400

    try:
        # Conectar a la base de datos
        conn = conectar_bd()
        cursor = conn.cursor()

        # Insertar datos en la tabla
        query = "INSERT INTO teachers (worker_id, specially, worker_name, register_date, update_date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (worker_id, specially, worker_name, register_date, update_date))
        conn.commit()

        return jsonify({"Mensaje": "Los datos se agregaros satisfactoriamente!"}), 201
    except mysql.connector.Error as err:
       return jsonify({"Error": f"Error al insertar los datos: {str(err)}"}), 500
    finally:
        cursor.close()
        conn.close()

