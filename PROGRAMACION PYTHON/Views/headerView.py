import tkinter
from tkinter import font
from PIL import Image,ImageTk

def header_view(ventana):

    header_panel = tkinter.Frame(ventana, bg="#aeeff0",width="1000",height="100")
    header_panel.grid(row=0,column=0,columnspan=2,sticky="nsew")

  #--------------------------------------------------------------------------------

    imagen = Image.open(r"C:\Users\josea\OneDrive\Desktop\PROGRAMACION PYTHON\HMiku.jpg")
    imagen = imagen.resize((120, 120))
    logo = ImageTk.PhotoImage(imagen)

    label_logo = tkinter.Label(header_panel, image=logo, bg="white",bd=2,relief="solid", highlightthickness=4, highlightbackground="#00d2ff")
    label_logo.image = logo
    label_logo.pack(side="left", padx=20, pady=10)

  #--------------------------------------------------------------------------------
    custom_font = font.Font(family="Comic Sans MS", size="26", weight="bold")

    custom_font2 = font.Font(family="Comic Sans MS", size="20", weight="bold")
  #--------------------------------------------------------------------------------

    posicionX = 165
    posicionY = 80

    titulo = tkinter.Label(header_panel,
                           text="🚗 Panel de Control de Vehículos 🛠️",
                           font=custom_font,
                           fg="#222",
                           bg="#e0ffff",
                           bd=2,
                           relief="solid",
                           highlightthickness=4,
                           highlightbackground="#00d2ff")
    
    titulo.place(x = posicionX, y = posicionY)

    titulo_adicional = tkinter.Label(header_panel,
                                     text="Buscador de datos marca DineroMiau",
                                     font=custom_font2,
                                     fg="#333",
                                     bg="#aeeff0")
    
    titulo_adicional.place(x = posicionX, y = posicionY - 45)

    return header_panel