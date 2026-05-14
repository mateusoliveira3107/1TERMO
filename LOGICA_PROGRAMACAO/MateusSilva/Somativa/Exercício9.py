medida = float(input("Digite a medida da peça em mm: "))

if medida < 9.8:
    print("Abaixo da tolerância")

elif medida > 10.2:
    print("Acima da tolerância")

else:
    print("Dentro da tolerância")