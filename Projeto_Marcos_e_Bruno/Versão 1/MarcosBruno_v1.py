from tkinter import *
from tkinter import messagebox
from string import ascii_letters

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Times New Roman", "30")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 60
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
  
        self.titulo = Label(self.primeiroContainer, text="CONECTAR")
        self.titulo["font"] = ("Impact", "30", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome:", font=self.fontePadrao, fg = "grey")
        self.nomeLabel.pack(side=LEFT, padx = 10)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 20
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.senhaLabel = Label(self.terceiroContainer, text="Senha:", font=self.fontePadrao, fg = "grey")
        self.senhaLabel.pack(side=LEFT, padx = 10)
  
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 20
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer, bg = 'green')
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "15", 'bold')
        self.autenticar["width"] = 18
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack(pady = 10)

        self.cadastrar = Button(self.quartoContainer, bg = 'blue')
        self.cadastrar["text"] = "Cadastre-se"
        self.cadastrar["font"] = ("Calibri","15", 'bold')
        self.cadastrar["width"] = 18
        self.cadastrar["command"] = self.cadastrarJanela
        self.cadastrar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=None, fg="red")
        self.mensagem["font"]=("Times New Roman","10","bold")
        self.mensagem.pack()


    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if not usuario or not senha:
            messagebox.showwarning("Campo Vazio", "Preencha todos os campos!")
        elif usuario in Users and senha == Senhas[Users.index(usuario)]:
            self.mensagem["fg"] = "green"
            self.mensagem["text"] = "Autenticado!"
        else:
            self.mensagem["fg"] = "red"
            self.mensagem["text"] = "Usuário inexistente. Por favor, cadastre-se."

        #Cadastrar usuário
    def cadastrarJanela(self):
        self.mensagem["fg"] = "blue"
        self.mensagem["text"] = "A janela de cadastro foi aberta"
        janela = Toplevel()
        fonteCadastro = ("Times New Roman", "20")

        cadBloco1 = Frame(janela)
        cadBloco1["pady"] = 60
        cadBloco1.pack()

        cadBloco2 = Frame(janela)
        cadBloco2["padx"] = 80
        cadBloco2["pady"] = 15
        cadBloco2.pack()

        cadBloco3 = Frame(janela)
        cadBloco3["padx"] = 80
        cadBloco3["pady"] = 15
        cadBloco3.pack()

        cadBloco4 = Frame(janela)
        cadBloco4["padx"] = 50
        cadBloco4["pady"] = 10
        cadBloco4.pack()

        cadBloco5 = Frame(janela)
        cadBloco5["padx"] = 50
        cadBloco5["pady"] = 10
        cadBloco5.pack()

        tituloCad = Label(cadBloco1)
        tituloCad["text"] = "CADASTRAR"
        tituloCad["font"] = ("Impact", "30", "bold")
        tituloCad.pack()

        nomeLabel2 = Label(cadBloco2, text = "Nome:", fg = "grey")
        nomeLabel2["font"] = fonteCadastro
        nomeLabel2.pack(side = LEFT, padx = 10)

        nomeEntry2 = Entry(cadBloco2, width = 20)
        nomeEntry2["font"] = fonteCadastro
        nomeEntry2.pack(padx = 20)

        senhaLabel2 = Label(cadBloco3, text = "Senha:", fg = "grey")
        senhaLabel2["font"] = fonteCadastro
        senhaLabel2.pack(side = LEFT, padx = 10)

        def showSenha():
            if mostrarSenha.get() == True:
                senhaEntry2["show"] = ""
            else:
                senhaEntry2["show"] = "*"

        mostrarSenha = BooleanVar()

        senhaEntry2 = Entry(cadBloco3, width = 20)
        senhaEntry2["font"] = fonteCadastro
        senhaEntry2["show"] = "*"
        senhaEntry2.pack(side = LEFT)

        senhaShow = Checkbutton(cadBloco3, variable = mostrarSenha, command = showSenha)
        senhaShow["text"] = "Ver senha"
        senhaShow["font"] = ("Times New Roman", "10")
        senhaShow.pack(pady = 5, side = RIGHT)
        
        mensagem = Label(cadBloco4, fg = "red")
        mensagem["font"] = ("Times New Roman", "8")
        mensagem["text"] = ""
        mensagem.pack()

        caractereMSG = Label(cadBloco4, fg = "red", font = ("Times New Roman", "10"))
        caractereMSG["text"] = ""
        caractereMSG.pack()

        letraMSG = Label(cadBloco4, fg = "red", font = ("Times New Roman", "10"))
        letraMSG["text"] = ""
        letraMSG.pack()

        numeroMSG = Label(cadBloco4, fg = "red", font = ("Times New Roman", "10"))
        numeroMSG["text"] = ""
        numeroMSG.pack()

        def cadastro():
            user = nomeEntry2.get()
            password = senhaEntry2.get()

            numeroMSG["text"] = ""
            letraMSG["text"] = ""
            caractereMSG["text"] = ""

            if not user or not password:
                messagebox.showwarning("Campo Vazio", "Preencha todos os campos!")
            elif user in Users:
                messagebox.showwarning("Nome negado", "Este nome já existe. Por favor, escolha outro.")
            elif not any(str(i) in password for i in caracteres_especiais):
                caractereMSG["text"] = "Inclua ao menos UM caractere especial (#$!@%...)"
                pass
            elif not any(str(i) in password for i in numeros):
                numeroMSG["text"] = "Inclua ao menos UM número"
                pass
            elif not any(str(i) in password for i in letras):
                letraMSG["text"] = "Inclua ao menos UMA letra"
            else:
                Users.append(user)
                Senhas.append(password)
                messagebox.showinfo("Cadastro realizado", "Usuário cadastrado com sucesso!")
                janela.destroy()


        cadastrarButton = Button(cadBloco5, width = 10, command = cadastro)
        cadastrarButton["text"] = "Cadastrar"
        cadastrarButton["font"] = ("Times New Roman", "10", "bold")
        cadastrarButton.pack(pady = 10)


Users = []
Senhas = []

letras = list(ascii_letters)
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caracteres_especiais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']


root = Tk()
Application(root)

root.mainloop()



