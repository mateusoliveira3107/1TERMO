# Exercício 3
# Criar um algoritmo para aplicação de descontos para produtos como sapatos aplicar 10%, para produtos como roupas 5% e produtos como perfumes 2%

print("\n--Descontos da loja--")

print("\nDefina o produto comprado: ")
print("Para sapatos digite 1")
print("Para roupas digite 2")
print("Para perfumes digite 3")

produtin = int(input("Qual tipo de produto foi comprado? "))
qntd = int(input("Quantidade do produto: "))
preço = float(input("\nDigite o preço do produto: "))

total = qntd*preço
tot1 = total * 0.1
tot2 = total * 0.05
tot3 = total * 0.02

if produtin == 1:
    print("Sapatos tem desconto de 10%")
elif produtin == 2:
    print("Roupas tem desconto de 5%")
elif produtin == 3:
    print("Perfumes tem desconto de 2%")
else:
    print("Esse produto não está na loja")

if produtin == 1:
    print("Valor total do produto com desconto de 10% é de {}R$",(total-tot1))
elif produtin == 2:
     print("Valor total do produto com desconto de 5% é de {}R$",(total-tot2))
else:
    print("Valor total do produto com desconto de 2% é de {}R$",(total-tot3))




