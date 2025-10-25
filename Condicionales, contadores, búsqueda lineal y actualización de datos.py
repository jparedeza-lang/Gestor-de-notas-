def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

def gestionar_notas_extendido():
    
    cursos = []
    
    total_acumulado = 0.0
    contador = 0
    
    aprobados = 0
    reprobados = 0

    print("--- REGISTRO DE NOTAS ---")
    print("Ingrese el nombre del curso y su nota (ej: Matematicas 85). Escriba 'FIN' para terminar.")

    while True:
        entrada_str = input("Ingrese curso y nota: ").strip()

        if entrada_str.upper() == "FIN":
            break

        if not entrada_str:
            print("ERROR: La entrada no puede estar vacía.")
            continue
        
        partes = entrada_str.rsplit(' ', 1)
        
        if len(partes) < 2:
            print("ERROR: Formato incorrecto. Ingrese el nombre del curso seguido de la nota.")
            continue
            
        nombre_curso = partes[0].strip()
        nota_str = partes[1].strip()

        if not nombre_curso:
            print("ERROR: El nombre del curso no puede estar vacío.")
            continue
            
        if es_numerico(nota_str):
            try:
                nota_num = float(nota_str)

                if 0 <= nota_num <= 100:
                    
                    cursos.append({"nombre": nombre_curso, "nota": nota_num})
                    total_acumulado += nota_num
                    contador += 1
                    print(f"Curso '{nombre_curso}' (Nota: {nota_num}) registrado con éxito.")
                
                else:
                    print("ERROR: La nota debe estar entre 0 y 100.")
                    
            except ValueError:
                print("ERROR: La nota debe ser un valor numérico válido.")

        else:
            print("ERROR: La nota debe ser un valor numérico válido.")
        
    
    print("\n" + "="*30)
    print("--- ANÁLISIS DE DATOS ---")
    print("="*30)

    if contador == 0:
        print("No se registraron cursos válidos para el análisis.")
        return
        
    
    # CONTADORES Y CONDICIONALES
    for curso in cursos:
        if curso['nota'] >= 60:
            aprobados += 1
        else:
            reprobados += 1

    print(f"Contadores: Aprobados ({aprobados}) | Reprobados ({reprobados})")
    
    promedio = total_acumulado / contador
    print(f"PROMEDIO GENERAL: {promedio:.2f}")

    
    print("\n--- ACTUALIZACIÓN DE NOTA ---")
    nombre_buscar = input("Ingrese el nombre del curso para ACTUALIZAR su nota: ").strip()

    indice_encontrado = -1
    
    # BÚSQUEDA LINEAL
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar.lower():
            indice_encontrado = i
            break
    
    # CONDICIONAL: Resultado de la búsqueda
    if indice_encontrado != -1:
        curso = cursos[indice_encontrado]
        print(f"Curso encontrado: {curso['nombre']} (Nota actual: {curso['nota']:.2f})")

        while True:
            nota_nueva_str = input("Ingrese la NUEVA nota (0-100): ").strip()
            try:
                nota_nueva = float(nota_nueva_str)
                # CONDICIONAL: Validación del Rango para la actualización
                if 0 <= nota_nueva <= 100:
                    
                    # ACTUALIZACIÓN DE DATOS
                    cursos[indice_encontrado]['nota'] = nota_nueva
                    print(f"Nota de '{curso['nombre']}' actualizada a: {nota_nueva:.2f}")
                    break
                else:
                    print("ERROR: La nota debe estar entre 0 y 100.")
            except ValueError:
                print("ERROR: Ingrese un valor numérico válido.")

    else:
        print(f"Curso '{nombre_buscar}' no encontrado mediante Búsqueda Lineal.")
        
    print("="*30)


if __name__ == "__main__":
    gestionar_notas_extendido()
