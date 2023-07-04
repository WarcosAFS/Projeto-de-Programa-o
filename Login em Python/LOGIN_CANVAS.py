from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from string import ascii_letters
import json
import subprocess
import os
import sys


class Login:
    def __init__(self, master=None):

        ##### FONTES PADRAO
        self.fonte = ("Arial", "30", "bold")
        self.fonte_entradas = ("Times New Roman", "30")

        self.canvas = Canvas(master, width=1000, height=600, highlightthickness= 0)
        self.canvas.pack()

        ########      DIRETORIO ATUAL       #####################

        self.caminho_atual = os.path.abspath(__file__)
        self.diretorio_atual = os.path.dirname(self.caminho_atual)

        #########      ADICIONAR IMAGENS PARA PERSONALIZAÇÃO     ###############

        self.caminho_background = os.path.join(self.diretorio_atual, 'Imagens/background.jpg')
        self.abrir_imagem_background = Image.open(self.caminho_background)
        self.imagem_background_resized = self.abrir_imagem_background.resize((1002, 602))
        self.bg = ImageTk.PhotoImage(self.imagem_background_resized)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.caminho_image_fogo = os.path.join(self.diretorio_atual, 'Imagens/imagem_fogo.jpg')
        self.abrir_imagem_fogo = Image.open(self.caminho_image_fogo)
        self.imagem_fogo_resized = self.abrir_imagem_fogo.resize((450, 600))
        self.fogo = ImageTk.PhotoImage(self.imagem_fogo_resized)

        self.caminho_logo = os.path.join(self.diretorio_atual, 'Imagens/python_logo.png')
        self.abrir_imagem_logo = Image.open(self.caminho_logo)
        self.imagem_logo_resized = self.abrir_imagem_logo.resize((185, 100))
        self.logo = ImageTk.PhotoImage(self.imagem_logo_resized)
        self.canvas.create_image(0, 470, image=self.logo, anchor="nw")

        self.caminho_botao_autenticar = os.path.join(self.diretorio_atual, 'Imagens/botao_autenticar.png')
        self.abrir_botao_autenticar = Image.open(self.caminho_botao_autenticar)
        self.botao_autenticar_resized = self.abrir_botao_autenticar.resize((210, 80))
        self.botao_autenticar = ImageTk.PhotoImage(self.botao_autenticar_resized)

        self.caminho_botao_cadastrar = os.path.join(self.diretorio_atual, 'Imagens/botao_cadastrar.png')
        self.abrir_botao_cadastrar = Image.open(self.caminho_botao_cadastrar)
        self.botao_cadastrar_resized = self.abrir_botao_cadastrar.resize((270, 90))
        self.botao_cadastrar = ImageTk.PhotoImage(self.botao_cadastrar_resized)

        #### TITULO
        self.canvas.create_text(500, 100, text="CONECTAR", font=("Calibri", "50", "bold"), fill="#F0E68C")

        #### ENTRADAS DE AUTENTICAÇÃO
        self.nome_entry = Entry(master, font=self.fonte_entradas)
        self.senha_entry = Entry(master, font=self.fonte_entradas, show='*')
        self.canvas.create_window(550, 250, window=self.nome_entry, width=300)
        self.canvas.create_window(550, 350, window=self.senha_entry, width=300)

        self.canvas.create_text(300, 250, text='Nome:', fill='white', font=self.fonte)
        self.canvas.create_text(300, 350, text='Senha:', fill='white', font=self.fonte)

        #### MENSAGEM GERAL (CANTO INFERIOR)
        self.mensagem = self.canvas.create_text(660, 460, text='', font=("Arial", "22"), fill='yellow', state='hidden',
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

        self.autenticar_botao = self.canvas.create_image(390, 475, image=self.botao_autenticar, anchor='w')
        self.titulo_autenticar_botao = self.canvas.create_text(430, 475, text='Autenticar', font=("Arial", "20", "bold"), anchor='w')
        self.canvas.tag_bind(self.autenticar_botao, '<Button-1>', lambda event: verificar_usuario())
        self.canvas.tag_bind(self.titulo_autenticar_botao, '<Button-1>', lambda event: verificar_usuario())


        #############     JANELA DE CADASTRO DO USUARIO    ##############
        def cadastrar():
            janela_cadastro = Toplevel()
            janela_cadastro.title('Tela de Cadastro')
            janela_cadastro.geometry('450x600')
            janela_cadastro.resizable(False, False)

            canvas = Canvas(janela_cadastro, width=450, height=600, highlightthickness= 0)
            canvas.pack()

            canvas.create_image(0, 0, image=self.fogo, anchor='nw')
            canvas.create_rectangle(50, 150, 400, 500, fill='black', width=5, outline='blue')

            canvas.create_text(225, 50, text='CADASTRAR', font=("Calibri", "30", "bold"), fill='white', anchor='n')


            ########      ENTRADAS PARA AS CREDENCIAIS       ###################
            nome_entry = Entry(janela_cadastro, font=("Arial", "20"))
            senha_entry = Entry(janela_cadastro, font=("Arial", "20"), show='*')
            confirmar_senha_entry = Entry(janela_cadastro, font=("Arial", "20"), show='*')
            canvas.create_window(280, 200, window=nome_entry, anchor='n', width=200)
            canvas.create_window(280, 280, window=senha_entry, anchor='n', width=200)
            canvas.create_window(280, 360, window=confirmar_senha_entry, anchor='n', width=200)

            #####  ROTULOS
            canvas.create_text(115, 200, text='Nome:', font=("Arial", "20", "bold"), fill='white', anchor='n')
            canvas.create_text(115, 280, text='Senha:', font=("Arial", "20", "bold"), fill='white', anchor='n')
            canvas.create_text(115, 360, text='Confirmar\nsenha:', font=("Arial", "15", "bold"), fill='white', anchor='n')


            ##############  FUNÇÃO MOSTRAR/OCULTAR SENHA NO CADASTRO  #######################
            senha_variable = IntVar()

            def ver_senha_cad():
                if senha_variable.get() == 0:
                    senha_entry['show'] = '*'
                    confirmar_senha_entry['show'] = '*'
                else:
                    senha_entry['show'] = ''
                    confirmar_senha_entry['show'] = ''

            senha_check = Checkbutton(janela_cadastro, variable=senha_variable, command=ver_senha_cad, bg='black')
            canvas.create_window(230, 400, window=senha_check, width=15, anchor='n')
            canvas.create_text(240, 412, text='Ver senha', font=("Arial", "10"), fill='white', anchor='w')

            ############# ARMAZENAR DADOS DO USUARIO CADASTRANDO #################
            # Requisitos senha
            aviso = ''

            letras, letras_aviso = list(ascii_letters), 'Inclua ao menos UMA letra'

            numeros, numeros_aviso = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'Inclua ao menos UM número'

            caracteres_especiais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';',
                                    '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
            
            caracteres_especiais_aviso = 'Inclua ao menos UM caractere especial'
            confirmar_senha_aviso = 'As senhas devem ser iguais'

            mensagem = canvas.create_text(220, 520, text='', font=("Arial", "14", "bold"), fill='yellow', anchor='n')

            def cadastrar_usuario():
                cadastrar_nome = nome_entry.get()
                cadastrar_senha = senha_entry.get()
                cadastrar_confirmar_senha = confirmar_senha_entry.get()
                if not cadastrar_nome or not cadastrar_senha or not cadastrar_confirmar_senha:
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
                        janela_cadastro.destroy()

            #### BOTAO DE CADASTRO DA TELA DE CADASTRAMENTO

            cadastrar_botao = canvas.create_image(95, 465, image=self.botao_cadastrar, anchor='w')
            titulo_cadastrar_botao = canvas.create_text(165, 460, text='Cadastrar', font=("Arial", "20", "bold"), anchor='w')
            canvas.tag_bind(cadastrar_botao, '<Button-1>', lambda event: cadastrar_usuario())
            canvas.tag_bind(titulo_cadastrar_botao, '<Button-1>', lambda event: cadastrar_usuario())


        ##### BOTAO DE CADASTRO DA TELA DE AUTENTICAÇÃO
        self.cadastrar_botao = self.canvas.create_image(360, 555, image=self.botao_cadastrar, anchor='w')
        self.titulo_cadastrar_botao = self.canvas.create_text(430, 550, text='Cadastrar', font=("Arial", "20", "bold"),
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
        self.canvas.create_window(400, 390, window=self.senha_check, width=15, anchor='w')
        self.canvas.create_text(420,390, text='Ver senha', font=("Arial", "10"), fill='white', anchor='w')



root = Tk()
login = Login(root)
root.resizable(False, False)
root.title("Tela de Autenticação")
root.geometry("1000x600")


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
        messagebox.showinfo('Cadastro efetuado', 'Suas credenciais foram cadastradas\nVocê agora pode se conectar')

    file.close()



root.mainloop()
