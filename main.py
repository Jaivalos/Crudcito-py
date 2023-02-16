import sys
from BD.conexion import DAO
import funciones
from os import system

def menu():

    #Creacion de menu de opciones
    dato = True
    while (dato):
        opcion_correcta = False
        while (not opcion_correcta):
            print("---------------- Menú Principal ----------------")
            print("1. Listar Cursos")
            print("2. Añadir Curso")
            print("3. Actualizar Curso")
            print("4. Eliminar Curso")
            print("5. Salir")

            opcion = int(input("\n Selecciona una opción: "))

            if (opcion < 1) or (opcion > 5):
                print("Dato incorrecto, seleccione una opcion valida")
            elif (opcion == 5): 
                dato = False
                print("Gracias por usar el sistema") 
                break
            else:
                opcion_correcta = True
                ejecutar_opcion(opcion)


def ejecutar_opcion(opcion):
    dao = DAO()

    #----------------------OPCION 1----------------------
    if opcion == 1:
        try:
            cursos = dao.obtener_cursos()
            if(len(cursos) > 0):
                funciones.listar_cursos(cursos)
            else:
                system("cls")
                print("No se encontraron cursos")
        except:
            print("Ocurrio un error")

    #----------------------OPCION 2----------------------

    elif opcion == 2:
        curso = funciones.datos_creacion_curso()
        try:
            dao.crear_curso(curso)
        except:
            print("Ocurrio un error")

    #----------------------OPCION 3----------------------
        
    elif opcion == 3: 
        try:
            cursos = dao.obtener_cursos()
            if(len(cursos) > 0):
                curso = funciones.datos_actualizacion_curso(cursos)
                if curso:
                    dao.actualizar_curso(curso)
                else:
                    print("Codigo de curso a actualizar no encontrado")
            else:
                print("No se encontraron cursos")
        except:
            print("Ocurrio un error")

    #----------------------OPCION 3----------------------

    elif opcion == 4:
        try:
            cursos = dao.obtener_cursos()
            if(len(cursos) > 0):
                codigo_eliminar = funciones.datos_eliminacion_curso(cursos)

                if (codigo_eliminar != ""):
                    dao.eliminar_curso(codigo_eliminar)
                else:
                    print("Codigo de curso no encontrado")
            else:
                print("No se encontraron cursos")
        except:
            print("Ocurrio un error")
    else:
        print("Opcion no valida")

menu()  

