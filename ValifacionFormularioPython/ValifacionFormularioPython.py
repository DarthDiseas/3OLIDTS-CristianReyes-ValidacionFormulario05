import tkinter as tk
from tkinter import messagebox
import re

def guardar_datos():
    #Obtener los datos de los campos
    nombres = Entry_nombres.get()
    apellidos = Entry_apellidos.get()
    edad = Entry_edad.get()
    estatura = Entry_estatura.get()
    telefono = Entry_telefono.get()
    
    #Obtener el género selecionado
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
        
    #Validar que los campos estén correctos
    if (es_entero_valido(edad) and es_decimal_valido(estatura) and
        es_entero_valido_de_10_digitos(telefono) and es_texto_valido(nombres) and es_texto_valido(apellidos)):
        #Crear cadena de los datos
        datos = f"Nombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad}años\nEstatura: {estatura}cm\nTelefono: {telefono}\nGenero: {genero}"
        #guardar los datos en un archivo de texto
        with open("datos.txt", "a") as archivo:
            archivo.write(datos + "\n\n")
        
        messagebox.showinfo("Información guardada con éxito:\n\n" + datos)
        
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Por favor, ingrese datos válidos en los campos.")
        
def limpiar_campos():
    Entry_nombres.delete(0, tk.END)
    Entry_apellidos.delete(0, tk.END)
    Entry_edad.delete(0, tk.END)
    Entry_estatura.delete(0, tk.END)
    Entry_telefono.delete(0, tk.END)
    var_genero.set(0)
    
def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except  ValueError:
        return False
    
def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
    
def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def es_texto_valido(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))

    #Crear ventana
ventana = tk.Tk()
ventana.title("Formulario")

    #Crear variables para RadioButtons
var_genero= tk.IntVar()

    #Etiquetas y campos de entradas
label_nombres = tk.Label(ventana, text="Nombres:")
label_nombres.pack()
Entry_nombres = tk.Entry(ventana)
Entry_nombres.pack()
        
label_apellidos = tk.Label(ventana, text="Apellidos:")
label_apellidos.pack()
Entry_apellidos = tk.Entry(ventana)
Entry_apellidos.pack()

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack()
Entry_edad = tk.Entry(ventana)
Entry_edad.pack()

label_estatura = tk.Label(ventana, text="Estatura (cm):")
label_estatura.pack()
Entry_estatura = tk.Entry(ventana)
Entry_estatura.pack()

label_telefono = tk.Label(ventana, text="Teléfono:")
label_telefono.pack()
Entry_telefono = tk.Entry(ventana)
Entry_telefono.pack()

label_genero = tk.Label(ventana, text="Género:")
label_genero.pack()

rb_hombre = tk.Radiobutton(ventana, text="HOMBRE", variable=var_genero, value=1)
rb_hombre.pack()

rb_mujer = tk.Radiobutton(ventana, text="MUJER", variable=var_genero, value=2)
rb_mujer.pack()

btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
btn_guardar.pack()

btn_borrar = tk.Button(ventana, text="Borrar", command=limpiar_campos)
btn_borrar.pack()
    #INICIAR LA APLICACIÓN
ventana.mainloop()


#from ast import Delete
#from audioop import lin2adpcm
#from cProfile import label
#from distutils import archive_util
#import tkinter as tk
#from tkinter import Entry, messagebox
#import re
#from tokenize import Double
#from unittest.loader import VALID_MODULE_NAME
#from xml.dom.minidom import Entity