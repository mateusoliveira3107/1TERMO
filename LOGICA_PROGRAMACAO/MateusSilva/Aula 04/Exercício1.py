#Exercício 1
# Criar um algoritimo para calcular a média e com base em notas, podemos inserir duas notas e 
# apresenta a média e nota base de 50 é aprovado e menor que esse valor será reprovado

print("\n--Calculo de Média--")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1+nota2)/2

print("Sua média é de {}".format(media))

if media >= 50:
    print("Você foi aprovado")
elif media < 50:
    print("Você foi reprovado")













