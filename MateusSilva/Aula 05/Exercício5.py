# Exercício 5
# Criar um menu de opções com 4 itens ex: Escolher Series apresente sua escolha de series das outras três
# qualquer opcao diferente sair do menu
import time
print("=-="*8)

print("1. Drama")
print("2. Terror")
print("3. Comédia")
print("4. Romance")
print("5. Sair")

opcao = int(input("Escolha uma opção: "))
while opcao != 5:
    if opcao == 1:
        print("Serie escolhida: Drama")
        break
    elif opcao ==2:
        print("Serie escolhida: Terror")
        break
    elif opcao ==3:
        print("Serie escolhida: Comédia")
        break
    elif opcao ==4:
        print("Serie escolhida: Romance")
        break


time.sleep(1)
print("Saindo do sistema")