cursos = [] # lista para almacenar los cursos
historial = [] # lista para almacenar el historial de operaciones


def validar_nota(mensaje): #funcion que verifica que la nota sea entre 0 y  100 
    while True:
        try: #utlizamos para manejar de forma discreta si el usuario comete un error 
            nota = float(input(mensaje))
            if 0 <= nota <= 100: #validamos el valor
                return nota
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:#permite que el programa siga funcionando a un si el usuarion nos proporciono un dato erroneo
            print("Entrada inválida. Por favor, ingrese un número.")

def buscar_curso_lineal_indice(nombre_buscado):
    nombre_buscado = nombre_buscado.lower() #  en esta linea de codigo utilizamos .lower para que el programa no sea sensible a las mayusculas y minisculas
    for i, curso in enumerate(cursos): #enumero los cursos con su inidce empezamos desde 0 hasta N 
        if nombre_buscado in curso['nombre'].lower():
            return i 
    return -1 

def buscar_curso_binaria_indice(nombre_buscado): # funcion que utilizamos el metodo de busqueda binaria para buscar el curso por nombre
    nombre_buscado = nombre_buscado.lower()
    
    lista_ordenada = sorted(cursos, key=lambda x: x['nombre'].lower()) #ordena la lista 
    
    inicio = 0
    fin = len(lista_ordenada) - 1
    
    while inicio <= fin: #
        medio = (inicio + fin) // 2
        nombre_medio = lista_ordenada[medio]['nombre'].lower()
        
        if nombre_medio == nombre_buscado: # comprueba si el curso fue encontrado 
            
            return medio, lista_ordenada
        elif nombre_buscado < nombre_medio:
            fin = medio - 1
        else:
            inicio = medio + 1
            
    return -1, None #si el bucle termina no se encontro el curso 




def ordenamiento_burbuja_nota(lista): # esta funcion ordena los cursos por nota de forma descendente
    n = len(lista)
    lista_copia = lista.copy() 
    
    for i in range(n): #determina el rango hasta donde llegara 
        for j in range(0, n - i - 1):
            if lista_copia[j]['nota'] < lista_copia[j + 1]['nota']:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    return lista_copia

def ordenamiento_insercion_nombre(lista): #ordenamos los cursos por nombre que se basara en la primera letra del nombre 
    n = len(lista)
    lista_copia = lista.copy() #creo una copia de la lista para no afectar a la original 

    for i in range(1, n): #itera sobre los elementos desordenados, a partir del índice 1
        key_curso = lista_copia[i]
        j = i - 1
        
        while j >= 0 and key_curso['nombre'].lower() < lista_copia[j]['nombre'].lower(): #empiza a ordenar 
            lista_copia[j + 1] = lista_copia[j] # inserta el elemento  a su posicion ordenada 
            j -= 1
        lista_copia[j + 1] = key_curso
        
    return lista_copia #devuelve una lista ordenada de los  cursos


def mostrar_menu():
    # creo una funcion para mostrar el menu del programa contiene 13 opciones al seleccioneccionar una opcion se ejecuta la funcion  que corrresponde a su numero asignado
    print("\n====== GESTOR DE NOTAS ACADEMICAS ======")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre ")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota ")
    print("9. Ordenar cursos por nombre ")
    print("10. Buscar curso por nombre ")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios ")
    print("13. Salir")
    print("="* 40) # imprimo una linea de 20 guiones para separar el menu con la linea de entrada de la consola 

def agregarcurso():
    # creo una funcion para agregar un curso utilizare strip() para eliminar los espacios en blanco al inicio y al final del nombre del curso
    
    # Solicita el nombre y la nota del curso , los almacena en la lista de cursos
    
    
    while True: # Bucle para solicitar y validar que el nombre del curso no esté vacío.

        curso_nombre = input("Ingrese el nombre del curso: ").strip()
        if curso_nombre:
            break
        else:
            print("El nombre del curso no puede estar vacío.")
            
    # verificamos que la nota sea entre (0-100)
    nota_obtenida = validar_nota(f"Ingrese la nota obtenida para '{curso_nombre}' (0-100): ")

    # Crea el diccionario con la estructura correcta
    nuevo_curso = {
        "nombre": curso_nombre,
        "nota": nota_obtenida
    }
    
    cursos.append(nuevo_curso) #añadimos el curso a la lista global cursos
    
    # Se guarda la operación en la pila de historial
    historial.append(f"Se agregó: '{curso_nombre}' - Nota: {nota_obtenida}")
    
    print(f"Curso '{curso_nombre}' registrado con éxito con nota: {nota_obtenida}.")#le confirmanos al usuario que la operacion fue exitosa 

def mostrar_todos_cursos(): #funcion para mostrar todos los cursos
    
    if not cursos: #verificamos que la lista no este vacia 
        print("No hay cursos registrados.")
        return

    print("\nCursos registrados:")
    for i, curso in enumerate(cursos, start=1): #enumeramos todos los cursos con un su indice , empezamos desde 1
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']:.2f}")

