pecas = 0
pecasruins = 0

for i in range (1,6):
    diametro = float(input(f"Digite o diâmetro da {i}° peça: "))
    if diametro < 19.9:
        pecasruins += 1

    elif diametro > 20.1:
        pecasruins += 1

    else:
        pecas += 1

pecastotais = pecas + pecasruins
porcentagemperdida = (pecasruins/pecastotais) * 100
eficiencia = 100 - porcentagemperdida

print(f"Total de peças aprovadas: {pecas}")
print(f"Total de peças ruins: {pecasruins}")
print(f"Porcentagem de eficiência do lote: {eficiencia:.1f}%")