from tkinter import *

print("EJERCICIO UTILIZANDO LA LIBRERIA TKINDER")
print("Autor: DAVID CHULDE")
 
v0 = Tk() # Tk() Es la ventana principal
v1=Toplevel(v0) # Crea una ventana hija
v1.protocol("WM_DELETE_WINDOW", "onexit") # Elimina la opción de salir para evitar el error
v0.resizable(0,0) # Evita que la ventana se pueda cambiar de tamaño
v1.resizable(0,0) # Evita que se le pueda cambiar de tamaño a la ventana
 
def mostrar(ventana): ventana.deiconify() # Muestra una ventana
def ocultar(ventana):ventana.withdraw() # Oculta una ventana
def ejecutar(f): v0.after(200,f) # Una forma de ejecutar las funciones
def imprimir(texto): print (texto) # Imprime un texto
 
v0.config(bg="black") # Le da color al fondo
v0.geometry("500x500") # Cambia el tamaño de la ventana
 
b1=Button(v0,text="ABRIR VENTANA V1",command=lambda: ejecutar(mostrar(v1)) or imprimir("hola") or imprimir("tercera función")) # Primer botón
b1.grid(row=1,column=1) # El botón es cargado
b2=Button(v1,text="OCULTARME",command=lambda: ejecutar(ocultar(v1))) # Segundo botón
b2.grid(row=1,column=2) # El botón es cargado
 
b3=Button(v0,text="OCULTAR VENTANA V1",command=lambda: ejecutar(ocultar(v1)))
b3.grid(row=1,column=2) # El botón es cargado
 
v1.withdraw() # Oculta la ventana v1
v0.mainloop() # Es el evento que llama al inicio de nuestro programa. Siempre lo lleva la ventana principal.


## OTRO EJEMPLO ###
 
def hija():
 
    ## Crea la ventana hija.
    t1 = Toplevel(root,bg="blue")
 
    ## Establece el tamaño para la ventana.
    t1.geometry('400x200+20+20')
 
    ## Provoca que la ventana tome el focus
    t1.focus_set()
 
    ## Deshabilita todas las otras ventanas hasta que
    ## esta ventana sea destruida.
    t1.grab_set()
 
    ## Indica que la ventana es de tipo transient, lo que significa
    ## que la ventana aparece al frente del padre.
    t1.transient(master=root)
 
    ## Crea un widget Label en la ventana
    Label(t1, text='Ventana hija',bg="blue").pack(padx=10, pady=10)
 
    ## Crea un widget que permite cerrar la ventana,
    ## para ello indica que el comando a ejecutar es el
    ## metodo destroy de la misma ventana.
    Button(t1,text="Cerrar",bg="green", command=t1.destroy).pack()
 
    ## Crea un entry.
    e=Entry(t1,bg="lightyellow")
 
    ## Establece el focus en el entry.
    e.focus()
    e.pack()
 
    ## Pausa el mainloop de la ventana de donde se hizo la invocación.
    t1.wait_window(t1)
 
## Crea la ventana para la aplicación
root = Tk()
 
## Establece un título y un tamaño para la ventana
root.title('Ventana principal')
root.geometry('800x400+10+10')
 
## Crea una etiqueta.
Label(root, text='Esta es la ventana principal').pack(pady=10)
 
## Crea un botón, desde el cual se puede lanzar una
## ventana de tipo modal.
Button(root,text="ventana", command=hija).pack()
 
root.mainloop()
