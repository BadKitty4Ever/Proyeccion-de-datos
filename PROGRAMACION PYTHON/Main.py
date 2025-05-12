import tkinter
from Views.headerView import header_view
from Views.formView import formulario_view


#-------------------------------------------------------------------------------

ventana = tkinter.Tk()
ventana.title("✨ Registro Vehicular ✨")
ventana.geometry("1200x700")

ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=6)
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=4)

#--------------------------------------------------------------------------------

header_view(ventana)
formulario_view(ventana)

ventana.mainloop()