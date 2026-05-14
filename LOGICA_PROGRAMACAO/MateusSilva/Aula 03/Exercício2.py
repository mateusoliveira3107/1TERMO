print("\n  Questionário")

nome = (input("Qual é o seu nome? "))
ano = int(input("que ano você nasceu? "))
curso = input("Qual é o seu curso?")
ano2 = int(input("que ano você está? "))

idade = int(ano2) - ano
idade2 = int(ano2 - 1) - ano

print ("\nSeu nome é", nome, "você está cursando", curso, "e você tem", idade2, "ou",idade, "anos de idade")

