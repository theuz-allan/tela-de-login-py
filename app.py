import customtkinter as ctk

#config. aparencia
ctk.set_appearance_mode('dark')

#criar funcionalidades
def validar_login():
    usario = campo_usuario.get()
    senha = campo_senha.get()

    # verificar se o usario e senha
    if usario == 'matheus' and senha == '123456':
        resultado_login.configure(text = 'Login feito com sucesso', 
        text_color='green')
    else:
        resultado_login.configure(text = 'Usuário ou senha incorretos', 
        text_color='red')


#criação da janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

#adicionar campos de entrada
#label
label_usuario = ctk.CTkLabel(app,text='Usuário:')
label_usuario.pack(pady=10)
#entry
campo_usuario = ctk.CTkEntry(app,placeholder_text='Insira seu Usuário')
campo_usuario.pack(pady=10)

#label
label_senha = ctk.CTkLabel(app,text='Senha:')
label_senha.pack()
#entry
campo_senha = ctk.CTkEntry(app,placeholder_text = "Insira sua Senha")
campo_senha.pack(pady=10)

#button
botao_login = ctk.CTkButton(app,text = 'Login',command = validar_login)
botao_login.pack(pady=10)
#campo feedback de login
resultado_login = ctk.CTkLabel(app,text = '')
resultado_login.pack(pady=10)

#iniciar aplicação
app.mainloop()