from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from string import ascii_letters
import subprocess
import os
import sys

class Login:
    def __init__(self, master=None):
        self.fonte = ("Arial", "30", "bold")
        self.fonte_entradas = ("Times New Roman", "30")

######### WIDGETS ##########################

        self.canvas = Canvas(master, width = 1000, height = 600)
        self.canvas.pack()

######## DIRETORIO ATUAL #####################
        self.caminho_atual = os.path.abspath(__file__)
        self.diretorio_atual = os.path.dirname(self.caminho_atual)

######### ADICIONAR IMAGEM DE FUNDO (BACKGROUND) ###############
        self.caminho_bg = os.path.join(self.diretorio_atual, 'background.jpg')
        self.image_bg = Image.open(self.caminho_bg)
        self.imagem_bg = self.image_bg.resize((1002,602))
        self.photo_bg = ImageTk.PhotoImage(self.imagem_bg)
        self.imagem = self.canvas.create_image(0, 0, image=self.photo_bg, anchor="nw")

        self.caminho_image_fire = os.path.join(self.diretorio_atual, 'imagem_fogo.jpg')
        self.image_fire = Image.open(self.caminho_image_fire)
        self.imagem_fogo = self.image_fire.resize((450,600))
        self.photo_fogo = ImageTk.PhotoImage(self.imagem_fogo)


########## ADICIONAR IMAGEM DO LOGO PYTHON #############

        self.caminho_logo = os.path.join(self.diretorio_atual, 'python_logo.png')
        self.image_logo = Image.open(self.caminho_logo)
        self.imagem_logo = self.image_logo.resize((185,100))
        self.photo_logo = ImageTk.PhotoImage(self.imagem_logo)
        self.imagem = self.canvas.create_image(0, 470, image=self.photo_logo, anchor="nw")

        self.titulo = self.canvas.create_text(210, 50, text="CONECTAR", font=("Calibri", "50", "bold"), fill="#F0E68C")

        self.nome_entry = Entry(master,font = self.fonte_entradas)
        self.senha_entry = Entry(master, font = self.fonte_entradas, show= '*')
        self.nome_entrada = self.canvas.create_window(0,0, window = self.nome_entry, width = 300)
        self.senha_entrada = self.canvas.create_window(0,0, window = self.senha_entry, width = 300)

        self.nome_rotulo = self.canvas.create_text(0,0, text = 'Nome:', fill = 'white', font = self.fonte)
        self.senha_rotulo = self.canvas.create_text(0,0, text = 'Senha:', fill = 'white', font = self.fonte)

        self.mensagem = self.canvas.create_text(0,0, text = '', font = ("Arial", "22"), fill = 'yellow', state = 'hidden', anchor = 'nw')

########   VALIDAÇÃO DE CREDENCIAIS ###########################
        self.caminho_menu = os.path.join(self.diretorio_atual, 'MENU_JOGOS.py')

        def verificar_usuario():
            Nome = self.nome_entry.get()
            Senha = self.senha_entry.get()

            if Nome not in Nomes:
                messagebox.showerror('Falha na autenticação', 'Estas credenciais não existem\nPor favor, cadastre-se')
            elif Senha not in Senhas[Nomes.index(Nome)]:
                messagebox.showerror('Senha inválida', 'A senha informada está incorreta')
            else:
                messagebox.showinfo('Sucesso na autenticação', 'Credenciais validadas com sucesso')
                subprocess.Popen(['python', self.caminho_menu])


        self.autenticar_button = Button(master, font = ("Arial", "20"), text = 'Autenticar', command = verificar_usuario)
        self.autenticar_botao = self.canvas.create_window(0,0, window = self.autenticar_button, width = 150)


