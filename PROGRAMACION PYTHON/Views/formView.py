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

    entrycolor = tkinter.Entry(formulario_panel,bd=1,relief="solid",highlightthickness=3,highlightbackground="lightgreen")
    entrycolor.pack(pady=5)   

    def funcion_boton_color():
        respuestacolor = entrycolor.get()
        actualizarTabla(f"SELECT * FROM general WHERE color = '{respuestacolor}'",tablas_panel)
    
    buttomcolor = tkinter.Button(formulario_panel, text="En. Color", command=funcion_boton_color)
    buttomcolor.pack(pady=5)
 #__________________________________Tiempo___________________________________

    titulotiempo = tkinter.Label(formulario_panel, text="Ingrese el tiempo:")
    titulotiempo.pack(pady=5)

    entrytiempo1 = tkinter.Entry(formulario_panel,bd=1,relief="solid",highlightthickness=3,highlightbackground="lightgreen")
    entrytiempo1.pack(pady=5)

    entrytiempo2 = tkinter.Entry(formulario_panel,bd=1,relief="solid",highlightthickness=3,highlightbackground="lightgreen")
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
      #OR hora_salida BETWEEN '{tiempo1}' AND '{tiempo2}'"
      
      print(f"Consulta SQL generada: {consulta}")

      actualizarTabla(consulta, tablas_panel)

    buttomtiempo = tkinter.Button(formulario_panel, text="En. Tiempo", command=funcion_boton_tiempo)
    buttomtiempo.pack(pady=5)

 #________________________________Placa_____________________________________

    tituloplaca = tkinter.Label(formulario_panel, text="Ingrese la Placa:")
    tituloplaca.pack(pady=5)

    entryplaca = tkinter.Entry(formulario_panel,bd=1,relief="solid",highlightthickness=3,highlightbackground="lightgreen")
    entryplaca.pack(pady=5)

    def funcio_boton_genero():
       respuestaplaca = entryplaca.get()
       actualizarTabla(f"SELECT * FROM general WHERE placa = '{respuestaplaca}'",tablas_panel)

    buttomplaca = tkinter.Button(formulario_panel, text="En. Placa", command=funcio_boton_genero)
    buttomplaca.pack(pady=5) 

 #_______________________________Genero______________________________________

    titulogenero = tkinter.Label(formulario_panel, text="Ingrese Genero:")
    titulogenero.pack(pady=5)

    entrygenero = tkinter.Entry(formulario_panel,bd=1,relief="solid",highlightthickness=3,highlightbackground="lightgreen")
    entrygenero.pack(pady=5)

    def fucion_boton_genero():
       respuestagenero = entrygenero.get()
       actualizarTabla(f"SELECT * FROM general WHERE genero = '{respuestagenero}'",tablas_panel)

    buttomgenero = tkinter.Button(formulario_panel,text="En. Genero",command=fucion_boton_genero)
    buttomgenero.pack(pady=5)      
 #___________________________________________________________________________

    actualizarTabla(f"SELECT * FROM general",tablas_panel)

    return formulario_panel