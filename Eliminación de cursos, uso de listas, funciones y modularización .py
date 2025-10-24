def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

def buscar_curso_indice(cursos, nombre_buscar):
    nombre_buscar = nombre_buscar.lower()
    
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar:
            return i
    return -1

def eliminar_curso_por_nombre(cursos):
    print("\n--- ELIMINACIÓN DE CURSO ---")
    
    if not cursos:
        print("ERROR: No hay cursos registrados para eliminar.")
        return

    nombre_eliminar = input("Ingrese el nombre del curso a ELIMINAR: ").strip()

    indice_encontrado = buscar_curso_indice(cursos, nombre_eliminar)

    if indice_encontrado != -1:
        curso_eliminado = cursos[indice_encontrado]
        
        confirmacion = input(f"¿Desea realmente eliminar '{curso_eliminado['nombre']}' (Nota: {curso_eliminado['nota']:.2f})? (s/n): ").lower()
        
        if confirmacion == 's':
            cursos.pop(indice_encontrado) 
            print(f"Curso '{curso_eliminado['nombre']}' ELIMINADO correctamente.")
        else:
            print("Eliminación cancelada por el usuario.")
    else:
        print(f"ERROR: Curso '{nombre_eliminar}' no encontrado.")
    
    print("-" * 30)


def gestionar_notas_extendido():
    
    cursos = []
    
    print("--- INICIO DE GESTIÓN DE NOTAS ---")
    
    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Registrar nuevo curso (con nota)")
        print("2. Calcular promedio y análisis de contadores")
        print("3. Actualizar nota de un curso")
        print("4. ELIMINAR curso por nombre")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            nombre_curso = input("Nombre del curso: ").strip()
            if not nombre_curso:
                print("El nombre no puede ser vacío.")
                continue
            nota_str = input(f"Nota de {nombre_curso} (0-100): ").strip()
            if es_numerico(nota_str):
                nota_num = float(nota_str)
                if 0 <= nota_num <= 100:
                    cursos.append({"nombre": nombre_curso, "nota": nota_num})
                    print("Curso registrado.")
                else:
                    print("Nota fuera de rango.")
            else:
                print("Nota inválida.")

        elif opcion == '2':
            if not cursos:
                print("No hay cursos para analizar.")
                continue
            
            total_acumulado = sum(c['nota'] for c in cursos)
            contador = len(cursos)
            
            aprobados = sum(1 for c in cursos if c['nota'] >= 60)
            reprobados = contador - aprobados
            promedio = total_acumulado / contador
            
            print(f"\nPROMEDIO: {promedio:.2f}")
            print(f"Aprobados: {aprobados} | Reprobados: {reprobados}")
        
        elif opcion == '3':
            nombre_buscar = input("Curso a actualizar: ").strip()
            indice = buscar_curso_indice(cursos, nombre_buscar)
            
            if indice != -1:
                nueva_nota_str = input("Nueva nota (0-100): ").strip()
                if es_numerico(nueva_nota_str):
                    nueva_nota = float(nueva_nota_str)
                    if 0 <= nueva_nota <= 100:
                        cursos[indice]['nota'] = nueva_nota
                        print("Nota actualizada.")
                    else:
                        print("Nota fuera de rango.")
                else:
                    print("Nota inválida.")
            else:
                print("Curso no encontrado.")

        elif opcion == '4':
            eliminar_curso_por_nombre(cursos)
            
        elif opcion == '5':
            print("Saliendo del gestor.")
            break
            
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    gestionar_notas_extendido()
