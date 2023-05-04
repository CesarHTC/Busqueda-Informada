import networkx as nx
import matplotlib.pyplot as plt
def camino_voraz(grafo, inicio, fin):
    """
    Encuentra la ruta más corta desde el nodo de inicio hasta el nodo de destino
    utilizando el algoritmo de búsqueda voraz.
    """
    if not grafo.has_node(inicio):
        raise ValueError(f"El nodo de inicio '{inicio}' no está en el grafo.")
    if not grafo.has_node(fin):
        raise ValueError(f"El nodo de destino '{fin}' no está en el grafo.")
    
    camino = [inicio]
    visitados = set(camino)
    while camino[-1] != fin:
        vecinos = grafo.neighbors(camino[-1])
        distancias = {vecino: grafo[camino[-1]][vecino]['weight'] for vecino in vecinos if vecino not in visitados}
        if not distancias:
            raise ValueError(f"No se puede llegar al nodo de destino '{fin}' desde el nodo de inicio '{inicio}'.")
        vecino_mas_cercano = min(distancias, key=distancias.get)
        visitados.add(vecino_mas_cercano)
        camino.append(vecino_mas_cercano)
    return camino


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
nodo_inicio = 'A'
nodo_fin = 'E'
camino = camino_voraz(G, nodo_inicio, nodo_fin)


# Mostrar el grafo y la ruta más corta utilizando la biblioteca Matplotlib
pos = nx.spring_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, font_size=8)
nx.draw_networkx(G, pos, node_size=500, with_labels=True, edge_color='r', edgelist=[(camino[i], camino[i+1]) for i in range(len(camino)-1)], width=2)
plt.axis('off')
plt.show()
