# projeto cancela automática
# criar um algoritmo que consiga gerenciar entrada e saída de veículos,
# inserindo valores por hora permanecida.
# a forma de entrada e saída deve ser especificada e permitir o usuário inserir os dados
# necessários para registro do veículo

# Passos
# 1 - pressionar o botão, imprimiu o ticket
#  calcular o tempo de permanência
#  pegar o ticket
#  devolver ticket na saída

# 2 - Acesso por TAGs (Sem parar, Connect car...)
# calcular o tempo de permanencia
# gerar pagamento em fatura
# liberar e fechar cancelas

# 3 - Erros
# verificar sinal de transmissão da TAG
# verificar acesso por ticket ou TAG ao mesmo tempo
# perdeu ticket (levantar Informçaões)
# Problemas com cancela

from time import sleep

print("-=-=-=" * 8)
print("        Bem-vindo ao shopping do Mateus   ")
print("-=-=-=" * 8)
sleep(1)
def menu():                                                     # Função para mostrar o menu
    print("\n\n------- MENU - Estacionamento -------")
    print("1. Acesso por ticket")
    print("2. Acesso por TAGs")
    print("3. Sair")

def acesso_ticket():                                             # Função para entrar com ticket
    placacarro = input("Informe a placa do seu veículo: ")
    horainicial = float(input("Horário de chegada: "))
    sleep(1)
    print(f"Veículo {(placacarro).upper()} cadastrado com sucesso!\n")
    input("[ENTER] para retirar seu ticket ")
    sleep(1)
    print(f"Código do Ticket: {placacarro}.{horainicial:.0f}\n")
    sleep(1.5)
    print("Acesso liberado! Seja bem-vindo")
    sleep(1.5)
    print("\n-- Cancela aberta --")
    sleep(3)
    print("\n-- Cancela fechada --\n")
    return placacarro, horainicial

def acesso_TAGs():                                                 # Função para entrar com tags
    placacarro = input("Informe a placa do veículo: ")
    horainicial = float(input("Horário de chegada: "))
    sleep(1.5)
    print(f"Veículo {(placacarro).upper()} cadastrado com sucesso!")
    sleep(2)
    print("Acesso liberado! Seja bem-vindo")
    sleep(1.5)
    print("-- Cancela aberta --")
    sleep(3)
    print("\n-- Cancela fechada --")
    return placacarro, horainicial

while True:
    while True:
        menu()

        try:
            resposta = int(input("Sua opção: "))
            
            if resposta == 1:
                placacarro, horainicial = acesso_ticket()
            elif resposta == 2:
                placacarro, horainicial = acesso_TAGs()
            elif resposta == 3:
                print("Fechando sistema...")
                sleep(1.5)
                break
            else:
                print("Valor inválido. Tente novamente")

        except ValueError:
            print("Valor inválido")

    horasaida = float(input("Informe o horário de saída: "))
    tempo = horasaida - horainicial
    horas = int(tempo)
    pagamento = horas * 10

    sleep(0.5) 
    print("\n-----------------------------------------------")
    print("| Nota de pagamento")
    print("| Valor p/hora: R$10.00")
    print("|------------------------------------------------")
    print(f"|NOME DO VEÍCULO: {placacarro.upper()}           ")
    print(f"|Tempo: {horas:.0f}h"           )
    print(f"|Valor a pagar: R${pagamento}          ")
    print("\n----------- Saída do estacionamento -----------      \n")   


