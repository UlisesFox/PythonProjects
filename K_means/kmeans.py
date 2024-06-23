import numpy as np
import matplotlib.pyplot as plt

vida = [5, 5, 5, 6, 10, 9, 7, 4, 10, 3, 8, 2, 1, 3, 5, 10, 8, 7, 8, 1, 7, 1, 1, 1, 5, 6, 3, 1, 7, 2, 4, 7, 7, 10, 6, 5, 6, 1, 2, 7, 1, 2, 8, 4, 3, 2, 4, 8, 9, 2]
daño = [4, 7, 7, 2, 1, 3, 9, 8, 8, 2, 5, 10, 9, 2, 4, 3, 1, 7, 4, 8, 3, 8, 1, 6, 8, 10, 6, 5, 8, 6, 10, 6, 3, 6, 10, 9, 5, 6, 8, 4, 1, 8, 6, 1, 5, 9, 9, 6, 1, 3]
armadura = [2, 8, 3, 7, 3, 7, 1, 7, 9, 1, 3, 1, 10, 1, 6, 10, 1, 6, 3, 7, 2, 1, 8, 9, 3, 4, 9, 10, 4, 10, 10, 5, 7, 9, 10, 8, 3, 1, 2, 7, 4, 8, 4, 6, 8, 5, 2, 5, 9, 3]

vida_rangos = []
daño_rangos = []
armadura_rangos = []

for v, d, a in zip(vida, daño, armadura):
    if v <= 3:
        vida_rangos.append(0)
    elif 4 <= v <= 7:
        vida_rangos.append(1)
    else:
        vida_rangos.append(2)

    if d <= 3:
        daño_rangos.append(0)
    elif 4 <= d <= 7:
        daño_rangos.append(1) 
    else:
        daño_rangos.append(2)

    if a <= 3:
        armadura_rangos.append(0)
    elif 4 <= a <= 7:
        armadura_rangos.append(1)
    else:
        armadura_rangos.append(2)


datos = np.column_stack((vida_rangos, daño_rangos, armadura_rangos))

def calcular_distancia(punto1, punto2):
    return np.sqrt(np.sum((punto1 - punto2) ** 2))

def inicializar_centroides(datos, k):
    indices = np.random.choice(len(datos), k, replace=False)
    centroides = datos[indices]
    return centroides

def asignar_puntos_a_centroides(datos, centroides):
    asignaciones = []
    for punto in datos:
        distancias = [calcular_distancia(punto, centroide) for centroide in centroides]
        asignacion = np.argmin(distancias)
        asignaciones.append(asignacion)
    return asignaciones

def recalcular_centroides(datos, asignaciones, k):
    nuevos_centroides = []
    for i in range(k):
        puntos_asignados = [datos[j] for j in range(len(datos)) if asignaciones[j] == i]
        nuevo_centroide = np.mean(puntos_asignados, axis=0)
        nuevos_centroides.append(nuevo_centroide)
    return np.array(nuevos_centroides)

def convergencia(centroides_previos, centroides_actuales, tolerancia):
    return np.all(np.abs(centroides_previos - centroides_actuales) < tolerancia)

def k_means(datos, k, max_iteraciones=100, tolerancia=1e-4):
    centroides = inicializar_centroides(datos, k)
    iteracion = 0
    
    while iteracion < max_iteraciones:
        asignaciones = asignar_puntos_a_centroides(datos, centroides)
        nuevos_centroides = recalcular_centroides(datos, asignaciones, k)
        
        if convergencia(centroides, nuevos_centroides, tolerancia):
            break
        
        centroides = nuevos_centroides
        iteracion += 1
    
    return asignaciones, centroides, iteracion

if __name__ == "__main__":
    rangos_combinados = np.column_stack((vida_rangos, daño_rangos, armadura_rangos))
    
    k = 3

    asignaciones, centroides, iteraciones = k_means(rangos_combinados, k)
    
    print("Asignaciones finales:")
    for i, asignacion in enumerate(asignaciones):
        print(f"Punto {i + 1}: Clúster {asignacion + 1}")
    print("Centroides finales:")
    for i, centroide in enumerate(centroides):
        print(f"Centroide {i + 1}: {centroide.astype(int)}")
    print("Número de iteraciones:", iteraciones)
    
    plt.scatter(vida, daño, c=asignaciones, cmap='rainbow')
    plt.scatter(centroides[:, 0], centroides[:, 1], c='blue', marker='x', s=100, label='Google')
    plt.xlabel('Vida')
    plt.ylabel('Daño')
    plt.legend(loc='best')
    plt.title('Agrupación de Datos con K-Means')
    plt.show()