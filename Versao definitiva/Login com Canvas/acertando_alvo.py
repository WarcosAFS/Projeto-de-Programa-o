from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import random
import sys
import os
import subprocess

class Application:
    def __init__(self, master=None):
        
        self.fontePadrao = ("Arial", "10")
        self.containerInteracao = Frame(master)
        self.containerInteracao.pack(side=LEFT,anchor='n')
        self.containerInteracao.configure(background='#fdfdfd')
        
       
        
        self.primeiroContainer = Frame(self.containerInteracao)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer["padx"] = 5
        self.primeiroContainer.pack()
        self.primeiroContainer.configure(background='#fdfdfd')
                
        self.segundoContainer = Frame(self.containerInteracao)
        self.segundoContainer["pady"] = 20
        self.segundoContainer["padx"] = 5
        self.segundoContainer.pack()
        self.segundoContainer.configure(background='#fdfdfd')
                
        self.msgLabel = Label(self.primeiroContainer,text="Tente acertar a bola no alvo ;)\n\n", font=self.fontePadrao)
        self.msgLabel.configure(background='#fdfdfd',fg='black')
        self.msgLabel["font"] = ("Arial", "12", "bold")
        self.msgLabel.pack(side=TOP,anchor= 'w')
        
        self.btCima = Button(self.primeiroContainer)
        self.btCima["text"] = "Cima"
        self.btCima["font"] = ("Calibri", "12")
        self.btCima["width"] = 8
        self.btCima["command"] = self.acaoCima
        self.btCima.configure(background='#e0e0e0',fg='#000000')
        self.btCima.pack(side = TOP)
        
        self.btBaixo = Button(self.primeiroContainer)
        self.btBaixo["text"] = "Baixo"
        self.btBaixo["font"] = ("Calibri", "12")
        self.btBaixo["width"] = 8
        self.btBaixo["command"] = self.acaoBaixo
        self.btBaixo.configure(background='#e0e0e0',fg='#000000')
        self.btBaixo.pack(side = BOTTOM)
        
        self.btDir = Button(self.primeiroContainer)        
        self.btDir["text"] = "Direita"
        self.btDir["font"] = ("Calibri", "12")
        self.btDir["width"] = 8
        self.btDir["command"] = self.acaoDir
        self.btDir.configure(background='#e0e0e0',fg='#000000')
        self.btDir.pack(side =RIGHT)
        
        self.btEsq = Button(self.primeiroContainer)        
        self.btEsq["text"] = "Esquerda"
        self.btEsq["font"] = ("Calibri", "12")
        self.btEsq["width"] = 8
        self.btEsq["command"] = self.acaoEsq
        self.btEsq.configure(background='#e0e0e0',fg='#000000')
        self.btEsq.pack(side = LEFT)

        self.x = random.randint(1,8) * 50
        self.y = random.randint(1,15) * 50
        self.concluiuDesafio = False
        
        self.temObstaculo = True
        
        self.criar_circulo(self.x, self.y, 'g', myCanvas, "black")
        self.textoVitoria = "Parabéns! Você venceu =D"
        self.venceuLabel = Label(self.segundoContainer,text="", font=self.fontePadrao)
        self.venceuLabel.configure(background='#fdfdfd',fg='green')
        self.venceuLabel["font"] = ("Arial", "12", "bold")
        self.venceuLabel.pack(side=BOTTOM,anchor= 'w')
        
        myCanvas.create_oval(950, 450, 1050, 550, outline='#00ff00' ,width=5)
        obstaculoy0 = random.randint(0,10) * 50
        self.obstaculoy = (obstaculoy0,obstaculoy0+random.randint(6,12) * 50)
        
        if self.obstaculoy[1]-self.obstaculoy[0] > 950:
            self.obstaculoy[0] = 100
        if self.temObstaculo:
            myCanvas.create_rectangle(800, self.obstaculoy[0], 850, self.obstaculoy[1], outline='red', fill='red')
        #criar_retangulo(100, 200, 'p', myCanvas, "yellow")
        #criar_circulo(150, 50, 'g', myCanvas, "black")

        #criar_retangulo(250, 200, 'g', myCanvas, "green")

        
    def acaoCima(self):
        self.criar_circulo(self.x, self.y, 'g', myCanvas, '#f1f1f1')
        
        self.y -= 50
        if self.y <= 0:
            self.y = 50
        self.criar_circulo(self.x, self.y, 'g', myCanvas, 'black')
        

    def acaoBaixo(self):
        self.criar_circulo(self.x, self.y, 'g', myCanvas, '#f1f1f1')
        
        self.y += 50
        self.criar_circulo(self.x, self.y, 'g', myCanvas, 'black')
        
    def acaoDir(self):
        self.criar_circulo(self.x, self.y, 'g', myCanvas, '#f1f1f1')
        
        self.x += 50
        self.criar_circulo(self.x, self.y, 'g', myCanvas, 'black')
        
    def acaoEsq(self):
        self.criar_circulo(self.x, self.y, 'g', myCanvas, '#f1f1f1')
        
        self.x -= 50
        if self.x <= 0:
            self.x = 50
        self.criar_circulo(self.x, self.y, 'g', myCanvas, 'black')
        
            
            
    def criar_circulo(self, x, y, tam, canvasName,color): #center coordinates, radius
        if self.concluiuDesafio:
            return

            
        
        if tam =='p':
            r = 20
        else:
            r = 40
        
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        if color == 'black':
            print(x0,y0)
            

        def restart():
             python = sys.executable
             arquivo = caminho_acertando_o_alvo
             subprocess.call([python, arquivo])
             sys.exit(0)



        if self.temObstaculo and x0 > 750 and x0 <820 and y0 > self.obstaculoy[0]-50 and y0 < self.obstaculoy[1]-30:
            self.concluiuDesafio = True
            color = 'grey'
            resposta = messagebox.askyesno("DERROTA", "Você perdeu o desafio!\nDeseja tentar novamente?")
            if resposta:
                restart()
            else:
                sys.exit(0)

        if x0== 960 and y0==460:
            color = 'green'
            self.concluiuDesafio = True
            resposta = messagebox.askyesno("VITÓRIA", "Você venceu o desafio!\n Deseja tentar novamente?")
            if resposta:
                restart()
            else:
                sys.exit(0)
            

        canvasName.create_oval(x0, y0, x1, y1, outline=color, fill=color,width=3)
        canvasName.create_oval(950, 450, 1050, 550, outline='#00ff00' ,width=5)







def tecladoB(event):
    print('baixo pelo teclado')
    #print(event)
    Application.acaoBaixo(app)
    
def tecladoC(event):
    print('cima pelo teclado')
    #print(event)
    Application.acaoCima(app)

def tecladoE(event):
    print('esq pelo teclado')
    #print(event)
    Application.acaoEsq(app)
    

def tecladoD(event):
    print('dir pelo teclado')
    #print(event)
    Application.acaoDir(app)
        

root = Tk()

caminho_atual = os.path.abspath(__file__)
diretorio_atual = os.path.dirname(caminho_atual)
caminho_acertando_o_alvo = os.path.join(diretorio_atual, "acertando_alvo.py")


myCanvas = Canvas(root, width=1600, height=1000)
myCanvas.configure(background='#f1f1f1')
myCanvas.pack(side = RIGHT)
root.title("Acerte o Alvo - Prof. Tiago Falcão")
root.configure(background='#fdfdfd')
app = Application(root)
root.bind('<Down>', tecladoB) # configurando para mover o circulo quando pressionar as setas do teclado
root.bind('<Up>', tecladoC)
root.bind('<Left>', tecladoE)
root.bind('<Right>', tecladoD)
root.mainloop()