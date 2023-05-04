# Importamos las librerías necesarias
import random
import numpy as np

# Definimos la matriz de distancia
distancias = np.array([    
    [0, 2, 5, 7],
    [2, 0, 6, 8],
    [5, 6, 0, 9],
    [7, 8, 9, 0]
])

# Definimos la función objetivo
def objetivo(solucion):
    distancia_total = 0
    for i in range(len(solucion)-1):
        distancia_total += distancias[solucion[i]][solucion[i+1]]
    distancia_total += distancias[solucion[-1]][solucion[0]]
    return distancia_total

# Definimos la función de vecindario
def vecindario(solucion):
    vecinos = []
    for i in range(len(solucion)):
        for j in range(i+1, len(solucion)):
            vecino = solucion.copy()
            vecino[i], vecino[j] = vecino[j], vecino[i]
            vecinos.append(vecino)
    return vecinos

# Definimos la búsqueda tabú
def busqueda_tabu(solucion_inicial, max_iter, tam_tabu):
    mejor_solucion = solucion_inicial.copy()
    mejor_valor = objetivo(mejor_solucion)
    solucion_actual = solucion_inicial.copy()
    valor_actual = objetivo(solucion_actual)
    tabu_list = []
    for i in range(max_iter):
        vecinos = vecindario(solucion_actual)
        vecinos = [vecino for vecino in vecinos if vecino not in tabu_list]
        if not vecinos:
            break
        vecinos_valores = [objetivo(vecino) for vecino in vecinos]
        indice_mejor_vecino = np.argmin(vecinos_valores)
        mejor_vecino = vecinos[indice_mejor_vecino]
        mejor_valor_vecino = vecinos_valores[indice_mejor_vecino]
        if mejor_valor_vecino < valor_actual:
            solucion_actual = mejor_vecino.copy()
            valor_actual = mejor_valor_vecino
            if mejor_valor_vecino < mejor_valor:
                mejor_solucion = mejor_vecino.copy()
                mejor_valor = mejor_valor_vecino
        tabu_list.append(mejor_vecino)
        if len(tabu_list) > tam_tabu:
            tabu_list.pop(0)
    return mejor_solucion, mejor_valor

# Ejecutamos la búsqueda tabú
solucion_inicial = [0, 1, 2, 3]
max_iter = 100
tam_tabu = 5
mejor_solucion, mejor_valor = busqueda_tabu(solucion_inicial, max_iter, tam_tabu)

# Mostramos el resultado
print("Mejor solución encontrada:", mejor_solucion)
print("Valor de la mejor solución encontrada:", mejor_valor)
