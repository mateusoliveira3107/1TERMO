# Exercício - Crie uma aplicação que faça o cálculo da idade de pessoas
# Deve perguntar o nome da pessoa e o ano de nascimento

import tkinter as tk
from tkinter import messagebox, ttk

def cadastrar():
    nome = nome_entry.get()
    try:
        ano = int(ano_nascimento_entry.get())
    except ValueError:
        messagebox.showerror("Erro", "Preencha com um valor válido")

    if nome == "" and ano == "":
        messagebox.showwarning("Erro", "Preencha todos os campos")
    elif ano >= 2026:
        messagebox.showerror("Erro", "Preencha com um valor válido")
    else:
        idade = 2026 - ano
        messagebox.showinfo("Bem-Vindo", f"Olá {nome}, você tem {idade} anos de idade!")

janela = tk.Tk()
janela.title("Cálculo de Idade")
janela.geometry("650x400")
janela.configure(bg="#346AB1")

lbl_nome = tk.Label(janela, text= " Digite seu nome ", font=("Arial", 16), bg="#96CCFF", fg="#000000")
lbl_nome.grid(row=0, column=0, pady=10, padx=5)
nome_entry = tk.Entry(janela, width=22, bg="#96CCFF", font=("Arial", 14))
nome_entry.grid(row=0, column=1, pady=10, padx=5)

lbl_idade = tk.Label(janela, text=" Digite seu ano de nascimento ", font=("Arial", 16), bg="#96CCFF", fg="#000000")
lbl_idade.grid(row=1, column=0, pady=10, padx=5)
ano_nascimento_entry = tk.Entry(janela, width=22, bg="#96CCFF", font=("Arial", 14))
ano_nascimento_entry.grid(row=1, column=1, pady=10, padx=5)

botao_cadastrar = tk.Button(text=" Calcular Idade ", font=("Arial", 14), bg="#17A758",fg="#000000", command=cadastrar)
botao_cadastrar.grid(row=2, column=0, pady=10, padx=100)

botao_fechar = tk.Button(text=" Fechar ", font=("Arial", 14), bg="#A71717",fg="#000000", command=janela.destroy)
botao_fechar.grid(row=3, column=0, pady=0, padx=100)

janela.mainloop()