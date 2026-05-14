print("Inspeção de peças")

nota1 = float(input("Digite a nota da inspeção 1 (0 a 10)... "))
nota2 = float(input("Digite a nota da inspeção 2 (0 a 10)... "))
nota3 = float(input("Digite a nota da inspeção 3 (0 a 10)... "))

media = (nota1 + nota2 + nota2) / 3
print(f"Média de qualidade de peças: {media:.2f}")