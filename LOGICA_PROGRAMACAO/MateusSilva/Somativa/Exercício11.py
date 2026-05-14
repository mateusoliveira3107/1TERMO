peso = 0

resposta = float(input("Digite o peso da caixa: "))
peso += resposta

while resposta != 0:
    resposta = float(input("Digite o peso da caixa: "))
    peso += resposta

print(f"Peso total: {peso}")