import tkinter
from tkinter import font
from PIL import Image,ImageTk

def header_view(ventana):

    header_panel = tkinter.Frame(ventana, bg="Green",width="1000",height="100")
    header_panel.grid(row=0,column=0,columnspan=2,sticky="nsew")

    imagen = Image.open(r"C:\Users\josea\OneDrive\Desktop\PROGRAMACION PYTHON\Money.jpeg")
    imagen = imagen.resize((100, 100))
    logo = ImageTk.PhotoImage(imagen)

    label_logo = tkinter.Label(header_panel, image=logo, bg="white")
    label_logo.image = logo
    label_logo.pack(side="left", padx=20, pady=10)

    custom_font = font.Font(family="Helvetica", size="24", weight="bold")
    label_titulo = tkinter.Label(header_panel, text="Informe, Base de Datos",font=custom_font,bg="lightgreen",fg="black")
    label_titulo.pack(side="left",padx=20,pady=25)

    return header_panel