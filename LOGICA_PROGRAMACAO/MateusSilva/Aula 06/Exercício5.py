# Exercício 4
# Identificador de peças defeituosas (for + if)
# Percorra uma lista de medidas de peças: 
# Medidas: [50.1, 49.8, 52.0, 48.5]
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".
from time import sleep
medidas = [50.1, 49.8, 52.0, 48.5]

print("===="*9)
print("          Análise de peças")
print("===="*9)
sleep(2)
for i in medidas:
    if i >= 50:
        print(f"Peça com medida {i}: Aprovada!")
        sleep(0.8)
    else:
       print(f"Peça com medida {i}: Reprovada!")
       sleep(0.8)
sleep(1)
print("\nAnálise concluida!\n")

