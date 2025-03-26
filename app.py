import customtkinter as ctk

# Configuração de aparência
ctk.set_appearance_mode('dark')  # Modo escuro
ctk.set_default_color_theme('blue')  # Tema de cor

# Função de validação de login
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    if usuario == '' and senha == '': 
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login negado!', text_color='red')

# Criação da janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

# Criando os widgets

# Usuário
label_usuario = ctk.CTkLabel(app, text='Usuário', anchor="center")
label_usuario.pack(pady=5)

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=5)

# Senha
label_senha = ctk.CTkLabel(app, text='Senha', anchor="center")
label_senha.pack(pady=5)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show="*")  # Ocultar senha
campo_senha.pack(pady=5)

# Botão de login
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

# Campo de feedback
resultado_login = ctk.CTkLabel(app, text='', anchor="center")
resultado_login.pack(pady=5)

import customtkinter as ctk
import webbrowser

# Simulação de credenciais válidas
USUARIOS = {"usuario": "senha123"}

def autenticar():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    if USUARIOS.get(usuario) == senha:
        print("Login bem-sucedido!")
        webbrowser.open("http://localhost:8501")  # URL da sua dashboard Streamlit
        app.destroy()  # Fecha o app de login após abrir a dashboard
    else:
        label_status.configure(text="Usuário ou senha incorretos!", text_color="red")

# Criar janela
app = ctk.CTk()
app.geometry("300x300")
app.title("Login")

# Widgets
label_usuario = ctk.CTkLabel(app, text="Usuário:")
label_usuario.pack(pady=5)
entrada_usuario = ctk.CTkEntry(app)
entrada_usuario.pack(pady=5)

label_senha = ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=5)
entrada_senha = ctk.CTkEntry(app, show="*")
entrada_senha.pack(pady=5)

botao_login = ctk.CTkButton(app, text="Login", command=autenticar)
botao_login.pack(pady=10)

label_status = ctk.CTkLabel(app, text="")
label_status.pack()

# Rodar app
app.mainloop()
