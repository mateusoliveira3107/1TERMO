print("Múltiplas Leituras")
temperaturas = []
for i in range(1,6):
    temp = float(input(f"Digite a temperatura do sensor {i} em C°..."))
    temperaturas.append(temp)

print(f"Maior Temperatura lida: {max(temperaturas):.2f} C°")
print(f"Menor Temperatura lida: {min(temperaturas):.2f} C°")
print(f"Soma das Temperaturas lidas: {sum(temperaturas):.2f} C°")
