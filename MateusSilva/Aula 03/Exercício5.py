print("\n     --Venda de livros--")

preço = float(input("Digite o valor do livro: "))
desconto = (preço/20)

total = preço - desconto

print("\nO preço total do livro é de", total, ", considerando desconto de 5%")