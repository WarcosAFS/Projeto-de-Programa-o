from tkinter import Tk, Frame, Label, Entry, Button, Toplevel, messagebox
from string import ascii_letters, digits, punctuation

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Identificação")
        self.fontePadrao = ("Times New Roman", 30)
        self.caracteres_especiais = punctuation

        self.create_widgets()

    def create_widgets(self):
        self.primeiroContainer = Frame(self.master, pady=60)
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self.master, padx=80, pady=15)
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self.master, padx=80, pady=15)
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self.master, pady=50)
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="CONECTAR", font=("Impact", 30, "bold"))
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome:", font=self.fontePadrao, fg="grey")
        self.nomeLabel.pack(side="left", padx=10)

        self.nome = Entry(self.segundoContainer, width=20, font=self.fontePadrao)
        self.nome.pack(side="left")

        self.senhaLabel = Label(self.terceiroContainer, text="Senha:", font=self.fontePadrao, fg="grey")
        self.senhaLabel.pack(side="left", padx=10)

        self.senha = Entry(self.terceiroContainer, width=20, font=self.fontePadrao, show="*")
        self.senha.pack(side="left")

        self.autenticar = Button(self.quartoContainer, text="Autenticar", font=("Calibri", 15, "bold"), width=18, bg="green", command=self.verifica_senha)
        self.autenticar.pack(pady=10)

        self.cadastrar = Button(self.quartoContainer, text="Cadastre-se", font=("Calibri", 15, "bold"), width=18, bg="blue", command=self.cadastrar_janela)
        self.cadastrar.pack()

        self.mensagem = Label(self.quartoContainer, font=("Times New Roman", 10, "bold"), fg="red")
        self.mensagem.pack()

    def verifica_senha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        if not usuario or not senha:
            messagebox.showwarning("Campo Vazio", "Preencha todos os campos!")
        elif usuario in self.users and senha == self.senhas[self.users.index(usuario)]:
            self.mensagem["fg"] = "green"
            self.mensagem["text"] = "Autenticado!"
        else:
            self.mensagem["fg"] = "red"
            self.mensagem["text"] = "Usuário inexistente. Por favor, cadastre-se."

    def cadastrar_janela(self):
        janela = Toplevel(self.master)
        janela.title("Cadastramento")
        fonteCadastro = ("Times New Roman", 20)

        cadBloco1 = Frame(janela, pady=60)
        cadBloco1.pack()

        cadBloco2 = Frame(janela, padx=80, pady=15)
        cadBloco2.pack()

        cadBloco3 = Frame(janela, padx=80, pady=15)
        cadBloco3.pack()

        cadBloco4 = Frame(janela, padx=50, pady=10)
        cadBloco4.pack()

        cadBloco5 = Frame(janela, padx=50, pady=10)
        cadBloco5.pack()

        tituloCad = Label(cadBloco1, text="CADASTRAR", font=("Impact", 30, "bold"))
        tituloCad.pack()

        nomeLabel2 = Label(cadBloco2, text="Nome:", fg="grey", font=fonteCadastro)
        nomeLabel2.pack(side="left", padx=10)

        nomeEntry2 = Entry(cadBloco2, width=20, font=fonteCadastro)
        nomeEntry2.pack(padx=20)

        senhaLabel2 = Label(cadBloco3, text="Senha:", fg="grey", font=fonteCadastro)
        senhaLabel2.pack(side="left", padx=10)

        def show_senha():
            if mostrarSenha.get():
                senhaEntry2["show"] = ""
            else:
                senhaEntry2["show"] = "*"

        mostrarSenha = BooleanVar()

        senhaEntry2 = Entry(cadBloco3, width=20, font=fonteCadastro, show="*")
        senhaEntry2.pack(side="left")

        senhaShow = Checkbutton(cadBloco3, text="Ver senha", font=("Times New Roman", 10), variable=mostrarSenha, command=show_senha)
        senhaShow.pack(pady=5, side="right")

        mensagem = Label(cadBloco4, fg="red", font=("Times New Roman", 8))
        mensagem.pack()

        caractereMSG = Label(cadBloco4, fg="red", font=("Times New Roman", 10))
        caractereMSG.pack()

        letraMSG = Label(cadBloco4, fg="red", font=("Times New Roman", 10))
        letraMSG.pack()

        numeroMSG = Label(cadBloco4, fg="red", font=("Times New Roman", 10))
        numeroMSG.pack()

        def cadastro():
            user = nomeEntry2.get()
            password = senhaEntry2.get()

            numeroMSG["text"] = ""
            letraMSG["text"] = ""
            caractereMSG["text"] = ""

            if not user or not password:
                messagebox.showwarning("Campo Vazio", "Preencha todos os campos!")
            elif user in self.users:
                messagebox.showwarning("Nome negado", "Este nome já existe. Por favor, escolha outro.")
            elif not any(str(i) in password for i in self.caracteres_especiais):
                caractereMSG["text"] = "Inclua ao menos UM caractere especial (#$!@%...)"
            elif not any(str(i) in password for i in self.numeros):
                numeroMSG["text"] = "Inclua ao menos UM número"
            elif not any(str(i) in password for i in self.letras):
                letraMSG["text"] = "Inclua ao menos UMA letra"
            else:
                self.users.append(user)
                self.senhas.append(password)
                messagebox.showinfo("Cadastro realizado", "Usuário cadastrado com sucesso!")
                janela.destroy()

        cadastrarButton = Button(cadBloco5, text="Cadastrar", font=("Times New Roman", 10, "bold"), width=10, command=cadastro)
        cadastrarButton.pack(pady=10)

def main():
    root = Tk()
    Application(root)
    root.title("Identificação")
    root.mainloop()

if __name__ == "__main__":
    main()
