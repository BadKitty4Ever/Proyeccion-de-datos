import tkinter
import tkinter.messagebox as messagebox

#--------------------------------------------------------------------------------

def entrada_view(formulario_panel, tablas_panel, actualizarTabla):
    # Entradas
    labels_texts = ["Ingrese el color:", "Ingrese el tiempo inicio (hora):", "Ingrese el tiempo fin (hora):", "Ingrese la placa:", "Ingrese el género:"]
    entries = {}

    for texto in labels_texts:
        lbl = tkinter.Label(formulario_panel, text=texto)
        lbl.pack(pady=5)
        ent = tkinter.Entry(formulario_panel, bd=1, relief="solid", highlightthickness=3, highlightbackground="#00d2ff")
        ent.pack(pady=5)
        entries[texto] = ent

#--------------------------------------------------------------------------------

    def boton_filtrar():
        color = entries["Ingrese el color:"].get().strip()
        tiempo_inicio = entries["Ingrese el tiempo inicio (hora):"].get().strip()
        tiempo_fin = entries["Ingrese el tiempo fin (hora):"].get().strip()
        placa = entries["Ingrese la placa:"].get().strip()
        genero = entries["Ingrese el género:"].get().strip()

 #--------------------------------------------------------------------------------

        condiciones = []

        if color:
            condiciones.append(f"color = '{color}'")

 #--------------------------------------------------------------------------------

        if tiempo_inicio and tiempo_fin:
            if not tiempo_inicio.isdigit() or not tiempo_fin.isdigit():
                messagebox.showerror("‼️Error", "Los valores de tiempo deben ser numéricos")
                return
            t1 = int(tiempo_inicio)
            t2 = int(tiempo_fin)
            if t1 > t2:
                messagebox.showerror("Ups", "El tiempo inicio no puede ser mayor que el tiempo fin")
                return
            tiempo1 = f"{t1:02d}:00"
            tiempo2 = f"{t2:02d}:00"
            condiciones.append(f"(hora_entrada BETWEEN '{tiempo1}' AND '{tiempo2}')")

        elif tiempo_inicio or tiempo_fin:
            messagebox.showerror("❌Error", "Ambos campos de tiempo deben estar llenos")
            return
        
 #--------------------------------------------------------------------------------

        if placa:
            condiciones.append(f"placa = '{placa}'")

 #--------------------------------------------------------------------------------

        if genero:
            condiciones.append(f"genero = '{genero}'")

 #--------------------------------------------------------------------------------

        consulta = "SELECT * FROM general"

        if condiciones:
            consulta += " WHERE " + " AND ".join(condiciones)

        print(f"Consulta SQL generada: {consulta}")

        actualizarTabla(consulta, tablas_panel)

 #--------------------------------------------------------------------------------

    boton = tkinter.Button(formulario_panel, text="Filtrar", command=boton_filtrar)
    boton.pack(pady=10)

 #--------------------------------------------------------------------------------
    
    def boton_nueva_ventana():
        ventana_nueva = tkinter.Toplevel(formulario_panel)
        ventana_nueva.title("Pari Pa Pa Pari Pari")
        ventana_nueva.geometry("500x500")

# P1 ----------------------------------------------------------
        inombre = tkinter.Label(ventana_nueva,text="Nombre:")
        inombre.pack(padx=10,pady=2)
        enombre = tkinter.Entry(ventana_nueva,width=20)
        enombre.pack(padx=10,pady=10)
# P2 ----------------------------------------------------------
        igenero = tkinter.Label(ventana_nueva,text="Genero:")
        igenero.pack(padx=10,pady=2)
        egenero = tkinter.Entry(ventana_nueva,width=20)
        egenero.pack(padx=10,pady=10)
# P3 ----------------------------------------------------------
        iplaca = tkinter.Label(ventana_nueva,text="Placa:")
        iplaca.pack(padx=10,pady=2)
        eplaca= tkinter.Entry(ventana_nueva,width=20)
        eplaca.pack(padx=10,pady=10)
# P4 ----------------------------------------------------------
        icolor = tkinter.Label(ventana_nueva,text="Color:")
        icolor.pack(padx=10,pady=2)
        ecolor = tkinter.Entry(ventana_nueva,width=20)
        ecolor.pack(padx=10,pady=10)
# P5 ----------------------------------------------------------
        imodelo = tkinter.Label(ventana_nueva,text="Modelo:")
        imodelo.pack(padx=10,pady=2)
        emodelo = tkinter.Entry(ventana_nueva,width=20)
        emodelo.pack(padx=10,pady=10)
# P6 ----------------------------------------------------------
        ihe = tkinter.Label(ventana_nueva,text="Hora Entrada:")
        ihe.pack(padx=10,pady=2)
        ehe = tkinter.Entry(ventana_nueva,width=20)
        ehe.pack(padx=10,pady=10)
# P7 ----------------------------------------------------------
        ihs = tkinter.Label(ventana_nueva,text="Hora Salida:")
        ihs.pack(padx=10,pady=2)
        ehs = tkinter.Entry(ventana_nueva,width=20)
        ehs.pack(padx=10,pady=10)
# P8 ----------------------------------------------------------
        itarifa = tkinter.Label(ventana_nueva,text="Tarifa:")
        itarifa.pack(padx=10,pady=2)
        etarifa = tkinter.Entry(ventana_nueva,width=20)
        etarifa.pack(padx=10,pady=10)
# P9 ----------------------------------------------------------
        icw = tkinter.Label(ventana_nueva,text="Car Wash:")
        icw.pack(padx=10,pady=2)
        ecw= tkinter.Entry(ventana_nueva,width=20)
        ecw.pack(padx=10,pady=10)

    return entries, boton