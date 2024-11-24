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

#########################################################################################################################################
#Aqui diego tiene que subir su parte

from flask import Flask, jsonify, request
from conn import conectar_bd
from datetime import datetime
import mysql.connector

app = Flask(__name__)


@app.route('/view', methods=['GET'])
def get_all_data():
    try:
        # Conectar a la base de datos
        conn = conectar_bd()
        cursor = conn.cursor()

        # Consultar todos los datos de la tabla
        query = "SELECT * FROM teachers"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Convertir los resultados a un formato adecuado para JSON
        teachers = []
        for row in rows:
            teachers.append({
                "id": row[0],
                "worker_id": row[1],
                "specially": row[2],
                "worker_name": row[3],
                "register_date": row[4],
                "update_name": row[5]
            })

        return jsonify(teachers), 200

    except mysql.connector.Error as err:
        return jsonify({"Error": f"Error al recuperar los datos: {str(err)}"}), 500

    finally:
        cursor.close()
        conn.close()



#########################################################################################################################################

@app.route('/delete', methods=['DELETE'])
def delete_data():
    # Leer el worker_id desde el cuerpo de la solicitud
    data = request.get_json()
    
    # Verificar si el worker_id fue proporcionado
    worker_id = int(data.get('worker_id'))
    
    if not worker_id:
        return jsonify({"Error": "El numero de empleado es requerido."}), 400

    try:
        # Conectar a la base de datos
        conn = conectar_bd()
        cursor = conn.cursor()

        # Verificar si el registro existe con el worker_id
        query_check = "SELECT * FROM teachers WHERE worker_id = %s"
        cursor.execute(query_check, (worker_id,))
        row = cursor.fetchone()
        
        if not row:
            return jsonify({"Error": f"Registro con numero de empleado {worker_id} no encontrado."}), 404

        # Eliminar el registro
        query_delete = "DELETE FROM teachers WHERE worker_id = %s"
        cursor.execute(query_delete, (worker_id,))
        conn.commit()

        return jsonify({"Mensaje": f"Registro con numero de empleado {worker_id} eliminado exitosamente."}), 200

    except mysql.connector.Error as err:
        return jsonify({"Error": f"Error al eliminar el dato: {str(err)}"}), 500

    finally:
            cursor.close()
            conn.close()

@app.route('/update', methods=['PUT'])
def update_data():
    # Leer el worker_id y los nuevos datos desde el cuerpo de la solicitud
    data = request.get_json()

    worker_id = int(data.get('worker_id'))
    worker_name = data.get('worker_name')
    specially = data.get('specially')
    update_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    # Verificar que todos los campos necesarios están presentes
    if not worker_id:
        return jsonify({"Error": "El numero de empleado es requerido."}), 400
    if not worker_name or not specially or not specially or not update_date:
        return jsonify({"Error": "Todos los campos son requeridos para la actualización."}), 400

    try:
        # Conectar a la base de datos
        conn = conectar_bd()
        cursor = conn.cursor()

        # Verificar si el registro existe con el worker_id
        query_check = "SELECT * FROM teachers WHERE worker_id = %s"
        cursor.execute(query_check, (worker_id,))
        row = cursor.fetchone()
        
        if not row:
            return jsonify({"Error": f"Registro con numero de empledo {worker_id} no encontrado."}), 404

        # Actualizar el registro con los nuevos datos
        query_update = """
            UPDATE teachers
            SET worker_name = %s, specially = %s, update_date = %s
            WHERE worker_id = %s
        """
        cursor.execute(query_update, (worker_name, specially, update_date, worker_id))
        conn.commit()

        return jsonify({"Mensaje": f"Registro con numero de empleado {worker_id} actualizado exitosamente."}), 200

    except mysql.connector.Error as err:
        return jsonify({"Error": f"Error al actualizar el dato: {str(err)}"}), 500

    finally:
        # Cerrar cursor y conexión
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
