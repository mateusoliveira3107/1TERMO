# TKINTER

# # Componentes widgets
# # tk: Tk() # Janela
# # lb: Label() # Rótulo
# # bt: Button() # Botão
# # et: Entry() # Caixa de texto

# import tkinter as tk
# from tkinter import messagebox

# 1. Criar a janela principal
# janela = tk.Tk()
# janela.title("Minha Primeira Janela GUI")
# janela.configure(bg="#0BD30B")
# janela.geometry("1200x800") # Largura x Altura

# # 2. Criar a função do botão (evento)
# def mostrar_mensagem():
#     messagebox("Sucesso!", "Você clicou no botão")

# # 3. Criar os componentes
# lbl_titulo = tk.Label(janela, text="Bem-vindo à nossa aula de Tkinder", font=("Arial", 28, "bold"), bg="#FF0000")
# btn_botao = tk.Button(janela, text="Clique Aqui", font=("Arial", 22), bg="#e00d42", fg="white", command=mostrar_mensagem)
# btn_close = tk.Button(janela, text=" Fechar ", font=("Arial", 14, "bold"), bg="#e60e7a", command=janela.destroy)

# # 4. Posicionar os componentes
# lbl_titulo.pack(pady=10) # 'pady' adiciona um espaçamento vertical
# btn_botao.pack(pady=20)
# btn_close.pack(pady=200)

# 5. Rodar o loop da interface
# janela.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# def saudar_usuario():
#     nome = campo_nome.get()

#     if nome == "":
#         messagebox.showwarning("Aviso", "Por favor, digite seu nome!")
#     else:
#         messagebox.showinfo("Saudações Alunos", f"olá, {nome}! Seja bem-vindo ao mundo das interfaces gráficas")

# # Configurações da janela
# app = tk.Tk()
# app.title("Exeplo 1")
# app.geometry("1200x800")

# # Componentes
# lbl_instrucao = tk.Label(app, text="Digite seu nome abaixo: ")
# lbl_instrucao.pack(pady=10)

# campo_nome = tk.Entry(app, font=("Arial", 12))
# campo_nome.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=saudar_usuario)
# btn_enviar.pack(pady=15)

# app.mainloop()

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Calculadora de Média")
janela.configure(bg="#000279")
janela.geometry("1000x600")

def mensagem_erro():
    messagebox.showerror("Valor inválido")
def calcular_media():
        try:
            n1 = int(numero1.get())
            if n1 == "":
                mensagem_erro()
                return
            n2 = int(numero2.get())
            if n2 == "":
                mensagem_erro()
                return
            n3 = int(numero3.get())
            if n3 == "":
                mensagem_erro()
                return
        except ValueError:
               mensagem_erro()
               return
        media = (n1+n2+n3)/3
        messagebox.showinfo(f"Média: {media:.2f}")


lbl_numero = tk.Label(janela, text="Número 1:", font=("Arial", 14, "bold"), bg="#19a3ff").pack(pady=5)
numero1 = tk.Entry(janela, font=("Arial", 22))
numero1.pack(pady=30)

lbl_numero2 = tk.Label(janela, text="Número 2:", font=("Arial", 14, "bold"), bg="#19a3ff").pack(pady=5)
numero2 = tk.Entry(janela, font=("Arial", 22))
numero2.pack(pady=30)

lbl_numero3 = tk.Label(janela, text="Número 3:", font=("Arial", 14, "bold"), bg="#19a3ff").pack(pady=5)
numero3 = tk.Entry(janela, font=("Arial", 22))
numero3.pack(pady=30)

btn_calcular = tk.Button(janela, text="Calcular Média",command=calcular_media, font=("Arial", 30))
btn_calcular.pack(pady=15)

janela.mainloop()