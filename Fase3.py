# creo una funcion para mostrar el menu del programa contiene 4 opcines al seleccioneccionar una opcion se ejecuta la funcion  que corresponde
cursos = [] # lista para almacenar los cursos

def mostrar_menu():
    print("Menu de gestor de notas :")
    print("="*30)
    print("1. Agregar curso")
    print("2. eleminar curso ")
    print("3. ingresar notas y calcular el promdedio ")
    print("4. Salir")
    print("="* 20) # imprimo una linea de 20 guiones para separar el menu del resto del programa

    # creo una funcion para agregar un curso utilizare strip() para eliminar los espacios en blanco al inicio y al final del nombre del curso
def agregarcurso():
    curso = input("Ingrese el nombre del curso: ").strip()
    cursos.append(curso)
    print(f"Curso '{curso}' agregado exitosamente.")
    print("cursos actuales",cursos)

 # creo una duncion para eliminar un curso de la lista de cursos , muestro la lista de cursos con su indice y le pido al usuario que ingrese el numero del curso que desea eliminar 
 #i sera el indicador del indice y curso sera el nombre del curso , enumerate comienza en 1 para que el usuario no vea un indice 0 ademas que enumerate sirve para enumerar los elementos de una lista

def eliminarcurso():
    if not cursos:
        print("no hay cursos para eliminar")
    else:
        print("\nCursos disponibles:")
        for i, curso in enumerate(cursos, start=1):
            print(f"{i}. {curso}")

#utulizare try y except para manejar el error si el usuario ingresa un numero que no corresponde a ningun curso en la lista
#try preve de errores  y except maneja el error si el usuario ingresa un numero que no corresponde a ningun curso en la lista este bloque de codigo no se ejecuta y en su lugar se ejecuta el bloque de codigo dentro del except

    try:
        indice = int(input("Ingrese el numero del curso que desea eliminar: "))
        if 1 <= indice <= len(cursos):
            curso_eliminado = cursos.pop(indice - 1)
            print(f"Curso '{curso_eliminado}' eliminado exitosamente.")
        else:
            print("Numero de curso invalido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")


#creo la funcion para ingresar la N cantidad de notas que el usuario desee y calcular el promedio de las notas ingresadas

def ingresarnotasycalcularpromedio():
   
    curso = input("Ingrese el nombre del curso para el cual desea ingresar notas: ").strip()

    # creo un bloque parecido al bloque aneterir para manejar si el usuarrio ingresa una opcion no valida como el nombre de un curso que no existe en la lista

    try:
        cantidadnotas = int(input("Ingrese la cantidad de notas que desea ingresar: ")) #int para convertir la entrada del usario a un numero entero de str a int 
        if cantidadnotas <= 0:
            print("La cantidad de notas debe ser un numero mayor a 0.")
   
            print("Por favor, ingrese un numero valido para la cantidad de notas.")
            return  
        notas = [] # lista para almacenar las notas ingresadas por el usuario

        for i in range(cantidadnotas): #utilizo un range para iterar la cantidad de veces que el usuario desea ingresar nota    
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {i + 1}: ")) #float para convertir la entrada del usuario a un numero decimal de str a float
                    notas.append(nota)
                    break #s se rompe el ciclo while si la nota es valida
                except ValueError:
                    print("Por favor, ingrese un numero valido para la nota.")
         
        # creo un bloque para calcular el promedio de las notas ingresadas por el usuario
        if notas: 
            promediuo = sum(notas) / len(notas) # sum() para sumar todas las notas y len() para obtener la cantidad de notas ingresadas
            print(f"El promedio de las notas ingresadas para el curso '{curso}' es: {promediuo:}") 
        else:
            print("No se ingresaron notas.")

    except ValueError:
        print("Por favor, ingrese un numero valido para la cantidad de notas.")     
     

#creo una funcion principal   donde estaran todas las funcioes creadas aneteriormente y un ciclo while para que el menu se muestre hasta que el usuario decida salir del programa

def main():

    while True: #creo un bucle
        mostrar_menu() #llamo a la funcion mostrar_menu
          #utilizo try para manejar errores de entrada del usuario si selecciona una opcion no valida mostrare un mensaje de error y el menu se mostrara de nuevo
    
        try :
            opcion = int(input("Seleccione una opcion (1-4): ")) #int para convertir la entrada del usuario a un numero entero de str a int
            if opcion == 1:
                agregarcurso()#llamo a la funcion agregarcurso
            elif opcion == 2:
                eliminarcurso()#llamo a la funcion eliminarcurso
            elif opcion == 3:
                ingresarnotasycalcularpromedio()#llamo a la funcion ingresarnotasycalcularpromedio en esta funcion la N cantidad de notas que el usuario se sumaron su valor cada una y se dividio entre la cantidad de notas para obtener el promedio
            elif opcion == 4:
                print("Saliendo del programa. ¡Hasta luego!")
                break #rompo el ciclo while si el usuario selecciona la opcion 4
            else:
                print("Opcion invalida. Por favor, seleccione una opcion del 1 al 4.")
        except ValueError: #valueerror es una clausula para manejar errores de valor si el usuario ingresa un valor no valido
            print("Por favor, ingrese un numero valido para la opcion.")
        
      


if __name__ == "__main__":
    main() #llamo a la funcion main para ejecutar el programa