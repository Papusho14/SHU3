import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",      # Cambia esto a tu usuario de MySQL
        password="",  # Cambia esto a tu contraseña de MySQL
        database="prueba2"
    )
