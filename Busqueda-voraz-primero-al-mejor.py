import networkx as nx
import matplotlib.pyplot as plt

def greedy_path(graph, start, end):
    """
    Encuentra la ruta más corta desde el nodo de inicio hasta el nodo de destino
    utilizando el algoritmo de búsqueda voraz.
    """
    path = [start]
    while path[-1] != end:
        neighbors = graph.neighbors(path[-1])
        distances = {neighbor: graph[path[-1]][neighbor]['weight'] for neighbor in neighbors}
        closest_neighbor = min(distances, key=distances.get)
        path.append(closest_neighbor)
    return path

# Crear un grafo de ejemplo
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=8)
G.add_edge('C', 'E', weight=10)
G.add_edge('D', 'E', weight=2)

# Obtener la ruta más corta utilizando el algoritmo de búsqueda voraz
start_node = 'A'
end_node = 'E'
path = greedy_path(G, start_node, end_node)
print("Ruta más corta:", path)

# Mostrar el grafo y la ruta más corta utilizando la biblioteca NetworkX
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], edge_color='r', width=2)
plt.axis('off')
plt.show()
