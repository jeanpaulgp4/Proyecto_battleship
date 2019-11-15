
from tkinter import*
ventana=Tk()
ventana.geometry('1000x500')
ventana.title("Battleship")
imagen= PhotoImage(file = "home.png")
fondo=Label(ventana,image=imagen).place(x=0,y=0)
ventana.resizable(0, 0)

def clicke():
    ventana_empezar()
def ventana_empezar():
    ventana.destroy()
    ventanae=Tk()
    ventanae.geometry('900x900')
    ventanae.title("Battleship\Empezar")
    imagen2= PhotoImage(file = "tridente5.png")
    fondo2=Label(ventanae,image=imagen2).place(x=0,y=0)
    ventanae.resizable(0, 0)
    ventanae.mainloop()
#
def clicki():
    ventana_i()
def ventana_i():
    ventana.destroy()
    ventanai=Tk()
    ventanai.geometry('500x500')
    ventanai.title("Battleship\Instrucciones")
    imagen3= PhotoImage(file = "tridente2.png")
    fondo3=Label(ventanai,image=imagen3).place(x=0,y=0)
    regresar=Button(ventanai,text="Regresar",bg='deep sky blue',command=clickr)
    regresar.place(x=10,y=10)
    regresar.config(font=("verdana",16))
    ins1=Label(ventanai,text="Bienvenido a las instrucciones")
    ins1.place(x=110,y=100)
    ins1.config(font=("verdana",14))
    ins2=Label(ventanai,text="Ubica los barcos en orden, recuerda es un barco de 2,3,4 y 5")
    ins2.place(x=70,y=140)
    ins2.config(font=("verdana",8))
    ins3=Label(ventanai,text="Solo elije una posicion de la a hasta la j, acompañado de un numero del 1 al 10")
    ins3.place(x=25,y=160)
    ins3.config(font=("verdana",8))
    ins4=Label(ventanai,text="Genera un disparo de la misma forma que al ubicar los barcos")
    ins4.place(x=70,y=180)
    ins4.config(font=("verdana",8))
    ins5=Label(ventanai,text="Dispara hasta derrumbar los barcos enemigos o que el enemigo te derribe a ti")
    ins5.place(x=25,y=200)
    ins5.config(font=("verdana",8))
    ventanai.resizable(0, 0)
    ventanai.mainloop()
#
def clickinfo():
    ventana.destroy()
    ventanainfo=Tk()
    ventanainfo.geometry('500x500')
    ventanainfo.title("Battleship\Instrucciones")
    imagen4= PhotoImage(file = "tridente2.png")
    fondo4=Label(ventanainfo,image=imagen4).place(x=0,y=0)
    regresar=Button(ventanainfo,text="Regresar",bg='deep sky blue',command=clickr)
    regresar.place(x=10,y=10)
    regresar.config(font=("verdana",16))
    ins1=Label(ventanainfo,text="Informacion del creador")
    ins1.place(x=110,y=100)
    ins1.config(font=("verdana",14))
    ins2=Label(ventanainfo,text="Jean Paul Gonzalez Pedraza")
    ins2.place(x=110,y=200)
    ins2.config(font=("verdana",12))
    ins3=Label(ventanainfo,text="Correo:Jeanzalez@gmail.com")
    ins3.place(x=110,y=240)
    ins3.config(font=("verdana",12))
    ventanainfo.resizable(0, 0)
    ventanainfo.mainloop()
#
def clickr():
    ventana()

#
empezar=Button(ventana,text="Empezar",bg='deep sky blue',command=clicke)
empezar.place(x=470,y=250)
empezar.config(font=("verdana",16))

#
mensaje=Label(ventana,text="Hola tripulante bienvenido a esta aventura!",bg='deep sky blue')
mensaje.place(x=250,y=100)
mensaje.config(font=("verdana",19))
#
instrucciones=Button(ventana,text="Instrucciones",bg='deep sky blue',command=clicki)
instrucciones.place(x=445,y=310)
instrucciones.config(font=("verdana",16))
#
info=Button(ventana,text="Info",bg='deep sky blue',command=clickinfo)
info.place(x=940,y=460)
info.config(font=("verdana",16))

ventana.mainloop()
