produto = input("Nome do produto: ")
quantidade = int(input("Quantidade vendida: "))
preço = float(input("Preço unitário: "))
total = preço * quantidade


print("---------------------------")
print("Relatório de vendas")
print("---------------------------")

print(f"Produto: {produto}")
print(f"Quatidade vendida: {quantidade}")
print(f"Preço unitário: {preço}")
print(f"Total de vendas: R${total}")
print("---------------------------")