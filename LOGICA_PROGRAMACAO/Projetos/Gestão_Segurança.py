from time import sleep

ano_atual = 2026
funcionarios = []

def menu():
    print("--"*20)
    print("      Menu - Brigada de Incêndio")
    print("--"*20)
    print("1. Cadastrar Funcionário")
    print("2. Verificação de EPIs")
    print("3. Verificar Validade de Treinamento")

def cadastro():
    print("--"*20)
    print("      Cadastro de Funcionários")
    print("--"*20)
    nome_funcionario = input("Informe o nome do funcionário: ")
    setor_funcionario = input("Informe o setor do funcionário: ")
    status = input("Informe o status dos treinamentos [ NR-10 / NR-35 / Brigada ]: ")
    print(f"Funcionário {nome_funcionario} cadastrado com sucesso!")
    print(f"Setor: {setor_funcionario}")
    print(f"Status: {status}")
    sleep(3)
    print("--"*20)
    funcionarios.append(nome_funcionario)
    return nome_funcionario, setor_funcionario, status



def verificacao_epi():
    print("\n1. Elétrica")
    print("2. Mecânica")
    print("3. DEV")
    print("4. Logística")
    resposta = int(input("Informe seu setor:"))
    if resposta == 1:
        print("\n- Setor Elétrico -")
        print("- Obrigatoriedade de Uniforme Técnico")
        print("- Obrigatoriedade de luvas de alta tensão")
        print("- Obrigatoriedade de botas dielétricas.")
        print("- Obrigatoriedade de óculos de segurança.")
        print("- Obrigatoriedade de Protetor auditivo.")

    elif resposta == 2:
        print("\n- Setor Mecânico -")
        print("- Obrigatoriedade de Uniforme Técnico")
        print("- Obrigatoriedade de luvas de segurança")
        print("- Obrigatoriedade de óculos de segurança.")
        print("- Obrigatoriedade de botas de segurança.")
        print("- Obrigatoriedade de Protetor auditivo.")
    elif resposta == 3:
        print("\n- Setor Desenvolvimento de Sistemas -")
        print("- Obrigatoriedade de Uniforme Técnico")
    elif resposta == 4:
        print("\n- Setor Logística -")
        print("- Obrigatoriedade de Uniforme Técnico")
    else:
        print("Dados Inválidos!")


def ultimo_treinamento():
    ano = int(input("Informe o ano do último treinamento: "))
    if (ano_atual - ano) > 2:
        print("Treinamento Vencido! Encaminhar para reciclagem.")
    else:
        print("Treinamento Válido")
    return ano


while True:
    menu()
    opc = int(input("Sua opção: "))
    if opc == 1:
        cadastro()
    elif opc == 2:
        verificacao_epi()
    elif opc == 3:
        ultimo_treinamento()
