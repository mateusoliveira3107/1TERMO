print("Relatório de Truno Completo")
total_pecas = 5
pecas_aprovadas = 0
for i in range(1, total_pecas + 1):
    diametro = float(input(f"Digite o diâmetro da peça {i} em mm... "))
    if 19.9 <= diametro <= 20.1:
        pecas_aprovadas += 1

eficiencia = (pecas_aprovadas / total_pecas) * 100
print(f"Total de peças aprovadas: {pecas_aprovadas}")
print(f"Eficiência do lote: {eficiencia:.2f}%")