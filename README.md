# 🗺️ Dijkstra — Ruta Óptima en el Perú

Aplicación que encuentra y visualiza la ruta más corta entre departamentos del Perú usando el algoritmo de Dijkstra, con un mapa interactivo en tiempo real.

---

## ¿Qué hace?

Seleccionas un punto de partida y un destino, y el programa calcula el camino más eficiente entre capitales de departamento. Todo se muestra visualmente sobre un mapa real del Perú, con el recorrido resaltado en rojo.

- Selección de origen y destino por nombre de departamento
- Cálculo automático de la ruta más corta
- Visualización del recorrido sobre mapa real (estilo Google Maps)
- Detalle paso a paso con distancias entre cada punto
- Distancia total del trayecto al finalizar

---

## ¿Cómo funciona?

El mapa del Perú se representa como un **grafo**: cada departamento es un nodo, y las conexiones entre ellos son las rutas posibles, con sus distancias reales entre capitales como peso.

El algoritmo de Dijkstra evalúa todos los caminos posibles desde el origen y selecciona el de menor distancia acumulada hasta llegar al destino.

---

## Ejemplo de uso

```
Origen:  Puno  
Destino: Moquegua

Resultado:
Puno → Moquegua (XXX km)
Distancia total: XXX km
```

La ruta se dibuja automáticamente sobre el mapa al presionar **"Encontrar camino"**.

---

## Estructura del proyecto

```
dijkstra_ruta_optima/
│
├── main.py              # Interfaz gráfica y visualización del mapa
├── dijkstra.py          # Lógica del algoritmo de búsqueda
├── grafo.py             # Conexiones y pesos entre departamentos
└── datos_ciudades.py    # Coordenadas reales de cada capital
```

---

## Instalación

Instala las dependencias necesarias con:

```bash
pip install matplotlib contextily geopy
```

---

## Ejecución

```bash
python main.py
```

1. Selecciona el **departamento de origen**
2. Selecciona el **departamento de destino**
3. Presiona **"Encontrar camino"**

---

## Tecnologías usadas

| Herramienta | Uso |
|---|---|
| `matplotlib` | Visualización gráfica e interfaz |
| `contextily` | Carga del mapa real de fondo |
| `geopy` | Coordenadas geográficas reales |
| `Python` | Lenguaje principal del proyecto |

---

## Consideraciones

- El grafo fue construido con conexiones entre departamentos vecinos geográficamente
- Si dos departamentos no tienen conexión definida, el algoritmo no considerará esa ruta
- El mapa está en orientación vertical para respetar la forma real del Perú
- La visualización es completamente local, sin necesidad de navegador

---

## Posibles mejoras a futuro

- [ ] Mostrar todas las conexiones del grafo, no solo la ruta activa
- [ ] Animación del recorrido paso a paso
- [ ] Zoom y desplazamiento del mapa
- [ ] Colorear los departamentos según su posición en la ruta
- [ ] Integrar datos GIS reales para los límites departamentales

---

## Sobre el proyecto

Desarrollado como proyecto académico para el curso de Programación Competitiva, aplicando el algoritmos de DIJKSTRA y teoría de grafos a un caso real con datos geográficos del Perú.
