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

    formulario_insercion(panel)

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

#__________________Formulario_de_inserción______________________________

def formulario_insercion(panel):
    from tkinter import Label, Entry, Button, messagebox

    campos = ["Nombre", "Genero", "Placa", "Color", "Modelo", "Hora Entrada", "Hora Salida", "Tarifa", "Carwash"]
    entradas = {}

    contenedor_form = tkinter.Frame(panel, bg="white", bd=2, relief="groove")
    contenedor_form.pack(padx=10, pady=10, fill="x")

    tkinter.Label(contenedor_form, text="📥 Insertar Nuevo Vehículo", font=("Arial", 11, "bold"), bg="white").pack(pady=5)

    for campo in campos:
        lbl = Label(contenedor_form, text=campo + ":", bg="white")
        lbl.pack()
        ent = Entry(contenedor_form, width=30)
        ent.pack(pady=2)
        entradas[campo] = ent

    def insertar_datos():
        datos = [entradas[c].get().strip() for c in campos]

        if not all(datos):
            messagebox.showerror("⚠️ Error", "¡Todos los campos son obligatorios!")
            return

        sql = f"""
        INSERT INTO general
        (nombre, genero, placa, color, modelo, hora_entrada, hora_salida, tarifa, carwash)
        VALUES ('{datos[0]}', '{datos[1]}', '{datos[2]}', '{datos[3]}', '{datos[4]}',
                '{datos[5]}', '{datos[6]}', '{datos[7]}', '{datos[8]}');
        """

        try:
            conectar(sql)
            messagebox.showinfo("✅ Éxito", "Datos insertados correctamente")
            actualizarTabla("SELECT * FROM general", panel)
        except Exception as e:
            messagebox.showerror("💀 Error", str(e))

    btn_insertar = Button(contenedor_form, text="Insertar", command=insertar_datos, bg="#00e5ff")
    btn_insertar.pack(pady=10)