import math
import random
import matplotlib.pyplot as plt

# Función objetivo
def objective_function(x):
    return math.sin(x) * (1 / math.exp(abs(x)))

# Inicialización de la temperatura y otros parámetros
temperature = 100
cooling_rate = 0.03
x = random.uniform(-10, 10)
best_x = x
best_fitness = objective_function(x)

# Lista para almacenar los valores de x y fitness en cada iteración
x_values = []
fitness_values = []

# Algoritmo de Temple Simulado
while temperature > 1:
    # Generación de un vecino aleatorio
    new_x = random.uniform(-10, 10)
    # Cálculo del cambio de fitness
    delta_fitness = objective_function(new_x) - objective_function(x)
    # Evaluación del vecino
    if delta_fitness < 0:
        # Si el vecino es mejor, se acepta automáticamente
        x = new_x
    else:
        # Si el vecino es peor, se acepta con una probabilidad que depende de la temperatura
        if math.exp(-delta_fitness / temperature) > random.random():
            x = new_x
    # Actualización de la mejor solución encontrada
    if objective_function(x) < best_fitness:
        best_x = x
        best_fitness = objective_function(x)
    # Reducción de la temperatura
    temperature *= 1 - cooling_rate
    # Almacenamiento de los valores de x y fitness
    x_values.append(x)
    fitness_values.append(objective_function(x))

# Visualización gráfica de la búsqueda
plt.plot(x_values, fitness_values, 'b-')
plt.plot(best_x, best_fitness, 'r*', markersize=10)
plt.xlabel('x')
plt.ylabel('fitness')
plt.title('Temple Simulado')
plt.show()
