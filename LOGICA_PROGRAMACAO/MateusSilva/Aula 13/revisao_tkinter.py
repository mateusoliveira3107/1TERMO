# Revisão Tkinter

import tkinter as tk
from tkinter import messagebox, ttk

# DEF funções em bloco
def cadastrar_usuario():
    nome_usuario = nome_entry.get()
    curso_usuario = curso_entry.get()
    escola_usuario = cmb_nome_escola.get()
    
    if nome_usuario == "" and curso_usuario == "" and escola_usuario == "":
        messagebox.showwarning("Bem-Vindo", "Digite seu nome, seu curso e escolha sua escola")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá, {nome_usuario}. Seu curso é {curso_usuario} e sua esola é {escola_usuario}")


# Etapa 0 Janela

janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("600x450")
janela.configure(bg="#346AB1")

# Etapa 1 Componentes

# Labels = Rótulos ou Nossos antigos "prints"
lbl_nome = tk.Label(janela, text= "Digite seu nome", font=("Arial", 14), bg="#346AB1", fg="#000000")
lbl_nome.grid(row=0, column=0, pady=10, padx=10)
# Entry = Caixas de texto antigos input
nome_entry = tk.Entry(janela, width=30)
nome_entry.grid(row=0, column=1, pady=10, padx=10)

lbl_curso = tk.Label(janela, text= "Digite seu curso", font=("Arial", 14), bg="#346AB1", fg="#000000")
lbl_curso.grid(row=1, column=0, pady=10, padx=10)
curso_entry = tk.Entry(janela, width=30)
curso_entry.grid(row=1, column=1, pady=10, padx=10)

lbl_nome_escola = tk.Label(janela, text="Escolha sua escola", font=("Arial", 14),  bg="#346AB1")
lbl_nome_escola.grid(row=2, column=0, pady=10, padx=10)
# Combobox = Caixa de seleção
cmb_nome_escola = ttk.Combobox(janela, value=["SESI 408","SESI 05"])
cmb_nome_escola.grid(row=2, column=1, pady=10, padx=10)

# Botões
btn_realizar_cadastro = tk.Button(janela, text="Cadastrar", font=("Arial", 14), bg="#34A59C", fg="#000000", command=cadastrar_usuario)
btn_realizar_cadastro.grid(row=5, column=1, pady=10, padx=0)

btn_fechar_janela = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#A53434", fg="#000000", command=janela.destroy)
btn_fechar_janela.grid(row=6, column=1, pady=50, padx=0)

# Etapa 4 Loop
janela.mainloop()