cursos = [] # lista para almacenar los cursos
historial = [] # lista para almacenar el historial de operaciones


def validar_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 100:
                return nota
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

# Se incluye la versión de Inserción para diccionarios (por nombre)
def ordenamiento_insercion_nombre(lista):
    n = len(lista)
    lista_copia = lista.copy() 

    for i in range(1, n):
        key_curso = lista_copia[i]
        j = i - 1
        
        while j >= 0 and key_curso['nombre'].lower() < lista_copia[j]['nombre'].lower():
            lista_copia[j + 1] = lista_copia[j]
            j -= 1
        lista_copia[j + 1] = key_curso
        
    return lista_copia

# Se incluye la función de Ordenamiento Burbuja para diccionarios (por nota descendente)
def ordenamiento_burbuja_nota(lista):
    n = len(lista)
    lista_copia = lista.copy() 
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j]['nota'] < lista_copia[j + 1]['nota']:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    return lista_copia

# La función original 'ordenamiento_insercion' se elimina por ser redundante y solo manejar strings

def mostrar_menu():
    # creo una funcion para mostrar el menu del programa contiene 7 opciones al seleccioneccionar una opcion se ejecuta la funcion  que corresponde
    print("Menu de gestor de notas :")
    print("="*30)
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Ordenar cursos por nombre ")
    print("5. Ordenar cursos por nota ")
    print("6. Simular cola de revisión")
    print("7. Mostrar historial ")
    print("8. Salir")
    print("="* 20) # imprimo una linea de 20 guiones para separar el menu del resto del programa

def agregarcurso():
    # creo una funcion para agregar un curso utilizare strip() para eliminar los espacios en blanco al inicio y al final del nombre del curso
    while True:
        curso_nombre = input("Ingrese el nombre del curso: ").strip()
        if curso_nombre:
            break
        else:
            print("El nombre del curso no puede estar vacío.")
            
    # La nota es necesaria para el nuevo formato
    nota_obtenida = validar_nota(f"Ingrese la nota obtenida para '{curso_nombre}' (0-100): ")

    nuevo_curso = {
        "nombre": curso_nombre,
        "nota": nota_obtenida
    }
    
    cursos.append(nuevo_curso)
    historial.append(f"Se agregó: '{curso_nombre}' - Nota: {nota_obtenida}")
    print(f"Curso '{curso_nombre}' registrado con éxito con nota: {nota_obtenida}.")

def mostrar_todos_cursos():
    if not cursos: 
        print("No hay cursos registrados.")
        return

    print("\nCursos registrados:")
    for i, curso in enumerate(cursos, start=1): 
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']:.2f}")

def calcular_promedio_general():
    # crea la funcionalidad para calcular el promedio de todas las notas en la lista 'cursos'
    if not cursos:
        print("No hay cursos registrados para calcular el promedio.")
        return
    
    total_notas = sum(curso['nota'] for curso in cursos)
    promedio = total_notas / len(cursos)
    
    print(f"Promedio general: {promedio:.2f}")

def simular_cola_revision():
    cola_solicitudes = []
    
    print("\n--- Simulación de Cola de Solicitudes de Revisión ---")
    print("Ingrese los cursos a revisar. Escriba 'fin' para terminar.")
    
    while True:
        curso_revision = input("> ").strip()
        if curso_revision.lower() == 'fin':
            break
        if curso_revision:
            cola_solicitudes.append(curso_revision) # Agregar al final (Enqueue)
            print(f"'{curso_revision}' agregado a la cola.")
            
    if not cola_solicitudes:
        print("No se ingresaron solicitudes.")
        return

    print("\nProcesando solicitudes (orden de ingreso):")
    
    while cola_solicitudes:
        curso_actual = cola_solicitudes.pop(0) # Quitar del inicio (Dequeue - FIFO)
        print(f"Revisando: {curso_actual}")

    print("Todas las solicitudes han sido procesadas.")


def mostrar_historial_cambios(): 
    # esta funcion va guardar todas las operaciones en una lista para luego mostrar al usuario si lo desea tambien podra borrar alguna operacion si lo desea 
    if not historial:
        print("No hay historial de operaciones")
        return
    
    print("Historial de operaciones:")
    for i, operacion in enumerate(reversed(historial), start=1):
        print(f"{i}. {operacion}")


# Las funciones 'eliminarcurso' e 'ingresarnotasycalcularpromedio' y 'eliminar_ultima_operacion' no se mapean directamente
# al menú expandido de estructuras de datos, pero se mantienen sus nombres por compatibilidad con tu código inicial.
def eliminarcurso():
    # Este código necesita la estructura de diccionario para funcionar con el resto.
    print("La función eliminar curso requiere implementación detallada con búsqueda.")

def ingresarnotasycalcularpromedio():
    # La funcionalidad de promedio ahora está en calcular_promedio_general.
    print("La función de ingresar notas ha sido reemplazada por 'calcular_promedio_general'.")

def main():

    while True: #creo un bucle
        mostrar_menu() #llamo a la funcion mostrar_menu
        
        try :
            opcion = input("Seleccione una opcion (1-8): ").strip()
            
            if opcion == '1':
                agregarcurso()
            elif opcion == '2':
                mostrar_todos_cursos()
            elif opcion == '3':
                calcular_promedio_general()
            elif opcion == '4':
                ordenar_cursos_por_nombre()
            elif opcion == '5':
                ordenar_cursos_por_nota()
            elif opcion == '6':
                simular_cola_revision()
            elif opcion == '7':
                mostrar_historial_cambios()
            elif opcion == '8':
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opcion invalida. Por favor, seleccione una opcion del 1 al 8.")
        
        
if __name__ == "__main__":
    main()
