import tkinter
from Views.datosView import actualizarTabla
import tkinter.messagebox as messagebox
from datetime import datetime

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

    entrytiempo1 = tkinter.Entry(formulario_panel)
    entrytiempo1.pack(pady=5)

    entrytiempo2 = tkinter.Entry(formulario_panel)
    entrytiempo2.pack(pady=5)

    def funcion_boton_tiempo():
      
      tiempo1 = entrytiempo1.get().strip() # Hora de Entrada
      tiempo2 = entrytiempo2.get().strip() # Hora de Salida

      if not tiempo1 or not tiempo2:
         messagebox.showerror("❌Error","Ambos campos deben de estar llenos")
         return

      if not tiempo1.isdigit() or not tiempo2.isdigit():
         messagebox.showerror("‼️Error","Los Valores deben de ser numericos")
         return
      
      tiempo1 = int(tiempo1)
      tiempo2 = int(tiempo2)

      if tiempo1 > tiempo2:
         messagebox.showerror("Ups", "El primer tiempo no debe de ser mayor que el segundo")
         return
      
      tiempo1 = f"{tiempo1:02d}:00"
      tiempo2 = f"{tiempo2:02d}:00"
      

      consulta = f"SELECT * FROM general WHERE hora_entrada BETWEEN '{tiempo1}' AND '{tiempo2}'"
      # OR hora_salida BETWEEN '{tiempo1}' AND '{tiempo2}' para calcular tambien hora de salida
      
      print(f"Consulta SQL generada: {consulta}")

      actualizarTabla(consulta, tablas_panel)

    buttomtiempo = tkinter.Button(formulario_panel, text="En. Tiempo", command=funcion_boton_tiempo)
    buttomtiempo.pack(pady=5)
    
 #___________________________________________________________________________

    actualizarTabla(f"SELECT * FROM general",tablas_panel)

    return formulario_panel



