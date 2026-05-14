# Exercício 3
# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta

print("=-="*8)
print("Tabuada")
print("=-="*8)

print("Tabuada do 5:")

num = 5
for multiplicador in range(1,11):
    print(f"{num} x {multiplicador} =", num*multiplicador)

num = int(input("\nescolha um número para ver a tabuada: "))
for multiplicador in range(1,11):
    print(f"{num} x {multiplicador} =", num*multiplicador)
