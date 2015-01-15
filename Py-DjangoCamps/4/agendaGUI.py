# -*- coding:utf-8 -*-
from Tkinter import *
import modulos

def escribe():
    lista.insert(END,"Hola")

def listar():
    agenda = open("agendatelefonica.csv")
    numero = 0
    for i in range(1,30):
        lectura = agenda.readline()
##        print(lectura.replace(",","\t\t"))
        lista.insert(END,lectura.replace(",","   "))
        numero = numero + 1
    agenda.close()



f = Frame(height=300,width=300)
f.pack(padx=15,pady=15)

logoimg = PhotoImage(file="josevicentecarratala.gif")
etiquetalogo = Label(f,image = logoimg)
etiquetalogo.pack(side=TOP,padx=10,pady=10)

titulo = Label(f,text="Agenda Telefonica",fg="blue",font=("Arial",24))
titulo.pack(side=TOP,padx=10,pady=10)

autor = Label(f,text="Jose Vicente Carratala")
autor.pack(side=TOP,padx=10,pady=10)

campo = Entry(f,textvariable = 5)
campo.pack(side=TOP,padx=10,pady=10)

##boton1 = Button(f,text="Listar elementos de la agenda",command=lambda:modulos.listar(int(Entry.get(campo))))
boton1 = Button(f,text="Listar elementos de la agenda",command=listar)
boton1.pack(side=BOTTOM,padx=10,pady=10)

lista = Listbox(f)
lista.pack(side=TOP,padx=10,pady=10)




