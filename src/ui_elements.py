import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES

colores = {
    'azul': '#5797EA',
    'blanco': '#ffffff',
    'rojo': '#FF3939',
    'verde': '#13D461',
    'gris': '#383838',
    'morado': '#680D9F',
    'rosa': '#FF507A'
}

def crear_boton(marco, color_fondo, texto):
    return tk.Button(
        marco,
        background=colores[color_fondo],
        foreground=colores['blanco'],
        highlightthickness=2,
        highlightbackground=colores['blanco'],
        highlightcolor='WHITE',
        bd=0,
        text=texto,
        width=12,
        font=('Arial', 12, 'bold'),
    )

def crear_marco(root, lado, expandir=True, ajustar_contenido=False, color_fondo=None):
    marco = tk.Frame(root, bg=color_fondo)
    marco.pack(side=lado, fill=tk.BOTH, expand=expandir)
    marco.pack_propagate(ajustar_contenido)
    return marco

def crear_tabla(marco):
    style = ttk.Style()
    style.configure("Treeview", 
                    background="#BBD9FF",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#ff507a")

    style.map('Treeview', 
              background=[('selected', '#3073ff')])

    tabla = ttk.Treeview(marco, columns=("Clave", "Valor"), show='headings', style="Treeview")
    tabla.heading("Clave", text="Clave")
    tabla.heading("Valor", text="Valor")
    tabla.pack(pady=10, fill=tk.BOTH, expand=True)
    return tabla
