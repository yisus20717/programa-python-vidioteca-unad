"""Curso: Fundamentos de Programación (213022_562)
Nombre del Estudiante: Jesus Manuel Beltran Motato
Fuente: Autoria propia"""




def contar_titulos_populares_y_recientes(matriz_videoteca, umbral_calificacion, anio_limite):
    """ Módulo (función) encargado de ejecutar la lógica de negocio.
    Evalúa y cuenta cuántos títulos de la matriz tienen una calificación
    mayor o igual al umbral Y un año de lanzamiento posterior o igual al límite. """

    conteo = 0

    print("\n####################### Evaluando títulos según criterios de auditoría #######################")
    for pelicula in matriz_videoteca:
        # Estructura de la fila de la matriz: [Título, Año de Lanzamiento, Calificación (1-10), Género]
        titulo = pelicula[0]
        anio = pelicula[1]
        calificacion = pelicula[2]
        
        # Lógica de Negocio: Validación con estructura condicional básica
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            print(f" -> Cumple: '{titulo}' | Año: {anio} | Calificación: {calificacion:.1f}")
            conteo += 1

    if conteo == 0:
        print(" Avisos: Ningún título cumple los criterios establecidos.")
    else:
        print(" Evaluación realizada con éxito.")
            
    return conteo

def mostrar_catalogo_videoteca(matriz_videoteca):
    """
    Función auxiliar para mostrar en consola la matriz completa de datos
    de manera tabulada y ordenada con formato de decimales controlado.
    """
    print("\n======================= CATÁLOGO DE LA VIDEOTECA =======================")
    print(f"{'Título':<35} | {'Año':<6} | {'Calificación':<12} | {'Género':<15}")
    print("-" * 75)
    for pelicula in matriz_videoteca:
        print(f"{pelicula[0]:<35} | {pelicula[1]:<6} | {pelicula[2]:<12.1f} | {pelicula[3]:<15}")
    print("========================================================================")

def main():
    # Matriz: Creación de la matriz con 7 títulos 
    # Formato de almacenamiento: [Título, Año de Lanzamiento, Calificación (1-10), Género]
    videoteca = [
        ["Inception", 2010, 8.8, "Ciencia Ficción"],
        ["Interstellar", 2014, 8.6, "Ciencia Ficción"],
        ["Parasite", 2019, 8.5, "Drama"],
        ["Everything Everywhere All at Once", 2022, 8.0, "Acción"],
        ["Oppenheimer", 2023, 8.4, "Biografía"],
        ["Dune: Part Two", 2024, 8.7, "Ciencia Ficción"],
        ["The Matrix", 1999, 8.7, "Ciencia Ficción"]
    ]
    
    print("SISTEMA AUTOMATIZADO DE AUDITORÍA - VIDEOTECA DIGITAL - JESUS MANUEL BELTRAN MOTATO")
    
    # ejecucion de los datos iniciales de la matriz
    mostrar_catalogo_videoteca(videoteca)
    
    print("\n[Configuración de parámetros de búsqueda]")
    
    # Uso del ciclo while para validar la calificación dentro del rango correcto
    # Validación de calificación con control de errores
    while True: #crea un ciclo infinito que se repite hasta que se detenga.
        try:
            umbral_cali = float(input("Ingrese el umbral de calificación mínima (1.0 a 10.0): "))
            if 1.0 <= umbral_cali <= 10.0: #Cuando el usuario ingresa un valor correcto (por ejemplo, una calificación entre 1.0 y 10.0), se ejecuta el break
                break#El break rompe el ciclo inmediatamente y hace que el programa continúe con la siguiente instrucción fuera del while
            else:
                print("Calificación fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entre 1.0 y 10.0.")

    # Validación de año con control de errores
    while True:
        try:
            anio_lim = int(input("Ingrese el año de lanzamiento límite (mayor a 0): "))
            if anio_lim > 0:
                break
            else:
                print("Año inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero mayor a 0.")

    
    # Invocación del módulo de conteo pasando la matriz y los parámetros dinámicos
    total_cumplen = contar_titulos_populares_y_recientes(videoteca, umbral_cali, anio_lim)
    
    # Salida: Mostrar el conteo total de títulos que cumplen con ambos criterios
    print("\n====================== REPORTE FINAL DE SALIDA ======================")
    print(f" Cantidad total de títulos que satisfacen los criterios: {total_cumplen}")
    print("=====================================================================")


if __name__ == "__main__":
    main()