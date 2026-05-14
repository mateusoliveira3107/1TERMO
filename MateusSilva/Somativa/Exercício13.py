senha = "admin123"
tentativas = 0
resposta = input("\nDigite a senha do supervisor: ")
r = resposta
tentativas += 1


while r != senha:
    r = input("Acesso negado! Tente novamente: ")
    tentativas += 1
    if tentativas == 3:
        if r == senha:
             print("Acertou")
             
        else:
            print("Painel bloqueado")

if r == tentativas:
    print("Painel Bloqueado")
else:
    print("Acertou")