import numpy as np

# Definir la función de Griewank
def griewank(x):
    sum_term = np.sum(x**2)
    prod_term = np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))
    return 1 + sum_term / 4000 - prod_term

# Calcular el gradiente de la función de Griewank de manera numérica
def numerical_gradient(f, x, epsilon=1e-6):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_plus = x.copy()
        x_minus = x.copy()
        x_plus[i] += epsilon
        x_minus[i] -= epsilon
        grad[i] = (f(x_plus) - f(x_minus)) / (2 * epsilon)
    return grad

# Parámetros del algoritmo de descenso de gradiente
learning_rate = 0.1
tolerance = 1e-6
max_iterations = 10000

# Inicializar el punto de partida (por ejemplo, para 3 dimensiones)
x = np.array([1.0, 1.0, 1.0])

# Inicializar el contador de iteraciones
iterations = 0

# Bucle de descenso de gradiente
while iterations < max_iterations:
    grad = numerical_gradient(griewank, x)  # Calcular el gradiente en el punto actual de manera numérica
    x_new = x - learning_rate * grad  # Actualizar el punto usando el gradiente y la tasa de aprendizaje
    
    # Verificar si la convergencia es satisfactoria
    if np.linalg.norm(x_new - x) < tolerance:
        break
    
    x = x_new  # Actualizar el punto actual
    iterations += 1

# Imprimir la solución óptima y el número de iteraciones
print("Solución óptima:", x)
print("Número de iteraciones:", iterations)
print("Valor de Griewank en la solución óptima:", griewank(x))
