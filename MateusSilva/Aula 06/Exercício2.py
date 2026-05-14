# Exercício 1
# Tente criar um código que conte de 1 a 10, mas use o continue para imprimir o número 5 (simulando uma falha de sensor específica no item 5).
from time import sleep
print("Leitura de números: ")
for i in range(1,11):
    if i == 5:
        sleep(0.5)
        print(f"Falha ao ler o número {i}")
        sleep(1.9)
        print(f"Número {i} foi retirado da lista.")
        sleep(3.2)
        continue
    print(i)
    sleep(0.8)
print("Acabou!")