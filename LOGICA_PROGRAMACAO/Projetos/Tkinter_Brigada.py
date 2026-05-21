from time import sleep
import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Sistema de Segurança Brigada")
janela.configure(bg="#021375")
janela.geometry("1100x600")

ano_atual = 2026
funcionarios = []

def menu():
    print("--"*20)
    print("      Menu - Brigada de Incêndio")
    print("--"*20)
    print("1. Cadastrar Funcionário")
    print("2. Verificação de EPIs")
    print("3. Verificar Validade de Treinamento")
    print("4. Exibir Relatório")
    print("5. Sair")

def cadastro():
    print("--"*20)
    print("      Cadastro de Funcionários")
    print("--"*20)
    funcionario = {}
    funcionario["nome"] = input("Informe o nome do funcionário: ")
    funcionario["setor"] = input("Informe o setor do funcionário: ")
    funcionario["status"] = input("Informe o status dos treinamentos [ NR-10 / NR-35 / Brigada ]: ")
    print(f"Funcionário {funcionario['nome']} cadastrado com sucesso!")
    print(f"Setor: {funcionario['setor']}")
    print(f"Status: {funcionario['status']}")
    sleep(1.5)
    print("--"*20)
    funcionarios.append(funcionario)

def verificacao_epi():
    print("\n1. Elétrica")
    print("2. Mecânica")
    print("3. DEV")
    print("4. Logística")
    print("5. Trabalho em altura")
    resposta = int(input("Informe seu setor:"))
    if resposta == 1:
        print("\n- Setor Elétrico -\n")
        print("- Obrigatoriedade de Uniforme Técnico")
        print("- Obrigatoriedade de luvas de alta tensão")
        print("- Obrigatoriedade de botas dielétricas.")
        print("- Obrigatoriedade de óculos de segurança.")
        print("- Obrigatoriedade de Protetor auditivo.")

    elif resposta == 2:
        print("\n- Setor Mecânico -\n")
        print("- Obrigatoriedade de Uniforme Técnico")
        print("- Obrigatoriedade de luvas de segurança")
        print("- Obrigatoriedade de óculos de segurança.")
        print("- Obrigatoriedade de botas de segurança.")
        print("- Obrigatoriedade de Protetor auditivo.")
    elif resposta == 3:
        print("\n- Setor Desenvolvimento de Sistemas -\n")
        print("- Obrigatoriedade de Uniforme Técnico")
    elif resposta == 4:
        print("\n- Setor Logística -\n")
        print("- Obrigatoriedade de Uniforme Técnico")
    elif resposta == 5:
        print("\n- Setor Trabalho em altura-\n")
        print("- Obrigatoriedade de cinturão de segurança")
        print("- Obrigatoriedade de talabarte")
    else:
        print("Dados Inválidos!")


def ultimo_treinamento():
    ano = int(input("Informe o ano do último treinamento: "))
    if (ano_atual - ano) > 2:
        print("Treinamento Vencido! Encaminhar para reciclagem.")
    else:
        print("Treinamento Válido")

def relatorio():
    print("\n- Relatório Geral -")
    print(f"Funcionários cadastrados: {len(funcionarios)}")
    for i in funcionarios:
        print(f"Nome: {i['nome']} - Setor: {i['setor']} - Status: {i['status']}")
while True:
    menu()
    opc = int(input("Sua opção: "))
    if opc == 1:
        cadastro()
    elif opc == 2:
        verificacao_epi()
    elif opc == 3:
        ultimo_treinamento()
    elif opc == 4:
        relatorio()
    elif opc == 5:
        print("Saindo do sistema")
        sleep(2)
        break
    else:
        print("Dados inválidos")