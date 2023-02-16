import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="javi0712",
                db="crud_basico"
            )
        except Error as e:
            print("Error al intentar la conexion ", e)

    def obtener_cursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as e:
                print("Error al obtener cursos ", e)

                