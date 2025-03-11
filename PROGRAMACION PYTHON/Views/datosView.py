import tkinter
from Services.sql import conectar

def actualizarTabla(consulta_sql, panel):
    print("hola")
    consulta = conectar(consulta_sql)

    for cada_fila in consulta:
        for cada_columna in cada_fila:
         celda = tkinter.Label(panel, text=cada_columna, font=("Arial",12), fg="blue", bg="white")
         celda.pack()

