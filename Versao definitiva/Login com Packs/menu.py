from tkinter import *
from tkinter import messagebox
from string import ascii_letters
import subprocess
import os

class Menu:
    def __init__(self, master=None):

        self.fontePadrao = ("Times New Roman", "20")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 30
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 80
        self.segundoContainer["pady"] = 15
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 80
        self.terceiroContainer["pady"] = 15
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 50
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 50
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text = "Menu", font = ("Times New Roman", "40", "bold"))
        self.titulo.pack()

        self.subtitulo = Label(self.segundoContainer, text = "Escolha um jogo:", font = self.fontePadrao)
        self.subtitulo.pack()

        #Jogo Acertando o Alvo
        def abrirAlvo():
            subprocess.run(["python", caminho_acertando_o_alvo])

        self.acertando_o_alvo = Button(self.terceiroContainer, text = "Acertando o Alvo", font = self.fontePadrao, command = abrirAlvo)
        self.acertando_o_alvo["width"] = 20
        self.acertando_o_alvo["bg"] = "grey"
        self.acertando_o_alvo.pack()

        #Jogo Desenhando Gráfico
        def desGrafico():
            subprocess.run(["python", caminho_desenhando_grafico])

        self.desenhando_grafico = Button(self.quartoContainer, text = "Desenhando Gráfico", font = self.fontePadrao, command = desGrafico)
        self.desenhando_grafico["width"] = 20
        self.desenhando_grafico["bg"] = "grey"
        self.desenhando_grafico.pack()



#Diretorio
caminho_atual = os.path.abspath(__file__)
diretorio_atual = os.path.dirname(caminho_atual)

caminho_acertando_o_alvo = os.path.join(diretorio_atual, "acertando_alvo.py")
caminho_desenhando_grafico = os.path.join(diretorio_atual, "desenho_grafico.py")

root = Tk()
Menu(root)
root.title("Painel do Usuário")
root.geometry("800x600+300+50")

root.mainloop()