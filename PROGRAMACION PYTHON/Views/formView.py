import tkinter
from Views.datosView import actualizarTabla

def formulario_view(ventana):
    formulario_panel = tkinter.Frame(ventana, bg="White",width="400",height="600")
    formulario_panel.grid(row=1,column=0,sticky="nsew")

    tablas_panel = tkinter.Frame(ventana, bg="White", width="600", height="600")
    tablas_panel.grid(row=1,column=1, sticky="nsew")

 #_________________________________Color_____________________________________

    titulocolor = tkinter.Label(formulario_panel, text="Ingrese el color:")
    titulocolor.pack(pady=5)

    entrycolor = tkinter.Entry(formulario_panel)
    entrycolor.pack(pady=5)   

    def funcion_boton_color():
        respuesta = entrycolor.get()
        actualizarTabla(f"SELECT * FROM general WHERE color = '{respuesta}'",tablas_panel)
    
    buttomcolor = tkinter.Button(formulario_panel, text="En. Color", command=funcion_boton_color)
    buttomcolor.pack(pady=5)
 #__________________________________Tiempo___________________________________

    titulotiempo = tkinter.Label(formulario_panel, text="Ingrese el tiempo:")
    titulotiempo.pack(pady=5)

    entrytiempo = tkinter.Entry(formulario_panel)
    entrytiempo.pack(pady=5)

    def funcion_boton_tiempo():
        respuesta = entrycolor.get()
        actualizarTabla(f"SELECT * FROM general WHERE color = '{respuesta}'",tablas_panel)

    buttomtiempo = tkinter.Button(formulario_panel, text="En. Tiempo", command=funcion_boton_tiempo)
    buttomtiempo.pack(pady=5)
    
 #___________________________________________________________________________

    actualizarTabla(f"SELECT * FROM general",tablas_panel)

    return formulario_panel

