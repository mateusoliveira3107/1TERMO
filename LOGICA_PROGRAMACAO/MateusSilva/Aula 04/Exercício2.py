# Exercício 2
# Criar um algoritmo para demonstrar a sinalização de um semáforo

print("\nEscolha a cor que o semáforo sinalizará: ")
print("\nPara verde: 1\n")
print("Para amarelo: 2\n")
print("Para vermelho: 3\n")
cor = int(input("Qual cor você quer que seja sinalizada no semáforo? "))
if cor == 1:
    print("Cor sinalizadada: verde")
elif cor == 2:
    print("Cor sinalizada: amarelo")
elif cor == 3:
    print("Cor sinalizada: amarelo")
else:
    print("Essa opção não existe")
