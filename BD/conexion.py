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
            

    def crear_curso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "Insert into curso (codigo, nombre, creditos) values ('{0}', '{1}', '{2}')"
                cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print("Curso agregado.")
            except Error as e:
                print("Error al crear curso ", e)

    def actualizar_curso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "update curso set nombre='{0}', creditos= '{1}' where codigo= '{2}')"
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print("Curso actualizado.")
            except Error as e:
                print("Error al actualizar curso ", e)

    def eliminar_curso(self, codigo_eliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "delete from curso where codigo = {0}"
                cursor.execute(sql.format(codigo_eliminar))
                self.conexion.commit()
                print("Curso eliminado.")
            except Error as e:
                print("Error al eliminar curso ", e)


                