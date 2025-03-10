import tkinter
from datosView import actualizarTabla

def formulario_view(ventana):

    formulario_panel = tkinter.Frame(ventana, bg="red",width="400",height="600")
    formulario_panel.grid(row=1,column=0,sticky="nsew")

    def funcion_boton():
        respuesta = entry.get()
        print(respuesta)

    tablas_panel = tkinter.Frame(ventana, bg="blue", width="600", height="600")
    tablas_panel.grid(row=1,column=1, sticky="nsew")
    actualizarTabla(f"SELECT {respuesta} FROM usuarios",tablas_panel)

    titulo = tkinter.Label(formulario_panel, text="Ingrese su texto:")
    titulo.pack(pady=5)

    entry = tkinter.Entry(formulario_panel)
    entry.pack(pady=5)

    buttom = tkinter.Button(formulario_panel, text="Enviar", command=funcion_boton)
    buttom.pack(pady=5)

    return formulario_panel

