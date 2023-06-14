# Projeto-de-Programacao
Aplicação de Python na criação de interfaces gráficas.

####  Versão 1:

A fonte padrão utilizada é Arial.
A janela principal é intitulada como "Dados do usuário".
A cor do botão "Autenticar" é verde.
Existe um botão "Cadastrar" para permitir o cadastro de novos usuários.
As mensagens exibidas na interface são configuradas através das propriedades "text" e "fg" das labels.
As informações de usuários e senhas são armazenadas nas listas Users e Senhas, respectivamente.


#### Versão 2:

A fonte padrão utilizada é Times New Roman.
A janela principal é intitulada como "CONECTAR".
A cor do botão "Autenticar" é verde.
Existe um botão "Cadastre-se" para abrir uma nova janela de cadastro.
As mensagens exibidas na interface são configuradas através da caixa de diálogo messagebox da biblioteca Tkinter.
As informações de usuários e senhas são armazenadas nas listas Users e Senhas, respectivamente.
Foram adicionadas verificações de segurança no cadastro de novos usuários. A senha precisa conter pelo menos um caractere especial, um número e uma letra maiúscula ou minúscula. Caso contrário, uma mensagem de erro é exibida.
Foram adicionadas variáveis para verificar a existência de letras, números e caracteres especiais na senha.
A nova janela de cadastro é criada usando a função Toplevel().
