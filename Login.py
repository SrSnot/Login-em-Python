import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('firebase-admin')

import tkinter as tk
from tkinter import messagebox
import firebase_admin
from firebase_admin import auth, credentials

# Configuração do Firebase
config = {
    "apiKey": "AIzaSyDckuOQr_eZunwQmwhoVzlacZCrABMFSvc",
    "authDomain": "executor-de-scripts-pra-roblox.firebaseapp.com",
    "projectId": "executor-de-scripts-pra-roblox",
    "storageBucket": "executor-de-scripts-pra-roblox.appspot.com",
    "messagingSenderId": "148764386648",
    "appId": "1:148764386648:web:6fb7d06b529daa44ae712d",
    "measurementId": "G-P1H3QKWMD7"
}

cred = credentials.Certificate(config)
firebase_admin.initialize_app(cred)

def verificar_login():
    nome = nome_entry.get()
    senha = senha_entry.get()
    try:
        user = auth.sign_in_with_email_and_password(nome, senha)
        messagebox.showinfo("Login", "Login bem-sucedido! Bem-vindo ao software.")
        script = r"C:\Users\leo herobrineXD\Desktop\virus\Executor\executor.py"
        exec(open(script).read())
    except:
        messagebox.showerror("Login", "Nome de usuário ou senha incorretos.")

def criar_conta():
    nome = nome_entry.get()
    senha = senha_entry.get()
    try:
        user = auth.create_user_with_email_and_password(nome, senha)
        messagebox.showinfo("Criar conta", "Conta criada com sucesso!")
    except:
        messagebox.showerror("Criar conta", "Falha ao criar a conta. Tente novamente.")


def criar_conta():
    nome = nome_entry.get()
    senha = senha_entry.get()
    try:
        user = auth.create_user(
            email=nome,
            email_verified=False,
            password=senha,
            disabled=False)
        messagebox.showinfo("Criar conta", "Conta criada com sucesso!")
    except:
        messagebox.showerror("Criar conta", "Falha ao criar a conta. Tente novamente.")

# Cria uma nova janela
janela = tk.Tk()

# Cria os campos de entrada para o nome de usuário e a senha
tk.Label(janela, text="Nome de usuário:").pack()
nome_entry = tk.Entry(janela)
nome_entry.pack()

tk.Label(janela, text="Senha:").pack()
senha_entry = tk.Entry(janela, show="*")
senha_entry.pack()

# Cria o botão de login
tk.Button(janela, text="Login", command=verificar_login).pack()

# Cria o botão de criar conta
tk.Button(janela, text="Criar conta", command=criar_conta).pack()

# Inicia o loop principal da janela
janela.mainloop()
