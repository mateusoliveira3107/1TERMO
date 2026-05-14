maior = 0

for i in range (1,6):
    temperatura = float(input(f"Digite a temperatura do {i}º sensor: "))
    if temperatura > maior:
        maior = temperatura

print(f"Maior temperatura: {maior}C°")