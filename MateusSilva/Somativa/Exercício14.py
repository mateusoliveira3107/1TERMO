from time import sleep
estoque = 100

while True:
    print("1- Adicionar itens")
    print("2- Remover itens")
    print("3- Sair")
    opc = int(input("Sua opção: "))
    if opc == 1:
        add = int(input("Quantos itens deseja adicionar ao estoque? "))
        estoque += add
        print(f"Estoque: {estoque} itens\n")
        if estoque < 10:
            sleep(0.5)
            print("Estoque Crítico!")
            sleep(1.5)

    elif opc == 2:
        remover = int(input("Quantos itens deseja remover do estoque? "))
        estoque -= remover
        print(f"Estoque: {estoque} itens\n")
        if estoque < 10:
            sleep(0.5)
            print("Estoque Crítico!\n")
            sleep(1.5)
    
    elif opc == 3:
        print("Saindo do sistema...")
        sleep(1.5)
        break