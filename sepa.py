import tkinter as tk
from tkinter import messagebox

ventana= tk.Tk()
ventana.title("Holaaa")
notebook=tk.Notebook(ventana)

pestaña1=tk.Frame(notebook)
pestaña2=tk.Frame(notebook)
pestaña3=tk.Frame(notebook)

notebook.add(pestaña1, text="Pestaña1")
notebook.add(pestaña2, text="Pestaña2")
notebook.add(pestaña3, text="Pestaña3")

notebook.pack(fill= "both", expand=True)

