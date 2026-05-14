# exemplo 1
# def saudacao(nome):
#     return f"Olá, {nome}!"

# mensagem = saudacao("Mateus")
# print(mensagem)

# exemplo 2
# nome = input("Seu nome: ")
# idade = int(input("Sua idade: "))

# print(f"{nome} tem {idade} anos")

# exemplo 3
# def boas_vindas(nome, cargo):
#     print(f"Olá, {nome}! Você é o novo {cargo}.")

# boas_vindas("Ana", "Desenvolvedora")
# boas_vindas("Carlos", "Gerente")

# exemplo 4
def configurar_conexao(servidor, porta=8080):
    print(f"Conectando a (servidor) na porta (porta)...")

configurar_conexao("192.168.1.1")        # Usa a porta 8080
configurar_conexao("10.0.0.1", 3000)     # Usa a porta 3000
configurar_conexao("192.168.1.2")
configurar_conexao("10.0.0.2", 3001)
