# Exercício 2:
# Calculadora de IMC (Potência e divisão)
# O índice de Massa corporal (IMC) é calculado dividindo o peso pela altura ao quadrado

print("\n Bem-Vindo a nossa calculadora de IMC")

peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))

altura2 = altura * altura
imc = peso / altura2

print("O seu IMC é igual a: ", imc)