import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import contextily as ctx

from datos_ciudades import ciudades
from dijkstra import dijkstra, distancia


# ================= MAPA =================
def dibujar_mapa(ruta=None):
    ax.clear()

    # Dibujar ciudades
    for dep, (ciudad, lat, lon) in ciudades.items():
        ax.scatter(lon, lat, color='blue', s=40)
        ax.text(lon, lat, ciudad, fontsize=8)

    # Dibujar ruta óptima
    if ruta:
        for i in range(len(ruta) - 1):
            lat1, lon1 = ciudades[ruta[i]][1], ciudades[ruta[i]][2]
            lat2, lon2 = ciudades[ruta[i + 1]][1], ciudades[ruta[i + 1]][2]

            ax.plot([lon1, lon2], [lat1, lat2],
                    color='red', linewidth=3)

    # 🔥 AJUSTE CLAVE (MAPA VERTICAL REAL)
    ax.set_xlim(-82, -68)
    ax.set_ylim(-20, 0)
    ax.set_aspect('equal')

    # 🔥 MAPA REAL (tipo Google Maps)
    ctx.add_basemap(ax, crs="EPSG:4326")

    ax.set_title("Ruta Óptima - Perú", fontsize=14)
    ax.set_axis_off()

    canvas.draw()


# ================= BOTÓN =================
def calcular():
    origen = combo_origen.get()
    destino = combo_destino.get()

    if origen not in ciudades or destino not in ciudades:
        panel_resultado.config(text="Seleccione ciudades válidas")
        return

    ruta, total = dijkstra(origen, destino)

    texto = "Ruta óptima:\n\n"

    for i in range(len(ruta) - 1):
        d = distancia(ruta[i], ruta[i + 1])
        texto += f"{ruta[i]} → {ruta[i+1]} ({d:.0f} km)\n"

    texto += f"\nDistancia total:\n{total:.0f} km"

    panel_resultado.config(text=texto)

    dibujar_mapa(ruta)


# ================= INTERFAZ =================
ventana = tk.Tk()
ventana.title("Ruta Óptima - Perú (Dijkstra)")
ventana.geometry("1100x650")
ventana.configure(bg="#f8f9fa")

# TOP BAR
frame_top = tk.Frame(ventana, bg="#f8f9fa")
frame_top.pack(pady=10)

combo_origen = ttk.Combobox(frame_top, values=list(ciudades.keys()), width=18)
combo_origen.set("Origen")
combo_origen.pack(side="left", padx=10)

combo_destino = ttk.Combobox(frame_top, values=list(ciudades.keys()), width=18)
combo_destino.set("Destino")
combo_destino.pack(side="left", padx=10)

btn = tk.Button(frame_top, text="Encontrar camino",
                bg="#0d6efd", fg="white",
                font=("Segoe UI", 10, "bold"),
                padx=15, pady=5,
                command=calcular)
btn.pack(side="left", padx=10)

# MAPA
fig, ax = plt.subplots(figsize=(7, 6))
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack(side="left", fill="both", expand=True)

# PANEL DERECHO
panel_resultado = tk.Label(
    ventana,
    text="Seleccione origen y destino",
    bg="white",
    bd=2,
    relief="solid",
    justify="left",
    width=35,
    font=("Segoe UI", 10)
)
panel_resultado.pack(side="right", padx=10, pady=10, fill="y")

# MAPA INICIAL
dibujar_mapa()

ventana.mainloop()