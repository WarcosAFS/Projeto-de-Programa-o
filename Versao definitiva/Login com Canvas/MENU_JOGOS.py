from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sys
import subprocess
import os




class Menu:
    def __init__(self, master = None):

########     PADRAO DE FONTE PARA OS BOTÕES    ##########################
        self.fonte_botoes = ("Arial", "14")

        self.canvas = Canvas(master, width = 600, height = 650)
        self.canvas.pack()


#####    TITULO
        self.titulo_bg = self.canvas.create_rectangle(-2,35,652,85, fill = '#A67242')
        self.titulo = self.canvas.create_text(300, 40, text = 'LISTA DE JOGOS', font = ('Arial', '30', 'bold'), fill = 'black', anchor = 'n')


###########    DIRETORIO ATUAL    ############################

        self.caminho_atual = os.path.abspath(__file__)
        self.diretorio_atual = os.path.dirname(self.caminho_atual)


##########    CAMINHOS A SEREM UTILIZADOS    ############

        self.caminho_Login_Canvas = os.path.join(self.diretorio_atual, 'LOGIN_CANVAS.py')
        self.caminho_acertando_o_alvo = os.path.join(self.diretorio_atual, 'acertando_alvo.py')
        self.caminho_desenho_grafico = os.path.join(self.diretorio_atual, 'desenho_grafico.py')


#########     IMAGENS PARA PERSONALIZAÇÃO   ################

##### BACKGROUND
        self.caminho_imagem_background = os.path.join(self.diretorio_atual, 'menu_fundo.jpg')
        self.abrir_imagem_background = Image.open(self.caminho_imagem_background)
        self.imagem_background_resized = self.abrir_imagem_background.resize((602, 652))
        self.photo_bg = ImageTk.PhotoImage(self.imagem_background_resized)
        self.imagem_background = self.canvas.create_image(0,0, image = self.photo_bg, anchor = 'nw')

##### PLAQUINHA
        self.caminho_imagem_plaquinha = os.path.join(self.diretorio_atual, 'plaquinha.png')
        self.abrir_imagem_plaquinha = Image.open(self.caminho_imagem_plaquinha)
        self.imagem_plaquinha_resized = self.abrir_imagem_plaquinha.resize((200, 100))
        self.photo_plaquinha = ImageTk.PhotoImage(self.imagem_plaquinha_resized)


##########    BOTOES DE SELEÇÃO E A CHAMADA DO JOGO     ########

        def acertando_o_alvo():
            subprocess.run(['python', self.caminho_acertando_o_alvo])

        self.acertando_o_alvo_botao = Button(master, font = self.fonte_botoes, text = 'Acertando o alvo', command = acertando_o_alvo, width= 180, height = 80, bg = '#A67242')
        self.plaquinha_acertando_o_alvo = self.canvas.create_window(300,200, window = self.acertando_o_alvo_botao, width = 175, height = 75)
        self.imagem_plaquinha_acertando_o_alvo = self.canvas.create_image(300, 150, image = self.photo_plaquinha, anchor = 'n')


        def desenho_grafico():
            subprocess.run(['python', self.caminho_desenho_grafico])

        self.desenho_grafico_botao = Button(master, font = self.fonte_botoes, text = 'Desenhando grafico', command = desenho_grafico, width= 180, height = 80, bg = '#A67242')
        self.plaquinha_desenho_grafico = self.canvas.create_window(300,350, window = self.desenho_grafico_botao, width = 175, height = 75)
        self.imagem_plaquinha_desenho_grafico = self.canvas.create_image(300, 300, image = self.photo_plaquinha, anchor = 'n')


##########     BOTAO DE DESCONECTAR (VOLTAR PARA A TELA DE LOGIN)       #############

        def desconectar():
            messagebox.showinfo('Desconectado...', 'Você foi desconectado e será redirecionado à tela de autenticação.')
            subprocess.Popen(['python', self.caminho_Login_Canvas])
            sys.exit(0)

        self.desconectar_button = Button(master, font = self.fonte_botoes, text = 'Desconectar', command = desconectar, bg = '#A67242', width = 142, height = 62)
        self.desconectar_botao = self.canvas.create_window(450,580, window = self.desconectar_button, width = 142, height = 62, anchor = 'nw')




root = Tk()
menu = Menu(root)


root.title('Menu de Jogos')
root.geometry('600x650')
root.mainloop()