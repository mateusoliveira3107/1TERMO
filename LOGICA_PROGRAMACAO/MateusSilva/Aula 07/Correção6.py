# # Vesão 1
print("Classificador de Lotes")
codigo_produto = input("Digite o código do produto... ")
if codigo_produto == "A":
    print("Alimentos")
elif codigo_produto == "E":
    print("Eletrônicos")
else:
    print("Desconhecido") 

# Vesão 2
print("Classificador de lotes - Versão 2")
codigo_produto = input("Digite o código do produto... ")
if codigo_produto.startswith("A"):
    print("Alimentos")
elif codigo_produto.startswith("E"):
    print("Eletrônicos")
else:
    print("Desconhecido")