import tkinter
from tkinter import ttk
from Services.sql import conectar

#______________________Actualizar_Tabla____________________________

def actualizarTabla(consulta_sql, panel):
    datos = conectar(consulta_sql)

    for widget in panel.winfo_children():
        widget.destroy()

    columnas = ("ID","Genero","Nombre","Placa","Color","Modelo","Hora Entrada","Hora Salida","Tarifa","Carwash")
    crear_tabla(panel, columnas, datos)

#__________________Crear_Tabla_____________________________________

def crear_tabla(panel, columnas, datos):
    tabla = ttk.Treeview(panel, columns=columnas, show="headings")

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor=tkinter.CENTER)

    tabla.pack(padx=10, pady=10)  # ¡Esto va SIEMPRE!

    if not datos:
        print("⚠️ No se encontraron datos o hubo un error en la consulta.")

        label = tkinter.Label(panel, text="No se encontraron datos.", fg="red", bg="white", font=("Arial", 12))
        label.pack(pady=5)
        return

    for fila in datos:
        tabla.insert("", tkinter.END, values=fila)

    return tabla
