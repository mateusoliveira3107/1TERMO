# Exercício 4
# Criar um algoritmo para calcular a média e com base em notas, podemos inserir duas notas e apresente a média porém a nota 0 a 100 para ser aprovado será
# acima de 70 e menor que 50 esse valor será reprovado porém vamos acrescentar uma nova condição que entre 50 e 70 recuperação

print("\n--Calculo de média--")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1+n2)/2

print("Sua média é de {}".format(media))
if media >= 70:
    print("Você foi aprovado")
elif media >= 50:
    print("Você está de recuperação")
elif media < 50:
    print("Você está reprovado")
else:
    print("Conta incorreta")