###################  JANELA DE CADASTRO DO USUARIO ##############

        def cadastrar():
            janela_cadastro = Toplevel()
            janela_cadastro.title('Sign up')
            janela_cadastro.geometry('450x600')

            canvas = Canvas(janela_cadastro, width = 450, height = 600)
            canvas.pack()

            imagem_de_fundo = canvas.create_image(0,0, image = self.photo_fogo, anchor = 'nw')

            #cor_de_fundo = canvas.create_rectangle(0, 0, 450, 600, fill = '#181818')
            cor_painel = canvas.create_rectangle(50, 150, 400, 500, fill = 'black', width = 5, outline = 'blue')

            titulo = canvas.create_text(0,0, text = 'CADASTRAR', font = ("Calibri", "30", "bold"), fill = 'white', anchor = 'n')

            nome_entry = Entry(janela_cadastro, font = ("Arial", "20"))
            senha_entry = Entry(janela_cadastro, font = ("Arial", "20"), show = '*')
            confirmar_senha_entry = Entry(janela_cadastro, font = ("Arial", "20"), show = '*')
            nome_entrada = canvas.create_window(0,0, window = nome_entry, anchor = 'n', width = 200)
            senha_entrada = canvas.create_window(0,0, window = senha_entry, anchor = 'n', width = 200)
            confirmar_senha_entrada = canvas.create_window(0,0, window = confirmar_senha_entry, anchor = 'n', width = 200)

            nome_rotulo = canvas.create_text(0,0, text = 'Nome:', font = ("Arial", "20", "bold"), fill = 'white', anchor = 'n')
            senha_rotulo = canvas.create_text(0,0, text = 'Senha:', font = ("Arial", "20", "bold"), fill = 'white', anchor = 'n')
            confirmar_senha_rotulo = canvas.create_text(0,0, text = 'Confirmar\nsenha:', font = ("Arial", "15", "bold"), fill = 'white', anchor = 'n')


##############  FUNÇÃO MOSTRAR/OCULTAR SENHA NO CADASTRO  #######################

            senha_variable = IntVar()

            def ver_senha_cad():
                if senha_variable.get() == 0:
                    senha_entry['show'] = '*'
                    confirmar_senha_entry['show'] = '*'
                else:
                    senha_entry['show'] = ''
                    confirmar_senha_entry['show'] = ''


            senha_check = Checkbutton(janela_cadastro, variable = senha_variable, command = ver_senha_cad, bg = 'black')
            senha_ver = canvas.create_window(0,0, window = senha_check, width = 15, anchor = 'n')
            senha_ver_rotulo = canvas.create_text(0,0, text = 'Ver senha', font = ("Arial", "10"), fill = 'white', anchor = 'w')


############# ARMAZENAR DADOS DO USUARIO CADASTRANDO #################


            #Requisitos senha
            aviso = ''
            letras, letras_aviso = list(ascii_letters), 'Inclua ao menos UMA letra'

            numeros, numeros_aviso= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'Inclua ao menos UM número'

            caracteres_especiais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
            caracteres_especiais_aviso = 'Inclua ao menos UM caractere especial'

            confirmar_senha_aviso = 'As senhas devem ser iguais'

            mensagem = canvas.create_text(0,0, text = '', font = ("Arial", "12","bold"), fill = 'white', anchor = 'n')

            def cadastrar_usuario():
                cadastrar_nome = nome_entry.get()
                cadastrar_senha = senha_entry.get()
                cadastrar_confirmar_senha = confirmar_senha_entry.get()
                if not cadastrar_nome or not cadastrar_senha:
                    messagebox.showwarning('Campo vazio', 'Preencha todos os campos')
                elif cadastrar_nome in Nomes:
                    messagebox.showwarning('Nome já existe', 'Por favor, escolha outro nome')
                else:
                    aviso = ''
                    if not any(str(i) in cadastrar_senha for i in caracteres_especiais):
                        aviso += f'{caracteres_especiais_aviso}\n'
                        canvas.itemconfig(mensagem, text = aviso)

                    if not any(str(i) in cadastrar_senha for i in numeros):
                        aviso += f'{numeros_aviso}\n'
                        canvas.itemconfig(mensagem, text = aviso)

                    if not any(str(i) in cadastrar_senha for i in letras):
                        aviso += f'{letras_aviso}\n'
                        canvas.itemconfig(mensagem, text = aviso)

                    if cadastrar_confirmar_senha != cadastrar_senha:
                        aviso += f'{confirmar_senha_aviso}'
                        canvas.itemconfig(mensagem, text = aviso)

                    if cadastrar_confirmar_senha == cadastrar_senha and any(str(i) in cadastrar_senha for i in caracteres_especiais) and any(str(i) in cadastrar_senha for i in numeros) and any(str(i) in cadastrar_senha for i in letras):
                        canvas.itemconfig(mensagem, text = '')
                        Nomes.append(cadastrar_nome)
                        Senhas.append(cadastrar_senha)
                        messagebox.showinfo('Cadastro efetuado', 'Suas credenciais foram cadastradas\nVocê agora pode se conectar')

            cadastrar_button = Button(janela_cadastro, text = 'Cadastrar', font = ("Arial", "15"), command = cadastrar_usuario)
            cadastrar_botao = canvas.create_window(0,0, window = cadastrar_button, width = 100, anchor = 'w')



