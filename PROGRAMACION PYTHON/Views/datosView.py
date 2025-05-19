import tkinter
from tkinter import ttk
from Services.sql import conectar

#__________________Estilo_de_la_tabla_________________________________

def estilo_tabla():
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("EstiloMiku.Treeview.Heading",
                    background="#00e5ff",
                    foreground="black",
                    font=("Arial", 10, "bold"),
                    relief="flat")
    
    style.configure("EstiloMiku.Treeview",
                    background="#ccf5ff",
                    foreground="black",
                    fieldbackground="#e0ffff",
                    borderwidth=2)
    
    style.map("EstiloMiku.Treeview",
              background=[("selected", "#00e5ff")],
              foreground=[("selected", "black")])

#______________________Actualizar_Tabla______________________________

def actualizarTabla(consulta_sql, panel):
    estilo_tabla()

    datos = conectar(consulta_sql)
    for widget in panel.winfo_children():
        widget.destroy()

    columnas = ("ID","Nombre","Genero","Placa","Color","Modelo","Hora Entrada","Hora Salida","Tarifa","Carwash")
    crear_tabla(panel, columnas, datos)

#__________________Crear_Tabla_____________________________________

def crear_tabla(panel, columnas, datos):
    tabla = ttk.Treeview(panel, columns=columnas, show="headings",style="EstiloMiku.Treeview")

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
