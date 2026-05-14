# Exercício 5
# Uma balança industrial está pesando um lote de 6 sacos de insumos.
# O peso ideal de cada saco é 50kg, mas o sistema aceita variações

from time import sleep
print("=-=-"*7)
print("        Balança")
print("=-=-"*7)
sleep(1)

pesos = [47.9, 51.5, 50.0, 62.5, 70.9, 32.5]

for i in pesos:
    if i > 50:
        print(f"O peso '{i}' está abaixo do ideal para consumo.")
        sleep(0.8)
    elif i < 50:
        print(f"O peso '{i}' está acima do ideal para consumo consumo.")
        sleep(0.8)
    elif i == 50:
        print(f"O peso '{i}' está no peso ideal para consumo.")
        sleep(0.8)