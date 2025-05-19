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
    crear_vista_vertical(panel, columnas, datos)

#__________________Crear_Vista_Vertical______________________________

def crear_vista_vertical(panel, columnas, datos):
    canvas = tkinter.Canvas(panel, bg="white")
    scrollbar = tkinter.Scrollbar(panel, orient="vertical", command=canvas.yview)
    frame_datos = tkinter.Frame(canvas, bg="white")

    frame_datos.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=frame_datos, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    if not datos:
        print("⚠️ No se encontraron datos o hubo un error en la consulta.")
        label = tkinter.Label(frame_datos, text="No se encontraron datos.", fg="red", bg="white", font=("Arial", 12))
        label.pack(pady=5)
        return

    for fila in datos:
        contenedor = tkinter.Frame(frame_datos, bg="#ccf5ff", bd=1, relief="solid")
        contenedor.pack(padx=10, pady=5, fill="x")

        for i, valor in enumerate(fila):
            etiqueta = tkinter.Label(contenedor, text=f"{columnas[i]}: {valor}", bg="#ccf5ff", anchor="w", font=("Arial", 10))
            etiqueta.pack(fill="x", padx=10, pady=2)

    return