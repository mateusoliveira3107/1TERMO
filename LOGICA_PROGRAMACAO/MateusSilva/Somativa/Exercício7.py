sensor_porta = input("Insira a situação da porta [fechada] ou [aberta]: ")
botao_emergencia = input("Insira a situação do botão de emergência [ligado] ou [desligado]: ")

if sensor_porta == "fechada":
    if botao_emergencia == "desligado":
        print("A máquina pode iniciar!")
    else:
        print("A máquina não pode iniciar!")

else:
    print("A máquina não pode iniciar!")