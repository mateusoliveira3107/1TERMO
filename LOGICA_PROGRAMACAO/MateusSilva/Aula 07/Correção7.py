print("Segurança de Operação")
sensor_porta = input("Digite o status do sensor da porta (fechada/aberta)... ")
botao_emergencia = input("Digite o status do botão de emergência (ligado/desligado)... ")
if sensor_porta == "fechada" and botao_emergencia == "desligado":
    print("A máquina pode iniciar.")
else:
    print("A máquina não pode iniciar.")