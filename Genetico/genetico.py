import random

# Función para evaluar la aptitud de un individuo
def evaluate_individual(individual, target_attribute, target_value):
    vida, danio, velocidad, shiny = individual

    if target_attribute == "vida":
        target = vida
    elif target_attribute == "danio":
       target = danio
    elif target_attribute == "velocidad":
        target = velocidad

    fitness_score = 1 / (1 + abs(target - target_value))

    return fitness_score

# Función para crear un nuevo individuo con mutaciones y teniendo en cuenta el atributo "shiny"
def create_new_individual(parent, mutation_rate):
    new_individual = list(parent)

    for i in range(3):
        if random.random() < mutation_rate:
            new_individual[i] = random.randint(1, target_value)  # Usar target_value como el nuevo valor máximo

    # Actualizar el atributo "shiny" según las probabilidades
    if random.random() < 0.05:
        new_individual[3] += 1

    return new_individual

# Parámetros del algoritmo genético
population_size = 20
generations = 100

# Pedir al usuario que seleccione el atributo y el valor objetivo
target_attribute = input("Ingrese el atributo a buscar (1.vida, 2.daño, 3.velocidad): ").lower()
if target_attribute == "1":
    target_attribute = "vida"
elif target_attribute == "2":
    target_attribute = "danio"
else:
    target_attribute = "velocidad"

target_value = int(input(f"Ingrese el valor objetivo para '{target_attribute}': "))

# Inicialización de la población inicial
population = []
for _ in range(population_size):
    vida = random.randint(1, target_value)  # Usar target_value como el nuevo valor máximo
    danio = random.randint(1, target_value)
    velocidad = random.randint(1, target_value)
    shiny = 0
    if random.random() < 0.05:
        shiny = 1

    individual = [vida, danio, velocidad, shiny]
    population.append(individual)

# Ciclo principal del algoritmo genético
found = False
last_generation = None
for generation in range(generations):
    fitness_scores = [evaluate_individual(individual, target_attribute, target_value) for individual in population]

    num_selected = population_size // 2
    selected_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i], reverse=True)[:num_selected]
    selected_population = [population[i] for i in selected_indices]

    new_population = list(selected_population)
    while len(new_population) < population_size:
        parent = random.choice(selected_population)
        new_individual = create_new_individual(parent, mutation_rate=0.1)
        new_population.append(new_individual)

    population = new_population

    best_individual = max(population, key=lambda individual: evaluate_individual(individual, target_attribute, target_value))
    best_fitness = evaluate_individual(best_individual, target_attribute, target_value)

    if best_fitness >= 1.0:
        found = True
        last_generation = generation + 1
        break

# Encontrar el índice del atributo objetivo en la lista de atributos
target_index = ["vida", "danio", "velocidad"].index(target_attribute)

# Encontrar el individuo con el valor más alto en el atributo seleccionado
best_individual = max(population, key=lambda individual: individual[target_index])

# Ordenar la población por aptitud (en orden descendente)
sorted_population = sorted(population, key=lambda individual: evaluate_individual(individual, target_attribute, target_value), reverse=True)

if found:
    print(f"Generación en la que se encontró al individuo - {last_generation}.")
else:
    print("El individuo no fue encontrado en las generaciones especificadas.")

# Mostrar el mejor, segundo y tercer mejor individuo
print("Podio de los individuos:")
print(f"Mejor individuo - {target_attribute}: {best_individual[target_index]}")
for i, individual in enumerate(sorted_population[:3]):
    print(f"{i + 1}.")
    print(f"Atributos - Vida: {individual[0]}, Daño: {individual[1]}, Velocidad: {individual[2]}, Shiny: {individual[3]}")
    print("-" * 30)