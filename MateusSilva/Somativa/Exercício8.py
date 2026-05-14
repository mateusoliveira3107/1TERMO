produzidas = int(input("Digite a quantidade de peças produzidas: "))
defeituosas = int(input("Digite a quantidade de peças defeituosas: "))
porcentagem = produzidas * (5/100)

if defeituosas > porcentagem:
    print("Revisar Processo")
else:
    print("Processo Otimizado!")


