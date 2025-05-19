import tkinter
from Views.datosView import actualizarTabla
from Views.entradaView import entrada_view  # Asegúrate de que esté bien importado

def formulario_view(ventana):
       
    tablas_panel = tkinter.Frame(ventana, bg="White", width=600, height=600)
    tablas_panel.grid(row=1, column=0, sticky="nsew")

    formulario_panel = tkinter.Frame(ventana, bg="White", width=400, height=600)
    formulario_panel.grid(row=1, column=1, sticky="nsew")

    entrada_view(formulario_panel, tablas_panel, actualizarTabla)

    actualizarTabla("SELECT * FROM general", tablas_panel)

    return formulario_panel
