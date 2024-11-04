import tkinter as tk
from tkinter import messagebox
 
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        mult = num1 * num2
        messagebox.showinfo("Resultado", f"El producto es: {mult}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        div = num1 / num2
        messagebox.showinfo("Resultado", f"La division es: {div}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
 
 
ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("300x200")
 
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)
 
label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)
 
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=20)

boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack(pady=20)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack(pady=20)

boton_division = tk.Button(ventana, text="Dividir", command=dividir)
boton_division.pack(pady=20)

ventana.mainloop()



# label: imprime texto 
# Entry: es para ingresar datos o como un input
#ventana.geometry se le asigna a la ventana una geometria o un tamaño
#try: es donde se mte el codigo donde puede haber un error, except: es ya cuando da un error en el try se le pone lo que va a aparecer