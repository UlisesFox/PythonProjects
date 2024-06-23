import math

def calcular_tiro_parabolico(masa_objeto, constante_resorte, longitud_resorte, angulo_lanzamiento):
    # Convertir el ángulo de grados a radianes
    angulo_radianes = math.radians(angulo_lanzamiento)

    # Calcular la velocidad inicial del objeto
    velocidad_inicial = math.sqrt(constante_resorte / masa_objeto) * longitud_resorte

    # Calcular las componentes horizontal y vertical de la velocidad inicial
    velocidad_inicial_x = velocidad_inicial * math.cos(angulo_radianes)
    velocidad_inicial_y = velocidad_inicial * math.sin(angulo_radianes)

    # Calcular el tiempo de vuelo
    tiempo_vuelo = (2 * velocidad_inicial_y) / 9.8

    # Calcular la altura máxima
    altura_maxima = (velocidad_inicial_y ** 2) / (2 * 9.8)

    # Calcular el alcance horizontal
    alcance_horizontal = velocidad_inicial_x * tiempo_vuelo

    # Calcular la velocidad en el punto más alto
    velocidad_maxima = math.sqrt(2 * 9.8 * altura_maxima)

    # Calcular la fuerza de impacto
    fuerza_impacto = masa_objeto * velocidad_maxima / tiempo_vuelo

    # Calcular la velocidad final
    velocidad_final = math.sqrt(velocidad_inicial_x ** 2 + (velocidad_inicial_y - 9.8 * tiempo_vuelo) ** 2)

    # Calcular la velocidad angular y aceleración angular
    velocidad_angular = velocidad_inicial_y / longitud_resorte
    aceleracion_angular = (velocidad_inicial_y - 9.8 * tiempo_vuelo) / longitud_resorte

    # Calcular la fuerza aplicada
    fuerza_aplicada = masa_objeto * aceleracion_angular

    # Calcular la energía potencial elástica
    energia_potencial_elastica = 0.5 * constante_resorte * (longitud_resorte ** 2)

    # Imprimir los resultados
    print("\nResultados del tiro parabólico:\n")
    print("Altura máxima:", altura_maxima)
    print("\nTiempo de vuelo:", tiempo_vuelo)
    print("\nVelocidad final:", velocidad_final)
    print("\nFuerza aplicada:", fuerza_aplicada)
    print("\nFuerza de impacto:", fuerza_impacto)
    print("\nVelocidad inicial:", velocidad_inicial)
    print("\nVelocidad angular:", velocidad_angular)
    print("\nAlcance horizontal:", alcance_horizontal)
    print("\nAceleración angular:", aceleracion_angular)
    print("\nVelocidad en el punto más alto:", velocidad_maxima)
    print("\nEnergía potencial elástica:", energia_potencial_elastica)

# Función para preguntar al usuario si desea realizar otra operación
def realizar_otra_operacion():
    respuesta = input("\n¿Desea realizar otra operación? (s/n): ")
    return respuesta.lower() == 's'

# Loop principal del programa
while True:
    print("\nNota: solo poner valores numéricos, el programa no acepta letras.")
    masa_objeto = float(input("Ingrese la masa del objeto (ej. 0.5 kg): "))  # kg
    constante_resorte = float(input("Ingrese la constante de elasticidad (ej. 100 N/m): "))  # N/m
    longitud_resorte = float(input("Ingrese la longitud del resorte (ej. 0.2 m): ")) # m
    angulo_lanzamiento = float(input("Ingrese el ángulo de lanzamiento (ej. 45°): "))  # grados

    calcular_tiro_parabolico(masa_objeto, constante_resorte, longitud_resorte, angulo_lanzamiento)

    if not realizar_otra_operacion():
        break
