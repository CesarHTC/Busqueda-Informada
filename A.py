# Librerias: matplotlib para graficar y numpy para herramientas para los arrays 
import matplotlib.pyplot as plt
import numpy as np
# Esta funcion utiliza la distancia de Manhattan como heurística, Devuelve un valor que indica la estimación de la distancia 
def heuristic(node, destino):
    return abs(node[0] - destino[0]) + abs(node[1] - destino[1])# la suma de las diferencias en valor absoluto 
                                                                #    entre las coordenadas x,y 

#Esta funcion crea una lista de los vecinos de un nodo node en una matriz de mapa.
def Vecinos(node, mapa):
    vecinos = []
    for horizontal, vertical in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        #x = filas y = columnas
        x, y = node[0] + horizontal, node[1] + vertical
        #Se verifica si las coordenadas x e y están dentro de los límites del mapa, 
        #que se obtienen de la longitud de las filas y columnas del mapa
        if 0 <= x < len(mapa) and 0 <= y < len(mapa[0]) and not mapa[x][y]: 
            #len(mapa) me da el nuemero de filas, len(mapa[0]) me da el numero de columnas
            # Si el valor de mapa[x][y] es False, significa que la celda está libre(ya que es 0) y 
            # se puede mover a través de ella por eso la negamos
            vecinos.append((x, y))
    return vecinos

def astar(inicio, destino, mapa):
    no_explorados = [inicio] #inicializo la lista con mi nodo de origen 
    explorados = []    #Nodos a los que el algoritmo ya visito 
    coste_acomulado = {inicio: 0}
    estimacion_coste = {inicio: heuristic(inicio, destino)} #estimacion del coste = coste acumulado + heuristica
    visitados = {}

    #Esta función implementa el algoritmo A* y recibe tres argumentos: el nodo de inicio (inicio), 
    # el nodo objetivo (goal) y una matriz booleana que indica qué celdas del mapa están 
    # bloqueadas por obstáculos (obstacles). Crea varias variables que se utilizarán en la 
    # búsqueda, incluyendo open_list y explorados, que son listas de nodos por explorar y ya 
    # explorados, respectivamente. También inicializa los diccionarios coste acumulado, estimacion del coste y visitados 
    # para almacenar información sobre los costos y caminos hacia cada nodo en el mapa

    while no_explorados:
        nodo_actual = min(no_explorados, key=lambda node: estimacion_coste[node])# min() devuelve el nodo en open_list con el valor 
        #mínimo del dicionarioestimacion del coste.
        if nodo_actual == destino:
            camino = []
            #LLeno la lista camino con los datos de la lista de visitados
            while nodo_actual in visitados:
                camino.append(nodo_actual)#agrego a la lista el nodo actual
                nodo_actual = visitados[nodo_actual]#actualice el nodo actual a su nodo anterior en el camino, que se encuentra en el diccionario de visitados.
            camino.append(inicio)#agreego el nodo de origen
            return camino[:]

        no_explorados.remove(nodo_actual)
        explorados.append(nodo_actual)

        for vecino in Vecinos(nodo_actual, mapa):
        

            if vecino in explorados:
                continue

            Coste_acumulado = coste_acomulado[nodo_actual] + 1
            if vecino not in no_explorados:
                no_explorados.append(vecino)
            elif Coste_acumulado >= coste_acomulado[vecino]:
                # Si el costo tentativo de llegar al vecino a través del nodo actual es mayor o igual
                # que el costo que se había calculado anteriormente para llegar al vecino, entonces 
                # se salta a la siguiente iteración del ciclo
                continue
                    
            visitados[vecino] = nodo_actual #El diccionario visitados se actualiza para registrar que el vecino fue alcanzado a través del nodo actual.
            coste_acomulado[vecino] = Coste_acumulado #El costo para alcanzar el vecino se actualiza con el costo tentativo calculado anteriormente. 
            estimacion_coste[vecino] = coste_acomulado[vecino] + heuristic(vecino, destino) #Finalmente, se actualiza el costo f_score para el vecino sumando el costo g_score y la heurística estimada para llegar al destino desde el vecino.

    return None



############################ Ejemplo de uso ############################################
# Los 0 son espacios libres y los 1 obstaculos

mapa = [     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],#Nodo Origen(0,0)
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],#1
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],#2
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],#3
             [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],#5 #Nodo meta (6,9)
             [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

inicio = (0, 0)
destino = (6, 9)
camino = astar(inicio, destino, mapa)
mapa = np.array(mapa)
plt.imshow(mapa, cmap='Blues' )
plt.grid(color='black', linewidth=0.5)

x, y = zip(*camino)
plt.plot(y,x, 'black')
plt.xticks(np.arange(0.5, 10, step=1),[])
plt.yticks(np.arange(0.5, 10, step=1),[])

plt.scatter(inicio[1], inicio[0], color='r')
plt.scatter(destino[1], destino[0], color='yellow')
plt.show()
