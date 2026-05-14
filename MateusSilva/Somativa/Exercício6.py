from time import sleep
print("Classificações de lotes")

print("A) Alimentos")
print("E) Eletrônicos")
sleep(1)
codigo = input("Insira o código do produto: ").upper()
if codigo == "A":
    print("Você escolheu o lote ALIMENTOS")
elif codigo == "E":
    print("Você escolheu o lote ELETRÔNICOS")
else:
    print("Desconhecido")
    