def calcular_promedio_general():
    # creo un bloque para calcular el promedio de las notas ingresadas por el usuario
    if not cursos:
        print("No hay cursos registrados para calcular el promedio.")
        return
    
    total_notas = sum(curso['nota'] for curso in cursos) 
    promedio = total_notas / len(cursos)
    
    print(f"Promedio general: {promedio:.2f}")

def contar_aprobados_reprobados():  # esta funcion permite mostrar la cantidad de cursos aprobados y reprobados 
    if not cursos:
        print("No hay cursos registrados para el conteo.")
        return
        
    aprobados = sum(1 for curso in cursos if curso['nota'] >= 60) # El 1 se suma solo si la condición es verdadera 
    reprobados = len(cursos) - aprobados # Calcula los reprobados restando los aprobados del total de cursos registrados
    
    print(f"\nCursos aprobados (Nota >= 60): {aprobados}") 
    print(f"Cursos reprobados (Nota < 60): {reprobados}")

def buscar_curso_lineal(): #funcion para buscar cursos por nombre 
    if not cursos:
        print("No hay cursos para buscar.")
        return
        
    nombre_buscado = input("Ingrese el nombre del curso que busca : ").strip()  #pedimos que ingrese el nombre del curso que desea buscar
    
    indice = buscar_curso_lineal_indice(nombre_buscado) # Llama a la función auxiliar que implementa la búsqueda lineal real, devuelve el índice del curso o -1 si no se encuentra
    
    if indice != -1:
        curso = cursos[indice] # accede al diccionario del curso usando el índice
        print(f"\nCurso encontrado: {curso['nombre']} - Nota: {curso['nota']:.2f}")
    else:
        print("Curso no encontrado .")

def actualizar_nota_curso(): # funcion para actualizar una nota existente
    if not cursos: 
        print("No hay cursos para actualizar.")
        return
        
    nombre_curso = input("Ingrese el nombre completo del curso para actualizar la nota: ").strip()
    
    indice = buscar_curso_lineal_indice(nombre_curso)  # Llama a la función auxiliar de búsqueda lineal para encontrar el indice del curso
    
    if indice != -1:
        curso = cursos[indice]
        nota_anterior = curso['nota']  #guarda la nota actual antes de la modificacion 
        print(f"Curso encontrado: {curso['nombre']} - Nota actual: {nota_anterior:.2f}")
        
        nueva_nota = validar_nota("Ingrese la nueva nota (0-100): ")# Pide y valida la nueva nota usando la función auxiliar
        
        cursos[indice]['nota'] = nueva_nota # Actualiza el valor de la nota en el diccionario de la lista principal
        historial.append( #Registra el cambio en la pila de historial 
            f"Se actualizó: {curso['nombre']} - Nota anterior: {nota_anterior:.2f} -> Nueva nota: {nueva_nota:.2f}"
        )
        print(f"Nota de '{curso['nombre']}' actualizada correctamente a {nueva_nota:.2f}.")
    else:
        print("Curso no encontrado.")

def eliminar_un_curso():
    # creo una duncion para eliminar un curso de la lista de cursos , muestro la lista de cursos con su indice y le pido al usuario que ingrese el numero del curso que desea eliminar 
    if not cursos:
        print("No hay cursos para eliminar.")
        return
        
    nombre_curso = input("Ingrese el nombre completo del curso a eliminar: ").strip() #pido el nombre del curso 
    
    indice = buscar_curso_lineal_indice(nombre_curso) #llamo a la funcion auxiliar para saber su indice 
    
    if indice != -1:
        curso_a_eliminar = cursos[indice] #obtengo el diccionario del curso que voy a eliminar 
        confirmacion = input(f"¿Está seguro que desea eliminar '{curso_a_eliminar['nombre']}'? (s/n): ").lower() #muestro una confirmacion para eleminar el curso s para si n para no 
        
        if confirmacion == 's': #procedo la confirmacion si es S
            cursos.pop(indice) #elimino el curso 
            historial.append(f"Se eliminó: {curso_a_eliminar['nombre']} - Nota: {curso_a_eliminar['nota']:.2f}")
            print(f"Curso '{curso_a_eliminar['nombre']}' eliminado correctamente.")
        else:
            print("Operación de eliminación cancelada.")
    else:
        print("Curso no encontrado.")

def ordenar_cursos_por_nota(): #ordeno los curso por la nota mas alta a las mas pequeña
    if not cursos:
        print("No hay cursos para ordenar")
        return
        
    cursos_ordenados = ordenamiento_burbuja_nota(cursos) # llamo la funcion auxiliar y entrego la lista de cursos
    
    print("\n--- Cursos Ordenados por Nota (Descendente - Burbuja) ---")
    for i, curso in enumerate(cursos_ordenados, start=1):# itera sobre la lista ordenada e imprime cada curso con su indice comenzando en 1.
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']:.2f}")

