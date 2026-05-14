temp = float(input("Digite a temperatura do motor: "))

if temp < 40:
    print("Baixa carga")

elif temp >= 70:
    print("ALERTA: Resfriamento Ativado!")

else:
    print("Normal")