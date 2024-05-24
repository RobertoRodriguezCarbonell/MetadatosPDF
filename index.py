import tkinter as tk
from tkinter import filedialog, ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
import PyPDF2
import os
import csv

colores = {
    'azul': '#5797EA',
    'blanco': '#ffffff',
    'rojo': '#FF3939'
}

def extraer_metadatos(pdf_path):
    f = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(f)
    metadata = {
        "Author": pdf_reader.metadata.get('/Author'),
        "Company": pdf_reader.metadata.get('/Company'),
        "Created": pdf_reader.metadata.get('/CreationDate'),
        "Creator": pdf_reader.metadata.get('/Creator'),
        "LastSaved": pdf_reader.metadata.get('/ModDate'),
        "Producer": pdf_reader.metadata.get('/Producer'),
        "Title": pdf_reader.metadata.get('/Title'),
        "FileSize": os.path.getsize(pdf_path),
        "NumPages": len(pdf_reader.pages)
    }
    return pdf_reader, metadata

def exportar_csv():
    # Obtén los datos de la tabla
    datos = [tabla_metadatos.item(i)['values'] for i in tabla_metadatos.get_children()]

    # Pregunta al usuario dónde guardar el archivo CSV
    archivo_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    # Si el usuario no seleccionó un archivo (por ejemplo, si canceló la operación), sal de la función
    if not archivo_path:
        return

    # Escribe los datos en el archivo CSV
    with open(archivo_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Clave", "Valor"])  # Escribe los encabezados de las columnas
        writer.writerows(datos)  # Escribe los datos

def mostrar_metadatos(pdf_path):
    pdf_reader, metadata = extraer_metadatos(pdf_path)
    
    # Borra las filas anteriores
    for i in tabla_metadatos.get_children():
        tabla_metadatos.delete(i)

    # Inserta los metadatos en la tabla
    for clave, valor in metadata.items():
        tabla_metadatos.insert('', 'end', values=(clave, valor))

def drop(event):
    archivo_path = event.data
    # Eliminar las llaves alrededor del nombre del archivo
    archivo_path = archivo_path.strip('{}')
    mostrar_metadatos(archivo_path)

def seleccionar_archivo():
    archivo_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if archivo_path:
        mostrar_metadatos(archivo_path)

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
                    fieldbackground="#D3D3D3")

    style.map('Treeview', 
              background=[('selected', 'blue')])

    tabla = ttk.Treeview(marco, columns=("Clave", "Valor"), show='headings', style="Treeview")
    tabla.heading("Clave", text="Clave")
    tabla.heading("Valor", text="Valor")
    tabla.pack(pady=10, fill=tk.BOTH, expand=True)
    tabla.drop_target_register(DND_FILES)
    tabla.dnd_bind('<<Drop>>', drop)
    return tabla

def limpiar_tabla():
    for i in tabla_metadatos.get_children():
        tabla_metadatos.delete(i)

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

button_clear = crear_boton(marco_izquierdo, 'azul', 'Limpiar')
button_clear['command'] = limpiar_tabla
button_clear.pack(pady=10)

button1 = crear_boton(marco_derecho, 'azul', 'CSV')
button1['command'] = exportar_csv
button2 = crear_boton(marco_derecho, 'rojo', 'PDF')

button1.grid(row=0, column=0, padx=(10, 0), pady=20)
button2.grid(row=0, column=1, padx=(10, 0), pady=20)

root.mainloop()