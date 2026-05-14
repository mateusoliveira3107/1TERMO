# Exercício 3 - SOma de cargas de energia (for)

# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dendro do loop) o consumo em KWh de cada uma das 5 máquinas.
# Ao final do loop, o programa deve exibir o consumo total da fábrica.
total = 0
for i in range(1,6):
    consumo = float(input(f"Digite o consumo em KWh da {i}º máquina: "))
    total += consumo

print(f"Consumo total da fábrica: {total:.2f} KWh")
