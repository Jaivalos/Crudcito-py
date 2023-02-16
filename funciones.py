from os import system

def listar_cursos(cursos):
    system("cls")
    print("\nCursos: \n")
    contador = 1
    for cur in cursos:
        datos = "{0}. Codigo: {1} | Nombre: {2} ({3} creditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print("")