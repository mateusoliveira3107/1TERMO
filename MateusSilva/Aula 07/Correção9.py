print("Validação de Medida")
medida = float(input("Digite a medida da peça em mm... "))
if medida < 9.8:
    print("A peça está abaixo da tolerância.")
elif medida > 10.2:
    print("A peça está acima da tolerância.")
else:
    print("A peça está dentro da tolerância.")