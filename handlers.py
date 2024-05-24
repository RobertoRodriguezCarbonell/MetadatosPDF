from file_operations import extraer_metadatos
from tkinter import filedialog
from tkinterdnd2 import DND_FILES

# Variable global para tabla_metadatos
tabla_metadatos = None

def configurar_handlers(tabla):
    global tabla_metadatos
    tabla_metadatos = tabla
    tabla_metadatos.drop_target_register(DND_FILES)
    tabla_metadatos.dnd_bind('<<Drop>>', drop)

def drop(event):
    print(f"Archivo arrastrado: {event.data}")
    archivo_path = event.data
    # Eliminar las llaves alrededor del nombre del archivo
    archivo_path = archivo_path.strip('{}')
    mostrar_metadatos(archivo_path)

def seleccionar_archivo():
    archivo_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if archivo_path:
        mostrar_metadatos(archivo_path)

def limpiar_tabla():
    for i in tabla_metadatos.get_children():
        tabla_metadatos.delete(i)

def mostrar_metadatos(pdf_path):
    print(f"Mostrando metadatos para: {pdf_path}")
    pdf_reader, metadata = extraer_metadatos(pdf_path)
    print(f"Metadatos extraídos: {metadata}")
    
    # Borra las filas anteriores
    for i in tabla_metadatos.get_children():
        tabla_metadatos.delete(i)

    # Inserta los metadatos en la tabla
    for clave, valor in metadata.items():
        tabla_metadatos.insert('', 'end', values=(clave, valor))
        print(f"Insertando en la tabla: {clave} - {valor}")
