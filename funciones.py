from os import system

#----------------------LISTAR CURSOS----------------------

def listar_cursos(cursos):
    system("cls")
    print("\nCursos: \n")
    contador = 1
    for cur in cursos:
        datos = "{0}. Codigo: {1} | Nombre: {2} ({3} creditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print("")

#----------------------CREAR CURSO----------------------

def datos_creacion_curso():
    system("cls")

    cod_correto = False
    while(not cod_correto):
        codigo = input("Ingrese el codigo del curso: ")
        if((len(codigo) == 2) and (codigo.isnumeric())):
            if(int(codigo) > 0):
                cod_correto = True
                codigo = int(codigo)
            else:
                print("El codigo debe ser mayor a 0")
        else:
            print("Codigo incorrecto, debe tener 2 digitos y ser un numero")

    nombre = input("Ingrese el nombre del curso: ")

    creditos_correctos = False
    while(not creditos_correctos):
        creditos = input("Ingrese la cantidad de creditos del curso: ")
        if ((creditos.isnumeric())):
            if(int(creditos) > 0):
                creditos_correctos = True
                creditos = int(creditos)
            else:
                print("Los creditos deben ser mayor a 0")
        else:
            print("Creditos incorrectos")

    curso = (codigo, nombre, creditos)
    return curso

#----------------------ACTUALIZAR CURSOS----------------------

def datos_actualizacion_curso(cursos):
    listar_cursos(cursos)
    existe_codigo = False
    codigo_editar = input("Ingrese codigo del curso a editar: ")
    for cur in cursos:
        if cur[0] == int(codigo_eliminar):
            existe_codigo = True
            break

    if existe_codigo == True:
        nombre = input("Ingrese el nombre del curso: ")

        creditos_correctos = False
        while(not creditos_correctos):
            creditos = input("Ingrese la cantidad de creditos del curso: ")
            if ((creditos.isnumeric())):
                if(int(creditos) > 0):
                    creditos_correctos = True
                    creditos = int(creditos)
                else:
                    print("Los creditos deben ser mayor a 0")
            else:
                print("Creditos incorrectos")
        curso = (codigo_editar, nombre, creditos)
    else:
        curso = None

    return curso

#----------------------ELIMINAR CURSOS----------------------

def datos_eliminacion_curso(cursos):
    listar_cursos(cursos)
    existe_codigo = False
    codigo_eliminar = input("Ingrese codigo del curso a eliminar: ")
    for cur in cursos:
        if cur[0] == int(codigo_eliminar):
            existe_codigo = True
            break

    if existe_codigo == False:
        codigo_eliminar = ""

    return codigo_eliminar