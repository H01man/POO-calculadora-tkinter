import tkinter
from tkinter import ttk
from tkinter import Label
import tkinter as tk

class calculadora():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry('500x250')

        self.numero1 = tk.StringVar()
        self.numero2 = tk.StringVar()
        self.res = tk.StringVar()

        self.label1 = tk.Label(self.ventana, text = 'Numero 1')
        self.label1.pack()
        self.input1 = tk.Entry(self.ventana,textvariable = self.numero1)
        self.input1.pack()
        self.label2 = tk.Label(self.ventana, text = 'Numero 2')
        self.label2.pack()
        self.input2 = tk.Entry(self.ventana, textvariable = self.numero2)
        self.input2.pack()

        boton1 = tk.Button(self.ventana, text = 'Suma', command= self.suma)
        boton1.pack()
        boton2 = tk.Button(self.ventana, text = 'Resta', command = self.resta)
        boton2.pack()
        boton3 = tk.Button(self.ventana, text = 'Multiplicacion', command = self.multi)
        boton3.pack()
        boton4 = tk.Button(self.ventana, text = 'Division', command = self.div)
        boton4.pack()
        self.ventana.mainloop()

    def suma(self):
        self.suma = int(self.numero1.get()) + int(self.numero2.get())
        print('Suma: ',self.suma)

    def resta(self):
        self.resta = int(self.numero1.get()) - int(self.numero2.get())
        print('Resta: ',self.resta)

    def multi(self):
        self.multi = int(self.numero1.get()) * int(self.numero2.get())
        print('Multiplicacion: ', self.multi)

    def div(self):
        self.div = int(self.numero1.get()) / int(self.numero2.get())
        print('Division: ',self.div)

calc = calculadora()
