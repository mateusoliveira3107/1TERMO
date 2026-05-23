from time import sleep
import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Sistema Brigada de Incêndio")
janela.configure(bg="#3a536b")
janela.geometry("1100x700")

ano_atual = 2026
funcionarios = []

def mensagemerro():
    messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")

def cadastro():
    janelacadastro = tk.Toplevel(janela)
    janelacadastro.title("Cadastrar funcionário")
    janela.geometry("1000x600")
    janela.configure(bg="#3a536b")
    def salvar():
        nome = nome.get()
        setor = setor.get()
        status = status.get()
        if nome == "" or setor == "" or status == "":
            mensagemerro()
            return
        funcionario = {"nome":nome, "setor":setor, "status":status}
        funcionario.append(funcionario)
        messagebox.showinfo(f"Funcionario {nome} cadastrado com sucesso",
        f"\nSetor: {funcionario["setor"]}", f"\nStatus: {funcionario["status"]}")

    tk.Label(janelacadastro, text="Nome do funcionário:", font=("Arial", 11), bg = "#3a536b").pack(pady=5)
    nome = tk.Entry(janelacadastro, font=("Arial", 12))
    nome.pack(pady=5)

    tk.Label(janelacadastro, text="Setor:", font=("Arial", 11), bg = "#3a536b").pack(pady=5)
    setor = tk.Entry(janelacadastro, font=("Arial", 12))
    nome.pack(pady=5)

    tk.Label(janelacadastro, text="Status:", font=("Arial", 12), bg = "#3a536b").pcak(pady=5)
    status = tk.Entry(janelacadastro, font=("Arial", 12))
    status.pack(pady=5)

    botaocadastro = tk.Button(janelacadastro, text="Cadastrar", font=("Arial", 12), bg= "#23a057", command=salvar)
    botaocadastro.pcak(pady=30)

def verificacao_epi():
    textoepi = "- Obrigatoriedade de EPI por setor -\n" \
    "\n1. Setor Elétrico: Uniforme Técnico, Luvas de alta tensão, Botas dielétricas, Óculos de segurança, Protetor auditivo\n" \
    "2. Setor Mecânico: Uniforme Técnico, Luvas de segurança, Óculos de segurança, Botas de segurança, Protetor auditivo\n" \
    "3. Desenvolvimento de sistemas: Uniforme técnico\n4. Logística: Uniforme técnico\n" \
    "5. Trabalho em altura: Cinturão de segurança"
    messagebox.showinfo(f"Verificação de EPI {verificacao_epi()}")

def ultimo_treinamento():
    janelatreinamento = tk.Toplevel(janela)
    janelatreinamento.title("Validade de treinamento")
    janelatreinamento.geometry("1000x600")
    janelatreinamento.configure(bg="#3a536b")

    def calculovalidade():
        ano = int(ano.get())
        try:
            if (ano_atual - ano) > 2:
                messagebox.showwarning("Treinamento Vencido! Encaminhar para reciclagem.")
            else:
                messagebox.showinfo("Treinamento Válido")
        except ValueError:
            messagebox.showerror("Erro, digite um ano válido")
    
    tk.Label(janelatreinamento, text="Informe o ano do último treinamento:", font=("Arial", 12), bg="#3a536b" )
    ano = tk.Entry(janelatreinamento, text="Verificar", font=("Arial", 11))
    ano.pack(pady=5)

    botaocalcular = tk.Button(janelatreinamento, text="Verificar", font=("Arial", 11), command=calculovalidade)
    botaocalcular.pack(pady=15)

def relatorio():
    if not funcionarios:
        messagebox.showwarning("Nenhum usuário cadastrado", font=("Arial", 11))
    else:
        tk.Label(janela, text="\n- Relatório Geral -")
        tk.Label(janela, text=f"Funcionários cadastrados: {len(funcionarios)}", font=("Arial", 11))
        for i in funcionarios:
            tk.Label(janela, text=f"Nome: {i['nome']} - Setor: {i['setor']} - Status: {i['status']}", font=("Arial", 11))


titulo = tk.Label(janela, text="    Menu - Brigada de Incêndio", font=("Arial", 16), bg="#3a536b")
titulo.pack(pady=30)

tk.Button(janela, text="1. Cadastrar Funcionário", font=("Arial",12), command=cadastro).pack(pady=10)
tk.Button(janela, text="2. Verificação de EPIs", font=("Arial",12), command=verificacao_epi).pack(pady=10)
tk.Button(janela, text="3. Verificar Validade de Treinamento", font=("Arial",12), command=ultimo_treinamento).pack(pady=10)
tk.Button(janela, text="4. Exibir Relatório", font=("Arial",12), command=relatorio).pack(pady=10)
tk.Button(janela, text="5. Sair", font=("Arial",12), command=janela.destroy).pack(pady=30)

janela.mainloop()