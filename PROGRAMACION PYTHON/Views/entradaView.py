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

    return entries, boton
