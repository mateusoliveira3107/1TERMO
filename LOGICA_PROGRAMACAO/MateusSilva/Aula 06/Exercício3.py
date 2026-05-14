# Exercício 2
# Simule um semáforo com parada para cada cor, determine um tempo que deseja para quando mudar para tal cor ele represente uma pausa
from time import sleep

print("=-=-"*7)
print("        Semáforo")
print("=-=-"*7)

while True:
    print("1) Verde")
    print("2) Amarelo")
    print("3) Vermelho")
    opc = int(input("Opção: "))

    if opc == 1:
        print("\nSinal Verde ligado!")
        for i in range(4):
            sleep(1.5)
            print("...")
        print("Sinal desligado!")
        break

    elif opc == 2:
        print("\nSinal Amarelo ligado!")
        for i in range(4):
            sleep(1)
            print("...")
        print("Sinal desligado!")
        break

    elif opc == 3:
        print("\nSinal Vermelho ligado!")
        for i in range(4):
            sleep(2)
            print("...")
        print("Sinal desligado!")
        break

    else:
        print("Valor inválido! Tente novamente.")