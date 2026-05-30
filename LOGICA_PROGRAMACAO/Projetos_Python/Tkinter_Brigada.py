import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Sistema Brigada de Incêndio")
janela.configure(bg="#253A61")
janela.geometry("1100x600")

ano_atual = 2026
funcionarios = []

def mensagemerro():
    messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")

def cadastro():
    janelacadastro = tk.Toplevel(janela)
    janelacadastro.title("Cadastrar funcionário")
    janelacadastro.geometry("700x400")
    janelacadastro.configure(bg="#3a536b")
    def salvar():
        campo_nome = nome.get()
        campo_setor = setor.get()
        campo_status = status.get()
        if campo_nome == "" or campo_setor == "" or campo_status == "":
            mensagemerro()
            return
        funcionario = {"nome":campo_nome, "setor":campo_setor, "status":campo_status}
        funcionarios.append(funcionario)
        messagebox.showinfo(f"Funcionario {campo_nome} cadastrado com sucesso",
        f"\nNome: {campo_nome}"f"\nSetor: {funcionario['setor']}"f"\nStatus: {funcionario['status']}")
        janelacadastro.destroy()

    tk.Label(janelacadastro, text="Nome do funcionário:", font=("Arial", 18), bg = "#3a536b").pack(pady=5)
    nome = tk.Entry(janelacadastro, font=("Arial", 18))
    nome.pack(pady=5)

    tk.Label(janelacadastro, text="Setor:", font=("Arial", 18), bg = "#3a536b").pack(pady=5)
    setor = tk.Entry(janelacadastro, font=("Arial", 18))
    setor.pack(pady=5)

    tk.Label(janelacadastro, text="Status:", font=("Arial", 18), bg = "#3a536b").pack(pady=5)
    status = tk.Entry(janelacadastro, font=("Arial", 18))
    status.pack(pady=5)

    botaocadastro = tk.Button(janelacadastro, text="Cadastrar", font=("Arial", 18), bg= "#23a057", command=salvar)
    botaocadastro.pack(pady=30)

def verificacao_epi():
    textoepi = "- Obrigatoriedade de EPI por setor -\n" \
    "\n1. Setor Elétrico: Uniforme Técnico, Luvas de alta tensão, Botas dielétricas, Óculos de segurança, Protetor auditivo\n" \
    "2. Setor Mecânico: Uniforme Técnico, Luvas de segurança, Óculos de segurança, Botas de segurança, Protetor auditivo\n" \
    "3. Desenvolvimento de sistemas: Uniforme técnico\n4. Logística: Uniforme técnico\n" \
    "5. Trabalho em altura: Cinturão de segurança"
    messagebox.showinfo("Verificação de EPI", textoepi)

def ultimo_treinamento():
    janelatreinamento = tk.Toplevel(janela)
    janelatreinamento.title("Validade de treinamento")
    janelatreinamento.geometry("500x250")
    janelatreinamento.configure(bg="#3a536b")

    def calculovalidade():
        try:
            anodigitado = int(ano.get())
            if (ano_atual - anodigitado) > 2:
                messagebox.showwarning("Aviso!", "Treinamento Vencido! Encaminhar para reciclagem.")
                janelatreinamento.destroy()
            elif anodigitado > ano_atual:
                messagebox.showerror("Erro", "Digite um ano válido")
                janelatreinamento.lift()
            else:
                messagebox.showinfo("Treinamento", "Treinamento Válido")
                janelatreinamento.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Digite um ano válido")
            janelatreinamento.lift()
    
    tk.Label(janelatreinamento, text="Informe o ano do último treinamento:", font=("Arial", 17), bg="#3a536b" ).pack(pady=10)
    ano = tk.Entry(janelatreinamento, font=("Arial", 15), bg="#6C7F91")
    ano.pack(pady=10)
    botaocalcular = tk.Button(janelatreinamento, text="Verificar", font=("Arial", 15), command=calculovalidade)
    botaocalcular.pack(pady=20)
    
def relatorio():
    if not funcionarios:
        messagebox.showwarning("Erro!", "Nenhum usuário cadastrado")
    else:
        janelarelatorio = tk.Toplevel(janela)
        janelarelatorio.title("Relatório")
        janelarelatorio.geometry("600x400")
        janelarelatorio.configure(bg="#3a536b")

        titulorelatorio = tk.Label(janelarelatorio, text="=-=-=-=-=-=-=-=-=-=-=-=-=-=     Relatório de Funcionários    =-=-=-=-=-=-=-=-=-=-=-=-=-=",font=("Arial", 18), bg="#1F546D")
        titulorelatorio.pack(pady=5)
        tk.Label(janelarelatorio, text=f" - - - - - - - - - - - - - - -    Funcionários cadastrados: {len(funcionarios)}    - - - - - - - - - - - - - - - ", font=("Arial", 15), bg="#80A0B1").pack(pady=15)
        for i in funcionarios:
            tk.Label(janelarelatorio, text=f" Nome: {i['nome']} - Setor: {i['setor']} - Status: {i['status']} ", font=("Arial", 12), bg="#93ABB8").pack(pady=10)
        tk.Button(janelarelatorio, text="Fechar", font=("Arial", 14),bg="#d81010", command=janelarelatorio.destroy).pack(pady=80)

titulo = tk.Label(janela, text="=-=-=-=-=-=-=-=-=-=-=-=-=-=      Menu - Brigada de Incêndio      =-=-=-=-=-=-=-=-=-=-=-=-=-=", font=("Arial", 22), bg="#286865")
titulo.pack(pady=35)

tk.Button(janela, text="1. Cadastrar Funcionário", font=("Arial",18),bg="#4d607c", command=cadastro).pack(pady=15)
tk.Button(janela, text="2. Verificação de EPIs", font=("Arial",18),bg="#4d607c", command=verificacao_epi).pack(pady=15)
tk.Button(janela, text="3. Verificar Validade de Treinamento",bg="#4d607c", font=("Arial",18), command=ultimo_treinamento).pack(pady=15)
tk.Button(janela, text="4. Exibir Relatório", font=("Arial",18),bg="#4d607c", command=relatorio).pack(pady=15)
tk.Button(janela, text="5. Sair", font=("Arial",18),bg="#d81010", command=janela.destroy).pack(pady=70)


janela.mainloop()