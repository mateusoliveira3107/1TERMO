# # Tratamento de erros com python
# # Erros comuns:
# # - ZeroDivisionError: divisão por zero
# # - ValueError: conversão de tipo inválida
# # - IndexError: acesso a índice fora do limite
# # - KeyError: acesso a chave inexistente em dicionário

# print("Exemplo de tratamento de erros")

# try:
#     num1 = int(input("Digite o primeiro número... "))
#     num2 = int(input("Digite o segundo número... "))
#     resultado = num1/num2
#     print(f"O resultado da divisão é: {resultado:.2f}")

# except ZeroDivisionError:
#         print("Erro: Não é possível dividir por zero.")

# except ValueError:
#         print("Erro: Entrada inváida. Por favor, digite um número inteiro")

# # except Exception as e:
# #     print(f"Ocorreu um erro inesperado: {e}")

# except NameError:
#       print("Erro: Variável não definida.")

# if num1 > 100:
#     print("O número digitado é maior que 100.")
#     for i in range(1, 6):
#           print(f"{num1} x {i} = {num1 * i}")
#           if num1 * i > 1000:
#                 print("O resultado da multiplicação é maior que 1000.")
#                 try:
#                       pass
#                 except Exception as e:
#                       print(f"Ocorreu um erro inesperado: {e}")

# else:
#       print(f"O número digitado é menor ou igual a 100.")

# Exercício 1
# Escreva um programa que solicite ao usuário um número inteiro e calcule a média de uma lista de números. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número inteiro.
# lista = 0

# print("=-=-=-="*10)
# print("Descubra a média entre 5 números!")
# print("=-=-=-="*10)
# for i in range(5):
#     try:
#         num = int(input("Digite um número inteiro: "))
#         lista += num
#     except ValueError:
#         print("Erro: Digite um valor inteiro")
#         num = int(input("Digite um número inteiro: "))
#         lista += num

# print(f"Média: {lista/5}")

# Exercício 2

# Escreva um programa que solicita ao usuário uma lista de palavras e conte quantas vezes cada palavra aparece na lista. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja uma string

# print("Conta palavras")

# print("Palavras:")


# try:
#     frase = input("Digite uma lista de palavras para adicionar à lista: ").split()
#     contagem = {}
#     for palavra in frase:
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1
        
#         print("Contagem de palavras")
#         for palavra, contagem in contagem.itens():
#             print(f"{palavra}: {contagem}")
        


# try:
#     palavras = input("Digite uma lista de palavras separadas por espaço... ").split()
#     contagem = {}
#     for palavra in palavras:
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1
#         print("Contagem de palavras:")
#         for palavra, contagem in contagem.itens():
#             print(f"{palavra}: {contagem}")
# except ValueError:
#     print("Erro: Entrada inválida. Por Favor, digite uma lista de palavras separadas por espaço.")



# Exercício 3: Escrever um programa mais simples com testes de tratameno de erros, como por exemplo, solicitar ao usuário um número. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número
# - ZeroDivisionError - se o usuário digitar zero como divisor

print("Divisão")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1/num2
    print(f"O resultado da divisão é: {resultado:.2}")

except ValueError:
      print("Erro: Você digitou um valor que não é um número")

except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
