import tkinter
from tkinter import ttk
from Services.sql import conectar

#__________________________________________________________________--

def actualizarTabla(consulta_sql, panel):
    print("hola")
    consulta = conectar(consulta_sql)

    for widget in panel.winfo_children():
        widget.destroy()

    #Datos ejemplo
    columnas = ("ID","Genero","Nombre","Placa","Color","Modelo","Hora Entrada","Hora Salida","Tarifa","Carwash")
    crear_tabla(panel,columnas,consulta)

#__________________________________________________________________--

def crear_tabla(panel, columnas, datos):
    # Crear el Treeview
    tabla = ttk.Treeview(panel, columns=columnas, show="headings")
    
    # Configurar los encabezados
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor=tkinter.CENTER)
    
    # Insertar los datos
    for dato in datos:
        tabla.insert("", tkinter.END, values=dato)
    
    tabla.pack(padx=10, pady=10)
    return tabla