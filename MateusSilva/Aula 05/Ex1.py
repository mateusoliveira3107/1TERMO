# 1. O laço 'for' (Repetições determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças)
# Exemplo: Relatório de produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
# for lote in range(1,6):
#     print(f"Processando lote numero {lote}...")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada")

# Imagine que você queira armazenar 10 carros
# for carros in range(10):
#     print(f"Quantidade de carros: {carros}")

# Exemplo 2
# Contar até 4
# for i in range(5):
#     print(i)

# Exemplo 3
pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso"]
maquinas = ["Máquina 1", "Máquina 2"]

for item in pecas:
    print(f"Item em estoque: {item}")
    for maq in maquinas:
        print(f"Máquinas que temos {maq}")