# Exercício 1
# Calculo de notas por semestre onde terá duas notas formativas e uma nota somativa para encerrar o semestre
# Os valores de notas são de 0 a 100

    # -- Seimeiro Semestre --

print("\n  --- Média de notas primeiro semestre ---")

formativa1 = float(input("\nDigite sua nota da primeira prova formativa: "))
formativa2 = float(input("Digite sua nota da segunda prova formativa: "))
somativa = float(input("Digite sua nota da terceira prova formativa: "))

result = (formativa1 + formativa2 + somativa)/3

  # -- Segundo Semestre --

print("\n  -- Média de notas segundo semestre --")

formativa4 = float(input("\nDigite sua sua nota da primeira prova formativa do segundo semestre: "))
formativa5 = float(input("Digite sua nota da segunda prova formativa do segundo semestre: "))
somativa2 = float(input("Digite sua nota da prova somativa do segundo semestre: "))

result2 = (formativa4 + formativa5 + somativa2)/3

print("\n --- Notas do Ano ---")

print("\nSua nota Nota final do primeiro semestre é: ", result)
print("\nSua nota Nota final do segundo semestre é: ", result2)

round(result, 2)
round(result2, 2)
