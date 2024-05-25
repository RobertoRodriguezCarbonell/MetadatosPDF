import PyPDF2
import os
import csv
from tkinter import filedialog

def extraer_metadatos(pdf_path):
    print(f"Extrayendo metadatos de: {pdf_path}")
    f = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(f)
    metadata = {
        "Author": pdf_reader.metadata.get('/Author', 'N/A'),
        "Company": pdf_reader.metadata.get('/Company', 'N/A'),
        "Created": pdf_reader.metadata.get('/CreationDate', 'N/A'),
        "Creator": pdf_reader.metadata.get('/Creator', 'N/A'),
        "LastSaved": pdf_reader.metadata.get('/ModDate', 'N/A'),
        "Producer": pdf_reader.metadata.get('/Producer', 'N/A'),
        "Title": pdf_reader.metadata.get('/Title', 'N/A'),
        "FileSize": os.path.getsize(pdf_path),
        "NumPages": len(pdf_reader.pages)
    }
    f.close()
    print(f"Metadatos encontrados: {metadata}")
    return pdf_reader, metadata

def exportar_csv(tabla_metadatos):
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

# exportar los datos como xlsx
def exportar_xlsx(tabla_metadatos):
    # Obtén los datos de la tabla
    datos = [tabla_metadatos.item(i)['values'] for i in tabla_metadatos.get_children()]

    # Pregunta al usuario dónde guardar el archivo CSV
    archivo_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("XLSX files", "*.xlsx")])

    # Si el usuario no seleccionó un archivo (por ejemplo, si canceló la operación), sal de la función
    if not archivo_path:
        return

    # Escribe los datos en el archivo CSV
    with open(archivo_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Clave", "Valor"])  # Escribe los encabezados de las columnas
        writer.writerows(datos)  # Escribe los datos