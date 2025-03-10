import tkinter

def header_view(ventana):

    header_panel = tkinter.Frame(ventana, bg="green",width="1000",height="100")
    header_panel.grid(row=0,column=0,columnspan=2,sticky="nsew")

    return header_panel