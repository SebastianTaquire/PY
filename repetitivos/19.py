import os, tkinter as tk
os.system("cls")

ventana = tk.Tk()
ventana.title("10 Botones Verticales")

contador = 0

while contador < 10:
    boton = tk.Button(ventana, text=f'Botón {contador + 1}')
    boton.pack(pady=5) 
    contador += 1 

ventana.mainloop()