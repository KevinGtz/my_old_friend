#! /usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
from tkFileDialog import asksaveasfilename,askopenfilename


#Comienza el class del editor
class PyNotePad:
    # Esta es La funsión inicial
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Notas de la escuela")

        # "inicia" el scroolbar
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=RIGHT, fill=Y)

        menubar = Menu(self.root)
        #Aquí indicamos los menus
        MENUArchivo = Menu(menubar)
        MENUArchivo.add_command(label="Guardar", command=self.Guardar)
        MENUArchivo.add_command(label="Abrir", command=self.Abrir)
        menubar.add_cascade(label="Archivo", menu=MENUArchivo)

        MENUAyuda = Menu(menubar)
        MENUAyuda.add_command(label="Sobre", command=self.sobre)
        menubar.add_cascade(label="Ayuda", menu=MENUAyuda)
        self.root.config(menu=menubar)

        # aqui añadimos la parte que del texto:
        self.text = Text(self.root)
        self.text.pack(expand=YES, fill=BOTH)

        #aqui configuramos el scrolbar
        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)


        # Y aquí por fin la ventana
        self.root.mainloop()

    def Guardar(self): #esto es una funcion para guardar el archivo

        fileName = asksaveasfilename()
        try:
            file = open(fileName, 'w')
            textoutput = self.text.get(0.0, END)
            file.write(textoutput)
        except:
            pass
        finally:
            file.close()

    def Abrir(self):#Funcion para abrir un archivo
      

        fileName = askopenfilename()
        try:
            file = open(fileName, 'r')
            contents = file.read()

            self.text.delete(0.0, END)
            self.text.insert(0.0, contents)
        except:
            pass

    def sobre(self):
        root = Tk()
        root.wm_title("Sobre")
        texto=("Notas de la escuela: Version 1.0")
        textONlabel = Label(root, text=texto)
        textONlabel.pack()

# Iniciamos el programa
PyNotePad()
