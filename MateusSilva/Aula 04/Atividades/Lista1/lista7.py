pecas = int(input("Digite o número de peças produzidas: "))
pecasd = int(input("Digite o número de peças defeituosas: "))
pecasboas = pecas - pecasd

total = (pecasboas/pecas) * 100

print(f"Peças boas: {pecas}")
print(f"Peças defeituosas: {pecasd}")

print(f"Aproveitamento de peças: {total:.2f}%")