import sys

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
    print(opcion)


menu()  

