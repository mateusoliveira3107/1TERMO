# Laço while (repetições indeterminadas)
# Use o while quando voc~e não sabe quando vai parar. Ele depende de uma condição (como um sensor da segurança ou um botão de emergência)
# import time
# temperatura = 25 # Início
# # Repete enquanto temperatura estiver segura

# while temperatura < 40:
#     print(f"Temperatura atual: {temperatura}C°. Sistema operando....")
#     time.sleep('0.5')
#     temperatura += 3 # Simulando o aquecimento da máquina
# print("\nALERTA! Temperatura atingiu o limite. Desligando motor...")

# Exemplo: menu de interação
opcao = ""

while opcao != "sair":
    opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").lower()
    if opcao != "sair":
        print(f"Dado '{opcao}' registrado no banco de dados")
print("Sistema encerrado")
