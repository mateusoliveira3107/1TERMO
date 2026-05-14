# Conteúdo sobre lógica
# Exemplo 1
# print("--Expressões lógicas--")
# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#     print("Você é maior idade")
#     print("Pode tirar carta de motorista")
# elif idade >= 16:
#     print("Você ainda não é maior, mas já pode votar")
# else:
#     print("Você é menor de idade")


# if: "se" a condição for verdadeira
# elif: "senão, se" (usado para múltiplas condições) 
# else: "senão" (executa se nenhuma das anteriores for verdadeira)

# Exemplo 2

# print("\n Escolha sua modalidade")
# print("Opção 1: TI")
# print("Opção 2: Humanas")
# print("Opção 3: Exatas")

# modalidade = int(input("Digite sua modalidade por números: "))
# if modalidade == 1:
#     print("Você escolheu TI")
# elif modalidade == 2:
#     print("Você escolheu humanas")
# else:
#     print("Você escolheu exatas")

# Exemplo 3
# print("Categorias de series e filmes")
# print("Escolha uma categoria")

# print("Series = S")
# print("Filmes = F")

# categoria = input("\nDigite sua categoria: ")
# if categoria == "S":
#     print("Sua escolha foi para séries")
# elif categoria == "F":
#        print("Sua escolha foi para filmes")
# else:
#     print("Você não escolheu nenhuma das categorias")

# Exemplo 4

print("\nCalculadora com condições")
print("Escolha como quer calcular")
print("1 = soma")
print("2 = subtração")
print("3 = multiplicação")
print("4 = divisão")

calculadora = float(input("Digite sua opção para calcular: \n"))
if calculadora == 1:
    print("1 = Você escolheu soma")
    soma1 = int(input("Digite o primeiro valor: "))
    soma2 = int(input("Digite o segundo valor: "))
    print(soma1+soma2)
elif calculadora == 2:
    print("2 = Você escolheu subtração")
    sub1 = int(input("Digite o primeiro valor: "))
    sub2 = int(input("Digite o segundo valor: "))
    print(sub1-sub2)
elif calculadora == 3:
    print("3 = Você escolheu multiplicação")
    mult1 = int(input("Digite o primeiro valor: "))
    mult2 = int(input("Digite o segundo valor: "))
    print(mult1*mult2)
elif calculadora == 4:
    print("Você escolheu divisão")
    div1 = int(input("Digite o primeiro valor: "))
    div2 = int(input("Digite o segundo valor: "))
    print(div1/div2)

