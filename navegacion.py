
# Aquí programaremos la lógica de movimiento tipo Pac-Man usando el Algoritmo A*

def calcular_distancia_manhattan(origen, destino):
    """
    Calcula cuántos pasos en horizontal y vertical separan al robot de la víctima.
    origen: Tupla (fila, columna) del Robot -> ej. (0, 0)
    destino: Tupla (fila, columna) de la Víctima -> ej. (0, 4)
    Fórmula: |x1 - x2| + |y1 - y2|
    """
    fila_robot, col_robot = origen
    fila_victima, col_victima = destino
    
    # Restamos las posiciones y usamos abs() para que el resultado siempre sea positivo
    distancia = abs(fila_robot - fila_victima) + abs(col_robot - col_victima)
    return distancia

def algoritmo_a_estrella(mapa, inicio, fin):
    """
    Aquí irá el algoritmo A* completo. 
    Por ahora, devolvemos una ruta simulada (una lista de pasos) 
    para que la interfaz pueda probar el movimiento.
    """
    # TODO: Implementar la lógica completa de A* esquivando muros (1)
    # Por el momento simulamos que el robot da 3 pasos a la derecha
    ruta_simulada = [(0,0), (0,1), (0,2), (0,3), (0,4)]
    return ruta_simulada
