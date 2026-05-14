# Exemplo 1

# Lista de temperaturas lidas pelo sensor por minuto

# leituras = [70, 75, 82, 98, 110, 85, 80]

# for temperatura in leituras:
#     if temperatura > 100:
#         print(f"CRÍTICO: {temperatura} C° detectado! Adicionando parada de emergência.")
#         break # O loop para aqui e NÃO lê os próximos valores (85 e 80)

# print(f"Temperatura está em {temperatura} C°. Operação normal.")

# print("Sistema desligado. Aguardando manuteção.")

# Exemplo 2

materiais = ["metal", "metal", "plástico", "metal", "vidro", "metal"]
for peca in materiais:
    if peca != "metal":
        print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
        continue # Pula o restante do código abaixo e vai para a próxima peça

    # Este código só roda se a peça for de metal
    print(f"Processando a peça de {peca}. Furando e polindo")

print("Fim do lote de produção")
