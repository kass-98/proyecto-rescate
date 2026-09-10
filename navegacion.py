
import heapq  # Herramienta para manejar prioridades matemáticas

def calcular_distancia_manhattan(origen, destino):
    """Calcula la distancia Manhattan: |x1 - x2| + |y1 - y2|"""
    fila_robot, col_robot = origen
    fila_victima, col_victima = destino
    return abs(fila_robot - fila_victima) + abs(col_robot - col_victima)

def algoritmo_a_estrella(mapa, inicio, fin):
    """
    Algoritmo A* Real. Encuentra la ruta más corta desde 'inicio' hasta 'fin'
    esquivando los muros (casillas con valor 1).
    """
    filas = len(mapa)
    columnas = len(mapa[0])
    
    # Estructura de prioridad: (costo_total, costo_actual, posicion_actual, camino_recorrido)
    # Empezamos con costo total = 0, costo actual = 0, en la posición inicial
    frontera = [(0, 0, inicio, [inicio])]
    visitados = set()  # Para recordar qué casillas ya exploramos y no repetir

    while frontera:
        # Sacamos la casilla con la menor puntuación estimada (la más óptima)
        _, costo_actual, actual, camino = heapq.heappop(frontera)

        # Si llegamos a la víctima, ¡éxito! Regresamos la ruta de pasos exacta
        if actual == fin:
            return camino

        if actual in visitados:
            continue
        visitados.add(actual)

        fila, col = actual

        # Movimientos posibles: Arriba, Abajo, Izquierda, Derecha
        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for df, dc in movimientos:
            nueva_f, nueva_c = fila + df, col + dc

            # Verificamos que el movimiento esté dentro del mapa y NO sea un muro (1)
            if 0 <= nueva_f < filas and 0 <= nueva_c < columnas:
                if mapa[nueva_f][nueva_c] != 1:  # Si no es muro
                    nuevo_vecino = (nueva_f, nueva_c)
                    if nuevo_vecino not in visitados:
                        nuevo_costo = costo_actual + 1
                        # Heurística: costo acumulado + distancia Manhattan que le falta
                        heuristica = calcular_distancia_manhattan(nuevo_vecino, fin)
                        costo_total = nuevo_costo + heuristica
                        
                        heapq.heappush(frontera, (costo_total, nuevo_costo, nuevo_vecino, camino + [nuevo_vecino]))
                        
    return [inicio]  # Si se encierra y no hay ruta, se queda quieto
