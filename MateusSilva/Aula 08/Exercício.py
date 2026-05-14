import os

# Exercício 1
# print(os.getcwd())

# Exercício 2
# print(os.listdir())

# Exercício 3
# os.mkdir("projetos")
# os.rename("projetos", "meus_projetos")
# os.rmdir("meus_projetos")

# Exercício 4
# with open("log.txt", "w") as arquivo:
#     arquivo.write("Log de atividades")

# with open("log.txt", "r") as arquivo:
#     texto = arquivo.read()
#     print(texto)

# Exemplo de dicionário

# Pessoa 1

# pessoa = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Paulo",
#     "profissão": "Engenheira"
# }
# print(pessoa["nome"])
# print(f"idade:", pessoa["idade"])
# print(f"cidade:", pessoa["cidade"])
# print(f"profissão:", pessoa["profissão"])

# Pessoa 2

# pessoa2 = {
#     "nome": "Mateus",
#     "idade": 16,
#     "cidade": "Limeira",
#     "profissão": "Nenhuma"
# }
# print("\n")
# print(pessoa2["nome"])
# print(f"idade:", pessoa2["idade"])
# print(f"cidade:", pessoa2["cidade"])
# print(f"profissão:", pessoa2["profissão"])

# with open("desliga.bat", "w") as desligar:
#     desligar.write("shutdown -s -t 3600 -c \"Desligamento programado para daqui a 1 hora. Salva seu trabalho!\"")
#     # -s comando para desligar
#     # -t tempo definir
#     # -a cancelar desligamento

# with open("desliga.bat", "r") as desligar:
#     conteudo = desligar.read()
#     print(conteudo)

# Exercício 7

# with open("notas.txt", "r") as notas:
#     conteudo = notas.read()
# with open("notas_backup.txt", "w") as backup:
#     backup.write(conteudo)
#     print("Backup realizado com sucesso!")

# Exemplo 2
# pasta = os.listdir()
# for arquivo in pasta:
#     if arquivo.endswith (".txt"):
#          os.remove(arquivo)     # remove irá apagar o arquivo do sistema
#          print(f"Arquivo {arquivo} excluido")

# print("Limpeza de arquivos concluída.")

# Exercício 8

with open("temperatura.txt", "w") as temp:
    conteudo = temp.write("80")

with open ("temperatura.txt", "r") as temp:
    conteudo2 = int(temp.read())

if conteudo2 > 70:
    print("Aviso! Temperatura acima de 70°")
