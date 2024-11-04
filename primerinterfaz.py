import tkinter as tk

ventana = tk.Tk ()
ventana.title("Mi primer interfaz gráfica")

etiqueta = tk.Label(ventana,text="Hola mundo")
etiqueta.pack(pady=5)

ventana.mainloop()

# label: imprime texto 
# Entry: es para ingresar datos o como un input
#ventana.geometry se le asigna a la ventana una geometria o un tamaño
#try: es donde se mte el codigo donde puede haber un error, except: es ya cuando da un error en el try se le pone lo que va a aparecer