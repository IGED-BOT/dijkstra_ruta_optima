from geopy.distance import geodesic
import heapq
from datos_ciudades import ciudades
from grafo import grafo


def distancia(dep1, dep2):
    lat1, lon1 = ciudades[dep1][1], ciudades[dep1][2]
    lat2, lon2 = ciudades[dep2][1], ciudades[dep2][2]

    return geodesic((lat1, lon1), (lat2, lon2)).km


def dijkstra(inicio, fin):
    # Validación
    if inicio not in grafo or fin not in grafo:
        return [], 0

    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    pq = [(0, inicio)]
    padres = {}

    while pq:
        dist_actual, actual = heapq.heappop(pq)

        if actual == fin:
            break

        for vecino in grafo[actual]:
            if vecino not in distancias:
                continue  # evita errores

            peso = distancia(actual, vecino)
            nueva = dist_actual + peso

            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                padres[vecino] = actual
                heapq.heappush(pq, (nueva, vecino))

    # reconstrucción
    ruta = []
    nodo = fin

    while nodo in padres or nodo == inicio:
        ruta.insert(0, nodo)
        nodo = padres.get(nodo)
        if nodo is None:
            break

    return ruta, distancias.get(fin, float('inf'))