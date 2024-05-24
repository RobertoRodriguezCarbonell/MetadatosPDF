import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD
from ui_elements import crear_boton, crear_marco, crear_tabla
from file_operations import exportar_csv, exportar_xlsx
import handlers

def configurar_ventana_principal():
    root = TkinterDnD.Tk()
    root.title("Extractor de Metadatos PDF")
    root.geometry("700x400")
    root.resizable(False, False)
    return root

root = configurar_ventana_principal()

marco_izquierdo = crear_marco(root, tk.LEFT, ajustar_contenido=True)
marco_derecho = crear_marco(root, tk.RIGHT, color_fondo='SystemButtonFace')

tabla_metadatos = crear_tabla(marco_izquierdo)

# Configurar handlers con tabla_metadatos
handlers.configurar_handlers(tabla_metadatos)

button_clear = crear_boton(marco_izquierdo, 'azul', 'Limpiar')
button_clear['command'] = handlers.limpiar_tabla
button_clear.pack(pady=10)

imagen_csv = tk.PhotoImage(file="./images/buttons/csv.png")
imagen_pdf = tk.PhotoImage(file="./images/buttons/pdf.png")
imagen_xlsx = tk.PhotoImage(file="./images/buttons/xlsx.png")
imagen_txt = tk.PhotoImage(file="./images/buttons/txt.png")
imagen_json = tk.PhotoImage(file="./images/buttons/json.png")
imagen_xml = tk.PhotoImage(file="./images/buttons/xml.png")

button_imagen_csv = tk.Button(marco_derecho, image=imagen_csv, bd=0)
button_imagen_csv['command'] = lambda: exportar_csv(tabla_metadatos)
button_imagen_pdf = tk.Button(marco_derecho, image=imagen_pdf, bd=0)
button_imagen_xlsx = tk.Button(marco_derecho, image=imagen_xlsx, bd=0)
button_imagen_xlsx['command'] = lambda: exportar_xlsx(tabla_metadatos)
button_imagen_txt = tk.Button(marco_derecho, image=imagen_txt, bd=0)
button_imagen_json = tk.Button(marco_derecho, image=imagen_json, bd=0)
button_imagen_xml = tk.Button(marco_derecho, image=imagen_xml, bd=0)

button_imagen_csv.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))
button_imagen_pdf.grid(row=0, column=1, padx=(10, 0), pady=(10, 0))
button_imagen_xlsx.grid(row=1, column=0, padx=(10, 0), pady=(10, 0))
button_imagen_txt.grid(row=1, column=1, padx=(10, 0), pady=(10, 0))
button_imagen_json.grid(row=2, column=0, padx=(10, 0), pady=(10, 0))
button_imagen_xml.grid(row=2, column=1, padx=(10, 0), pady=(10, 0))

root.mainloop()
