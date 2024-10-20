import os, tkinter as tk
os.system("cls")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("10 Botones Verticales")

# Inicializar el contador
contador = 0

# Usar un bucle while para crear 10 botones
while contador < 10:
    # Crear un botón y agregarlo a la ventana
    boton = tk.Button(ventana, text=f'Botón {contador + 1}')
    boton.pack(pady=5)  # Alinear verticalmente con espacio entre botones
    contador += 1  # Incrementar el contador

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()