########   AJUSTE DE POSIÇÃO INDIVIDUAL DOS WIDGETS NO CADASTRO ##########

            canvas.coords(titulo, 225, 50)
            canvas.coords(nome_entrada, 280, 200)
            canvas.coords(senha_entrada, 280, 280)
            canvas.coords(confirmar_senha_entrada, 280, 360)
            canvas.coords(nome_rotulo, 115, 200)
            canvas.coords(senha_rotulo, 115, 280)
            canvas.coords(confirmar_senha_rotulo, 115, 360)
            canvas.coords(senha_ver, 230, 400)
            canvas.coords(senha_ver_rotulo, 240, 412)
            canvas.coords(cadastrar_botao, 180, 460)
            canvas.coords(mensagem, 220, 520)




        self.cadastrar_button = Button(master, font = ("Arial", "15"), text = 'Cadastrar', command = cadastrar)
        self.cadastrar_botao = self.canvas.create_window(0,0, window = self.cadastrar_button, width = 130)


########  FUNÇÃO MOSTRAR/OCULTAR SENHA NO LOGIN  #######################

        self.senha_variable = IntVar()

        def ver_senha():
            if self.senha_variable.get() == 0:
                self.senha_entry['show'] = '*'
            else:
                self.senha_entry['show'] = ''

        self.senha_check = Checkbutton(master, variable = self.senha_variable, command = ver_senha, bg = '#1A1243')
        self.senha_ver = self.canvas.create_window(0,0, window = self.senha_check, width = 15, anchor = 'w')
        self.senha_ver_rotulo = self.canvas.create_text(0,0, text = 'Ver senha', font = ("Arial", "10"), fill = 'white', anchor = 'w')



########   AJUSTE DE POSIÇÃO INDIVIDUAL DOS WIDGETS NO LOGIN ##########

        self.canvas.place(x=-2, y=-2)
        self.canvas.coords(self.titulo, 500, 100)
        self.canvas.coords(self.nome_entrada, 550, 250)
        self.canvas.coords(self.senha_entrada, 550, 350)
        self.canvas.coords(self.nome_rotulo,300, 250)
        self.canvas.coords(self.senha_rotulo,300, 350)
        self.canvas.coords(self.senha_ver, 500, 390)
        self.canvas.coords(self.senha_ver_rotulo, 520, 390)
        self.canvas.coords(self.autenticar_botao, 500, 480)
        self.canvas.coords(self.cadastrar_botao, 500, 550)
        self.canvas.coords(self.mensagem, 660, 460)


root = Tk()
login = Login(root)


######### DIRETÓRIO/CAMINHO ATUAL   #############

caminho_atual = os.path.abspath(__file__)
diretorio_atual = os.path.dirname(caminho_atual)

caminho_login_canvas = os.path.join(diretorio_atual, "LOGIN_CANVAS.py")


##########  ARMAZENAMENTO DE CREDENCIAIS ############

Nomes = ['adm']
Senhas = ['adm']



root.title("Sign in")
root.geometry("1000x600")
root.mainloop()