def ordenar_cursos_por_nombre(): 
    if not cursos:
        print("No hay cursos para ordenar")
        return
        
    cursos_ordenados = ordenamiento_insercion_nombre(cursos) #llamo a la funcion de ordenamiento por nombre y entrego la llista de cursos
    
    print("\n--- Cursos Ordenados Alfabéticamente por Nombre (Inserción) ---")
    for i, curso in enumerate(cursos_ordenados, start=1): #Itera sobre la lista ordenada e imprime cada curso con su índice comenzando en 1
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']:.2f}")

def buscar_curso_binaria():
    if not cursos:
        print("No hay cursos para buscar.")
        return
        
    nombre_buscado = input("Ingrese el nombre del curso a buscar : ").strip() # Pide el nombre a buscar y lo limpia
    
    indice_encontrado, lista_temporal = buscar_curso_binaria_indice(nombre_buscado)  # Recibe el índice del curso en la lista ordenada temporal y la lista temporal

    if indice_encontrado != -1:
        curso = lista_temporal[indice_encontrado]# usa el índice para obtener el diccionario completo
        print(f"\nCurso encontrado: {curso['nombre']} - Nota: {curso['nota']:.2f}")
    else:
        print("Curso no encontrado.")

def simular_cola_revision():
    cola_solicitudes = [] #creo una lista que simulara la cola 
    
    print("\n--- Simulación de Cola de Solicitudes de Revisión ---")
    print("Ingrese los cursos a revisar. Escriba 'fin' para terminar.")
    
    while True: #Bucle para recibir las solicitudes del usuario y agregarlas a la cola
        curso_revision = input("> ").strip()
        if curso_revision.lower() == 'fin':
            break
        if curso_revision:
            cola_solicitudes.append(curso_revision) # Agrega al final de la lista
            print(f"'{curso_revision}' agregado a la cola.")
            
    if not cola_solicitudes:
        print("No se ingresaron solicitudes.")
        return

    print("\nProcesando solicitudes (orden de ingreso):")
    
    while cola_solicitudes: ## Usa .pop(0) para remover y obtener el primer elemento
        curso_actual = cola_solicitudes.pop(0)
        print(f"Revisando: {curso_actual}")

    print("Todas las solicitudes han sido procesadas.")


def mostrar_historial_cambios(): 
    # esta funcion va guardar todas las operaciones en una lista para luego mostrar al usuario si lo desea tambien podra borrar alguna operacion si lo desea 
    if not historial:
        print("No hay historial de cambios recientes.")
        return
        
    print("\n--- Historial de Cambios Recientes (Pila: Último cambio primero) ---")
    
    for i, operacion in enumerate(reversed(historial), start=1): #enumero todas las operaciones de la lista historial empezando por 1
        print(f"{i}. {operacion}")

def eliminar_ultima_operacion(): # creo una funcion para eliminar la ultima operacion realizada del historial 
    if not historial: 
        print("No hay operaciones en el historial para eliminar")
        return
    
    ultima_operacion = historial.pop() #elimino la operacion de historial se borra la ultima agregadad a la lista 
    print(f"Ultima operacion eliminada del historial: {ultima_operacion}")
    print(f"Quedan {len(historial)} operaciones en el historial")


#creo una funcion principal   donde estaran todas las funcioes creadas aneteriormente y un ciclo while para que el menu se muestre hasta que el usuario decida salir del programa

def main(): # declaramos la funcion principal 

    while True: #creo un bucle
        mostrar_menu() #llamo a la funcion mostrar_menu
        
        try:
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == '1':
                agregarcurso() #declaro cada opcion con su indice y la funcion que necesitara 
            elif opcion == '2':
                mostrar_todos_cursos()
            elif opcion == '3':
                calcular_promedio_general()
            elif opcion == '4':
                contar_aprobados_reprobados()
            elif opcion == '5':
                buscar_curso_lineal()
            elif opcion == '6':
                actualizar_nota_curso()
            elif opcion == '7':
                eliminar_un_curso()
            elif opcion == '8':
                ordenar_cursos_por_nota()
            elif opcion == '9':
                ordenar_cursos_por_nombre()
            elif opcion == '10':
                buscar_curso_binaria()
            elif opcion == '11':
                simular_cola_revision()
            elif opcion == '12':
                mostrar_historial_cambios()
            elif opcion == '13':
                print("Gracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
                break # Usamos 'break' en lugar de sys.exit()
            else:
                print("Opcion inválida. Por favor, seleccione un número del 1 al 13.")
        
        except ValueError: #valueerror es una clausula para manejar errores de valor si el usuario ingresa un valor no valido
            print("Por favor, ingrese un número válido para la opción.")

if __name__ == "__main__":
    main() #llamo a la funcion main para ejecutar el programa