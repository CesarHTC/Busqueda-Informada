def heuristic(node, destino):
    return abs(node[0] - destino[0]) + abs(node[1] - destino[1])# la suma de las diferencias en valor absoluto 
                                                                #    entre las coordenadas x,y 
# Esta funcion utiliza la distancia de Manhattan como heurística, Devuelve un valor que indica la estimación de la distancia 

def astar(inicio, destino, mapa):
    open_list = [inicio] #inicializo la lista con mi nodo de origen 
    closed_list = []    #Nodos a los que el algoritmo ya visito 
    g_score = {inicio: 0}
    f_score = {inicio: heuristic(inicio, destino)} #f_score = g_score + heuristic
    visitados = {}

    #Esta función implementa el algoritmo A* y recibe tres argumentos: el nodo de inicio (inicio), 
    # el nodo objetivo (goal) y una matriz booleana que indica qué celdas del mapa están 
    # bloqueadas por obstáculos (obstacles). Crea varias variables que se utilizarán en la 
    # búsqueda, incluyendo open_list y closed_list, que son listas de nodos por explorar y ya 
    # explorados, respectivamente. También inicializa los diccionarios g_score, f_score y cisitados 
    # para almacenar información sobre los costos y caminos hacia cada nodo en el mapa

    while open_list:
        nodo_actual = min(open_list, key=lambda node: f_score[node])# min() devuelve el nodo en open_list con el valor mínimo del dicionario f_score.
        if nodo_actual == destino:
            camino = []
            #LLeno la lista camino con los datos de la lista de visitados
            while nodo_actual in visitados:
                camino.append(nodo_actual)
                nodo_actual = visitados[nodo_actual]
            camino.append(inicio)
            return camino[::-1]

        open_list.remove(nodo_actual)
        closed_list.append(nodo_actual)

        for neighbor in get_neighbors(nodo_actual, mapa):
            if neighbor in closed_list:
                continue

            tentative_g_score = g_score[nodo_actual] + 1
            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g_score >= g_score[neighbor]:
                continue

            visitados[neighbor] = nodo_actual
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, destino)

    return None

def get_neighbors(node, mapa):
    neighbors = []
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x, y = node[0] + dx, node[1] + dy
        if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and not mapa[x][y]:
            neighbors.append((x, y))
    return neighbors

############################ Ejemplo de uso ############################################
# Los 0 son espacios libres y los 1 obstaculos

mapa = [     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#Nodo Origen(0,0)
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#1
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],#2
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],#3
             [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],#5 #Nodo meta (6,9)
             [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

inicio = (0, 0)
destino = (6, 9)
camino = astar(inicio, destino, mapa)

# Graficar el mapa y la ruta encontrada
import matplotlib.pyplot as plt
import numpy as np

mapa = np.array(mapa)
plt.imshow(mapa, cmap='binary')

x, y = zip(*camino)
plt.plot(y,x, 'r')
plt.scatter(inicio[1], inicio[0], color='g')
plt.scatter(destino[1], destino[0], color='b')
plt.show()
