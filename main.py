import sys
from BD.conexion import DAO
import funciones

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

    if opcion == 1:
        try:
            cursos = dao.obtener_cursos()
            if(len(cursos) > 0):
                funciones.listar_cursos(cursos)
            else:
                print("No se encontraron cursos")
        except:
            print("Ocurrio un error")
    elif opcion == 2:
        print("Registro")
    elif opcion == 3: 
        print("Actualización")
    elif opcion == 4:
        print("Eliminación")
    else:
        print("Opcion no valida")

menu()  

