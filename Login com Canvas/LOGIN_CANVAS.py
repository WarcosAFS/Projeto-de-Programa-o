import json
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from string import ascii_letters
import subprocess
import os
import sys


class Login:
    def __init__(self, master=None):

        ##### FONTES PADRAO
        self.fonte = ("Arial", "30", "bold")
        self.fonte_entradas = ("Times New Roman", "30")

        self.canvas = Canvas(master, width=1000, height=600)
        self.canvas.pack()

        ########      DIRETORIO ATUAL       #####################

        self.caminho_atual = os.path.abspath(__file__)
        self.diretorio_atual = os.path.dirname(self.caminho_atual)

        #########      ADICIONAR IMAGENS PARA PERSONALIZAÇÃO     ###############

        self.caminho_background = os.path.join(self.diretorio_atual, 'background.jpg')
        self.abrir_imagem_background = Image.open(self.caminho_background)
        self.imagem_background_resized = self.abrir_imagem_background.resize((1002, 602))
        self.photo_bg = ImageTk.PhotoImage(self.imagem_background_resized)
        self.imagem_background = self.canvas.create_image(0, 0, image=self.photo_bg, anchor="nw")

        self.caminho_image_fogo = os.path.join(self.diretorio_atual, 'imagem_fogo.jpg')
        self.abrir_imagem_fogo = Image.open(self.caminho_image_fogo)
        self.imagem_fogo_resized = self.abrir_imagem_fogo.resize((450, 600))
        self.photo_fogo = ImageTk.PhotoImage(self.imagem_fogo_resized)

        self.caminho_logo = os.path.join(self.diretorio_atual, 'python_logo.png')
        self.abrir_imagem_logo = Image.open(self.caminho_logo)
        self.imagem_logo_resized = self.abrir_imagem_logo.resize((185, 100))
        self.photo_logo = ImageTk.PhotoImage(self.imagem_logo_resized)
        self.imagem_logo = self.canvas.create_image(0, 470, image=self.photo_logo, anchor="nw")

        self.caminho_botao_autenticar = os.path.join(self.diretorio_atual, 'botao_autenticar.png')
        self.abrir_botao_autenticar = Image.open(self.caminho_botao_autenticar)
        self.botao_autenticar_resized = self.abrir_botao_autenticar.resize((210, 80))
        self.photo_botao_autenticar = ImageTk.PhotoImage(self.botao_autenticar_resized)

        self.caminho_botao_cadastrar = os.path.join(self.diretorio_atual, 'botao_cadastrar.png')
        self.abrir_botao_cadastrar = Image.open(self.caminho_botao_cadastrar)
        self.botao_cadastrar_resized = self.abrir_botao_cadastrar.resize((270, 90))
        self.photo_botao_cadastrar = ImageTk.PhotoImage(self.botao_cadastrar_resized)

        #### TITULO
        self.titulo = self.canvas.create_text(210, 50, text="CONECTAR", font=("Calibri", "50", "bold"), fill="#F0E68C")

        #### ENTRADAS DE AUTENTICAÇÃO
        self.nome_entry = Entry(master, font=self.fonte_entradas)
        self.senha_entry = Entry(master, font=self.fonte_entradas, show='*')
        self.nome_entrada = self.canvas.create_window(0, 0, window=self.nome_entry, width=300)
        self.senha_entrada = self.canvas.create_window(0, 0, window=self.senha_entry, width=300)

        self.nome_rotulo = self.canvas.create_text(0, 0, text='Nome:', fill='white', font=self.fonte)
        self.senha_rotulo = self.canvas.create_text(0, 0, text='Senha:', fill='white', font=self.fonte)

        #### MENSAGEM GERAL (CANTO INFERIOR)
        self.mensagem = self.canvas.create_text(0, 0, text='', font=("Arial", "22"), fill='yellow', state='hidden',
                                                anchor='nw')

        ########   VALIDAÇÃO DE CREDENCIAIS ###########################

        self.caminho_menu = os.path.join(self.diretorio_atual, 'MENU_JOGOS.py')

        def verificar_usuario():
            Nome = self.nome_entry.get()
            Senha = self.senha_entry.get()

            file = open(data_caminho)
            data = json.load(file)

            usuario_exists = False
            senha_correta = False
            for user in data['users']:
                if user['name'] == Nome:
                    usuario_exists = True
                    if user['password'] == Senha:
                        senha_correta = True

            if not Nome or not Senha:
                messagebox.showwarning('Campo vazio', 'Preencha todos os campos')
            elif not usuario_exists:
                messagebox.showerror('Falha na autenticação', 'Estas credenciais não existem\nPor favor, cadastre-se!')
            elif not senha_correta:
                messagebox.showerror('Senha inválida', 'A senha informada está incorreta')
            else:
                messagebox.showinfo('Sucesso na autenticação',
                                    f'Credenciais validadas com sucesso\nSeja bem-vindo {Nome}!')
                subprocess.Popen(['python', self.caminho_menu])
                sys.exit(0)

        self.autenticar_botao = self.canvas.create_image(0, 0, image=self.photo_botao_autenticar, anchor='w')
        self.titulo_autenticar_botao = self.canvas.create_text(0, 0, text='Autenticar', font=("Arial", "20", "bold"),
                                                               anchor='w')
        self.canvas.tag_bind(self.autenticar_botao, '<Button-1>', lambda event: verificar_usuario())
        self.canvas.tag_bind(self.titulo_autenticar_botao, '<Button-1>', lambda event: verificar_usuario())

        #############     JANELA DE CADASTRO DO USUARIO    ##############

        def cadastrar():
            janela_cadastro = Toplevel()
            janela_cadastro.title('Tela de cadastramento')
            janela_cadastro.geometry('450x600')

            janela_cadastro.resizable(False, False)

            canvas = Canvas(janela_cadastro, width=450, height=600)
            canvas.pack()

            imagem_de_fundo = canvas.create_image(0, 0, image=self.photo_fogo, anchor='nw')

            cor_painel = canvas.create_rectangle(50, 150, 400, 500, fill='black', width=5, outline='blue')

            titulo = canvas.create_text(0, 0, text='CADASTRAR', font=("Calibri", "30", "bold"), fill='white',
                                        anchor='n')

            ########      ENTRADAS PARA AS CREDENCIAIS       ###################

            nome_entry = Entry(janela_cadastro, font=("Arial", "20"))
            senha_entry = Entry(janela_cadastro, font=("Arial", "20"), show='*')
            confirmar_senha_entry = Entry(janela_cadastro, font=("Arial", "20"), show='*')
            nome_entrada = canvas.create_window(0, 0, window=nome_entry, anchor='n', width=200)
            senha_entrada = canvas.create_window(0, 0, window=senha_entry, anchor='n', width=200)
            confirmar_senha_entrada = canvas.create_window(0, 0, window=confirmar_senha_entry, anchor='n', width=200)

            #####  ROTULOS
            nome_rotulo = canvas.create_text(0, 0, text='Nome:', font=("Arial", "20", "bold"), fill='white', anchor='n')
            senha_rotulo = canvas.create_text(0, 0, text='Senha:', font=("Arial", "20", "bold"), fill='white',
                                              anchor='n')
            confirmar_senha_rotulo = canvas.create_text(0, 0, text='Confirmar\nsenha:', font=("Arial", "15", "bold"),
                                                        fill='white', anchor='n')

            ##############  FUNÇÃO MOSTRAR/OCULTAR SENHA NO CADASTRO  #######################

            ##### VARIAVEL DO VER SENHA
            senha_variable = IntVar()

            def ver_senha_cad():
                if senha_variable.get() == 0:
                    senha_entry['show'] = '*'
                    confirmar_senha_entry['show'] = '*'
                else:
                    senha_entry['show'] = ''
                    confirmar_senha_entry['show'] = ''

            senha_check = Checkbutton(janela_cadastro, variable=senha_variable, command=ver_senha_cad, bg='black')
            senha_ver = canvas.create_window(0, 0, window=senha_check, width=15, anchor='n')
            senha_ver_rotulo = canvas.create_text(0, 0, text='Ver senha', font=("Arial", "10"), fill='white',
                                                  anchor='w')

            ############# ARMAZENAR DADOS DO USUARIO CADASTRANDO #################

            # Requisitos senha
            aviso = ''

            letras, letras_aviso = list(ascii_letters), 'Inclua ao menos UMA letra'

            numeros, numeros_aviso = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'Inclua ao menos UM número'

            caracteres_especiais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';',
                                    '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
            caracteres_especiais_aviso = 'Inclua ao menos UM caractere especial'

            confirmar_senha_aviso = 'As senhas devem ser iguais'

            mensagem = canvas.create_text(0, 0, text='', font=("Arial", "14", "bold"), fill='yellow', anchor='n')

            def cadastrar_usuario():
                cadastrar_nome = nome_entry.get()
                cadastrar_senha = senha_entry.get()
                cadastrar_confirmar_senha = confirmar_senha_entry.get()
                if not cadastrar_nome or not cadastrar_senha:
                    messagebox.showwarning('Campo vazio', 'Preencha todos os campos')
                else:
                    aviso = ''
                    if not any(str(i) in cadastrar_senha for i in caracteres_especiais):
                        aviso += f'{caracteres_especiais_aviso}\n'
                        canvas.itemconfig(mensagem, text=aviso)

                    if not any(str(i) in cadastrar_senha for i in numeros):
                        aviso += f'{numeros_aviso}\n'
                        canvas.itemconfig(mensagem, text=aviso)

                    if not any(str(i) in cadastrar_senha for i in letras):
                        aviso += f'{letras_aviso}\n'
                        canvas.itemconfig(mensagem, text=aviso)

                    if cadastrar_confirmar_senha != cadastrar_senha:
                        aviso += f'{confirmar_senha_aviso}'
                        canvas.itemconfig(mensagem, text=aviso)

                    if cadastrar_confirmar_senha == cadastrar_senha and any(
                            str(i) in cadastrar_senha for i in caracteres_especiais) and any(
                        str(i) in cadastrar_senha for i in numeros) and any(
                        str(i) in cadastrar_senha for i in letras):
                        canvas.itemconfig(mensagem, text='')
                        persistir_usuario({'name': cadastrar_nome, 'password': cadastrar_senha})
                        messagebox.showinfo('Cadastro efetuado',
                                            'Suas credenciais foram cadastradas\nVocê agora pode se conectar')

            #### BOTAO DE CADASTRO DA TELA DE CADASTRAMENTO

            cadastrar_botao = canvas.create_image(0, 0, image=self.photo_botao_cadastrar, anchor='w')
            titulo_cadastrar_botao = canvas.create_text(0, 0, text='Cadastrar', font=("Arial", "20", "bold"),
                                                        anchor='w')
            canvas.tag_bind(cadastrar_botao, '<Button-1>', lambda event: cadastrar_usuario())
            canvas.tag_bind(titulo_cadastrar_botao, '<Button-1>', lambda event: cadastrar_usuario())

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
            canvas.coords(cadastrar_botao, 95, 465)
            canvas.coords(titulo_cadastrar_botao, 165, 460)
            canvas.coords(mensagem, 220, 520)

        ##### BOTAO DE CADASTRO DA TELA DE AUTENTICAÇÃO

        self.cadastrar_botao = self.canvas.create_image(0, 0, image=self.photo_botao_cadastrar, anchor='w')
        self.titulo_cadastrar_botao = self.canvas.create_text(0, 0, text='Cadastrar', font=("Arial", "20", "bold"),
                                                              anchor='w')
        self.canvas.tag_bind(self.cadastrar_botao, '<Button-1>', lambda event: cadastrar())
        self.canvas.tag_bind(self.titulo_cadastrar_botao, '<Button-1>', lambda event: cadastrar())

        ########  FUNÇÃO MOSTRAR/OCULTAR SENHA NO LOGIN  #######################

        self.senha_variable = IntVar()

        def ver_senha():
            if self.senha_variable.get() == 0:
                self.senha_entry['show'] = '*'
            else:
                self.senha_entry['show'] = ''

        self.senha_check = Checkbutton(master, variable=self.senha_variable, command=ver_senha, bg='#1A1243')
        self.senha_ver = self.canvas.create_window(0, 0, window=self.senha_check, width=15, anchor='w')
        self.senha_ver_rotulo = self.canvas.create_text(0, 0, text='Ver senha', font=("Arial", "10"), fill='white',
                                                        anchor='w')

        ########   AJUSTE DE POSIÇÃO INDIVIDUAL DOS WIDGETS NO LOGIN ##########

        self.canvas.place(x=-2, y=-2)
        self.canvas.coords(self.titulo, 500, 100)
        self.canvas.coords(self.nome_entrada, 550, 250)
        self.canvas.coords(self.senha_entrada, 550, 350)
        self.canvas.coords(self.nome_rotulo, 300, 250)
        self.canvas.coords(self.senha_rotulo, 300, 350)
        self.canvas.coords(self.senha_ver, 400, 390)
        self.canvas.coords(self.senha_ver_rotulo, 420, 390)
        self.canvas.coords(self.autenticar_botao, 390, 475)
        self.canvas.coords(self.titulo_autenticar_botao, 426, 475)
        self.canvas.coords(self.cadastrar_botao, 360, 555)
        self.canvas.coords(self.titulo_cadastrar_botao, 430, 550)
        self.canvas.coords(self.mensagem, 660, 460)


root = Tk()
login = Login(root)

root.resizable(False, False)


##########  ARMAZENAMENTO DE CREDENCIAIS ############
caminho_atual = os.path.abspath(__file__)
diretorio_atual = os.path.dirname(caminho_atual)
data_caminho = os.path.join(diretorio_atual, 'data.json')

def persistir_usuario(usuario):
    file = open(data_caminho)
    data = json.load(file)

    usuario_exists = False
    for user in data['users']:
        if user['name'] == usuario['name']:
            usuario_exists = True

    if usuario_exists:
        messagebox.showerror('Oops!', 'Usuário já existe!')
    else:
        data['users'].append(usuario)
        with open(data_caminho, 'w') as outfile:
            json.dump(data, outfile)

    file.close()


root.title("Tela de Autenticação")
root.geometry("1000x600")
root.mainloop()
