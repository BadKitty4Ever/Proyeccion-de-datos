import tkinter
from Views.headerView import header_view
from Views.formView import formulario_view
from PIL import Image, ImageTk, ImageSequence
from tkinter import Label
import pygame

pygame.mixer.init()
sonido_entrada = pygame.mixer.Sound(r"C:\Users\josea\OneDrive\Desktop\PROGRAMACION PYTHON\Hatsune Miku - SEGA (message sound).mp3")

#-------------------------------------------------------------------------------

ventana = tkinter.Tk()
ventana.title("✨ Registro Vehicular ✨")
ventana.geometry("1200x700")

ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=6)
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=6)

#--------------------------------------------------------------------------------

header_view(ventana)
formulario_view(ventana)
sonido_entrada.play()

#--------------------------------------------------------------------------------

nuevo_ancho = 250
nueva_altura = 250

gif = Image.open(r"C:\Users\josea\OneDrive\Desktop\PROGRAMACION PYTHON\download.gif")

# Redimensionar cada frame
frames = [
    ImageTk.PhotoImage(frame.copy().resize((nuevo_ancho, nueva_altura), Image.LANCZOS))
    for frame in ImageSequence.Iterator(gif)
]

gif_label = Label(ventana, bd=0, bg="white")
gif_label.place(relx=1.0, rely=1.0, anchor="se")

def animar(ind):
    frame = frames[ind]
    gif_label.configure(image=frame)
    ind = (ind + 1) % len(frames)
    ventana.after(25, animar, ind)

animar(0)
#--------------------------------------------------------------------------------

ventana.mainloop()