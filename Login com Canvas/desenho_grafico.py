from tkinter import *
import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.containerInteracao = Frame(master)
        self.containerInteracao.pack(side=LEFT, anchor='n')
        self.containerInteracao.configure(background='#fdfdfd')

        self.ContainerR = Frame(self.containerInteracao)
        self.ContainerR["pady"] = 10
        self.ContainerR["padx"] = 5
        self.ContainerR.pack(side=TOP, anchor='w')
        self.ContainerR.configure(background='red')

        self.tituloR = Label(self.ContainerR, fg="white", text="Tamanho do Vermelho:")
        self.tituloR.configure(background='#fdfdfd', fg='red')
        self.tituloR["font"] = ("Arial", "10", "bold")
        self.tituloR.pack(anchor='c')
        self.tamR = Entry(self.ContainerR)
        self.tamR["width"] = 6
        self.tamR["font"] = self.fontePadrao
        self.tamR.insert(END, '10')
        self.tamR.configure(background='white', fg='#000000', font=("Arial", 11))
        self.tamR.pack(anchor='c')

        self.ContainerG = Frame(self.containerInteracao)
        self.ContainerG["pady"] = 10
        self.ContainerG["padx"] = 17
        self.ContainerG.pack(side=TOP, anchor='w')
        self.ContainerG.configure(background='green')

        self.tituloG = Label(self.ContainerG, fg="white", text="Tamanho do Verde:")
        self.tituloG.configure(background='#fdfdfd', fg='green')
        self.tituloG["font"] = ("Arial", "10", "bold")
        self.tituloG.pack(anchor='c')
        self.tamG = Entry(self.ContainerG)
        self.tamG["width"] = 6
        self.tamG["font"] = self.fontePadrao
        self.tamG.insert(END, '10')
        self.tamG.configure(background='white', fg='#000000', font=("Arial", 11))
        self.tamG.pack(anchor='c')

        self.ContainerB = Frame(self.containerInteracao)
        self.ContainerB["pady"] = 10
        self.ContainerB["padx"] = 20
        self.ContainerB.pack(side=TOP, anchor='w')
        self.ContainerB.configure(background='blue')

        self.tituloB = Label(self.ContainerB, fg="white", text="Tamanho do Azul:")
        self.tituloB.configure(background='#fdfdfd', fg='blue')
        self.tituloB["font"] = ("Arial", "10", "bold")
        self.tituloB.pack(anchor='c')
        self.tamB = Entry(self.ContainerB)
        self.tamB["width"] = 6
        self.tamB["font"] = self.fontePadrao
        self.tamB.insert(END, '10')
        self.tamB.configure(background='white', fg='#000000', font=("Arial", 11))
        self.tamB.pack(anchor='c')

        self.ContainerO = Frame(self.containerInteracao)
        self.ContainerO["pady"] = 10
        self.ContainerO["padx"] = 12
        self.ContainerO.pack(side=TOP, anchor='w')
        self.ContainerO.configure(background='Orange')

        self.tituloO = Label(self.ContainerO, fg="white", text="Tamanho do Laranja:")
        self.tituloO.configure(background='#fdfdfd', fg='orange')
        self.tituloO["font"] = ("Arial", "10", "bold")
        self.tituloO.pack(anchor='c')
        self.tamO = Entry(self.ContainerO)
        self.tamO["width"] = 6
        self.tamO["font"] = self.fontePadrao
        self.tamO["text"] = '10'
        self.tamO.insert(END, '10')
        self.tamO.configure(background='white', fg='#000000', font=("Arial", 11))
        self.tamO.pack(anchor='c')

        self.primeiroContainer = Frame(self.containerInteracao)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer["padx"] = 5
        self.primeiroContainer.pack()
        self.primeiroContainer.configure(background='#fdfdfd')

        self.btInserir = Button(self.primeiroContainer)
        self.btInserir["text"] = "Inserir"
        self.btInserir["font"] = ("Calibri", "12")
        self.btInserir["width"] = 12
        self.btInserir["command"] = self.acaoInserir
        self.btInserir.configure(background='#e0e0e0', fg='#000000')
        self.btInserir.pack(side=BOTTOM)

        self.acaoInserir()

        # criar_circulo(50, 50, 'g', myCanvas, "green")
        # criar_retangulo(100, 200, 'p', myCanvas, "yellow")
        # criar_circulo(150, 50, 'g', myCanvas, "black")

        # criar_retangulo(250, 200, 'g', myCanvas, "green")

    def acaoInserir(self):
        myCanvas.create_rectangle(0, 0, 1600, 1000, outline='#f1f1f1', fill='#f1f1f1')

        myCanvas.create_rectangle(0, 270, 10 * 150, 274, outline='grey', fill='grey')
        for i in range(0, 2000, 100):
            myCanvas.create_rectangle(i, 00, i, 274, outline='grey', fill='grey')
            myCanvas.create_rectangle(i - 1, 260, i + 2, 274, outline='grey', fill='grey')

        tamR = int(self.tamR.get())
        myCanvas.create_rectangle(0, 0, 10 * tamR, 64, outline='red', fill='red')
        tamG = int(self.tamG.get())
        myCanvas.create_rectangle(0, 64, 10 * tamG, 128, outline='green', fill='green')
        tamB = int(self.tamB.get())
        myCanvas.create_rectangle(0, 128, 10 * tamB, 192, outline='blue', fill='blue')
        tamO = int(self.tamO.get())
        myCanvas.create_rectangle(0, 192, 10 * tamO, 255, outline='Orange', fill='Orange')


def converteCor(corPt):
    dicionario = {'Azul': 'blue', 'Verde': 'green', 'Cinza': 'grey', 'Vermelho': 'red', 'Amarelo': 'yellow',
                  'Preto': 'black'}
    return dicionario[corPt]


def criar_circulo(x, y, tam, canvasName, color):  # center coordinates, radius
    if tam == 'p':
        r = 20
    else:
        r = 40

    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, outline=color, fill=color, width=3)


def criar_retangulo(x0, y0, tam, canvasName, color):  # center coordinates, radius
    if tam == 'p':
        l = 30
    else:
        l = 60
    xf = 2 * l + x0
    yf = y0 + l

    return canvasName.create_rectangle(x0, y0, xf, yf, outline=color, fill=color)


def criar_quadrado(x0, y0, tam, canvasName, color):  # center coordinates, radius
    l = 5 * tam
    xf = l + x0
    yf = y0 + l

    return canvasName.create_rectangle(x0, y0, xf, yf, outline=color, fill=color)


root = Tk()
myCanvas = Canvas(root, width=1000, height=400)
myCanvas.configure(background='#f1f1f1')
myCanvas.pack(side=RIGHT)
root.title("Desenhando em Python - Prof. Tiago Falcão")
root.configure(background='#fdfdfd')
Application(root)
root.mainloop()
