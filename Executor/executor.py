import tkinter as tk
from tkinter import messagebox

def injectar():
    messagebox.showinfo("Ação", "Você clicou em 'Injectar'!")

def executar():
    messagebox.showinfo("Ação", "Você clicou em 'Executar'!")

def kill():
    messagebox.showinfo("Ação", "Você clicou em 'Kill'!")

def tema_claro():
    janela.config(bg='white')
    texto.config(bg='white', fg='black')
    botao_injectar.config(bg='white', fg='black')
    botao_executar.config(bg='white', fg='black')
    botao_kill.config(bg='white', fg='black')
    botao_tema_claro.config(bg='white', fg='black')
    botao_tema_escuro.config(bg='white', fg='black')

def tema_escuro():
    janela.config(bg='black')
    texto.config(bg='black', fg='white')
    botao_injectar.config(bg='black', fg='white')
    botao_executar.config(bg='black', fg='white')
    botao_kill.config(bg='black', fg='white')
    botao_tema_claro.config(bg='black', fg='white')
    botao_tema_escuro.config(bg='black', fg='white')

janela = tk.Tk()

texto = tk.Text(janela, height=10, width=60)
texto.grid(row=0, column=0, columnspan=3)

botao_injectar = tk.Button(janela, text="Injectar", command=injectar)
botao_injectar.grid(row=1, column=0)

botao_executar = tk.Button(janela, text="Executar", command=executar)
botao_executar.grid(row=1, column=1)

botao_kill = tk.Button(janela, text="Kill", command=kill)
botao_kill.grid(row=1, column=2)

botao_tema_claro = tk.Button(janela, text="Branco", command=tema_claro)
botao_tema_claro.grid(row=0, column=3, sticky='E')

botao_tema_escuro = tk.Button(janela, text="Dark", command=tema_escuro)
botao_tema_escuro.grid(row=1, column=3, sticky='E')

janela.resizable(False, False)  # Adicionado para remover a opção de maximizar

janela.mainloop()
