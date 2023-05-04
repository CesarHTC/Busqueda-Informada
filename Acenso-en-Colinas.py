import networkx as nx
import matplotlib.pyplot as plt
"""
El algoritmo comienza seleccionando un nodo aleatorio como nodo actual. Luego itera hasta 
que no haya vecinos con una evaluación mejor. En cada iteración, encuentra todos los vecinos 
del nodo actual, evalúa los vecinos y selecciona el vecino con la mejor evaluación (en este caso,
el vecino con el mayor número de conexiones). Si el mejor vecino tiene una evaluación mejor 
que el nodo actual, lo selecciona y repite el proceso. Si no, se detiene y sale del ciclo while.
Al final, se imprime el nodo con el mayor número de conexiones y se dibuja el grafo con el 
nodo seleccionado en rojo"""
# Creamos un grafo aleatorio con 10 nodos
G = nx.gnm_random_graph(15, 35)

# Definimos la función de evaluación como el número de conexiones de un nodo
def evaluate(node):
    return G.degree(node)

# Seleccionamos un nodo inicial aleatorio
current_node = list(G.nodes())[0]

# Iteramos hasta que no haya vecinos con una evaluación mejor
while True:
    # Encontramos todos los vecinos del nodo actual
    neighbors = list(G.neighbors(current_node))
    
    # Evaluamos los vecinos y encontramos el mejor
    best_neighbor = max(neighbors, key=evaluate)
    
    # Si el mejor vecino tiene una evaluación mejor que el nodo actual, lo seleccionamos
    if evaluate(best_neighbor) > evaluate(current_node):
        current_node = best_neighbor
    else:
        break

# Imprimimos el nodo con el mayor número de conexiones
print("El nodo con el mayor número de conexiones es:", current_node)
print("Número de conexiones:", evaluate(current_node))

# Dibujamos el grafo con el nodo seleccionado en rojo
node_colors = ["r" if node == current_node else "b" for node in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors)
plt.show()
