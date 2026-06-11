# ---------- Exercício 1 ----------
# 1 Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Registro de Operador")
# janela.geometry("500x300")
# janela.configure(bg="#3E56A3")

# def registrar_operador():
#     nome = nome_entry.get()
#     turno = turno_entry.get()
#     messagebox.showinfo("Bem-Vindo", f"Olá {nome}, Você foi registrado no turno {turno}")

# lbl_nome = tk.Label(janela, text= "Digite seu nome", font=("Arial", 14), fg="#000000")
# lbl_nome.grid(row=0, column=1, pady=10, padx=10)
# nome_entry = tk.Entry(janela, width=30)
# nome_entry.grid(row=0, column=2, pady=10, padx=10)

# lbl_turno = tk.Label(janela,text="Digite seu turno [A, B ou C]")
# lbl_turno.grid(row=1, column=1, pady=10, padx=10)
# turno_entry = tk.Entry(janela, width=30)
# turno_entry.grid(row=1, column=2, pady=10, padx=10)

# botao_registrar = tk.Button(janela, text="Registrar", font=("Arial", 14), bg="#18AF04",fg="#000000", command=registrar_operador)
# botao_registrar.grid(row=2, column=2, pady=10, padx=10)
# botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#740303", fg="#000000", command=janela.destroy)
# botao_fechar.grid(row=2, column=3, pady=10, padx=10)

# janela.mainloop()


# ---------- Exercício 2 ----------
# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Calculo de produção")
# janela.geometry("400x400")
# janela.configure(bg="#3E56A3")

# def calcular():
#     pecas_produzidas = int(numero_entry.get())
#     if pecas_produzidas <= 0:
#         messagebox.showerror("Erro", "Digite um valor válido")
#     else:
#         pecas_total = int(pecas_produzidas * 8)
#         messagebox.showinfo("Produção", f"Serão produzidas {pecas_total} em um turno de 8 horas")


# lbl_numero = tk.Label(janela, text= "Digite a quantidade de peças produzidas em 1 hora", font=("Arial", 12), fg="#000000")
# lbl_numero.grid(row=0, column=0, pady=10, padx=10)
# numero_entry = tk.Entry(janela, width=30, font=("Arial", 12), fg="#000000")
# numero_entry.grid(row=1, column=0, pady=10, padx=10)

# botao_calculo = tk.Button(janela, text="Calcular", font=("Arial", 14), bg= "#077A33", fg="#000000", command=calcular)
# botao_calculo.grid(row=2, column=0, pady=10, padx=10)
# botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#740303", fg="#000000", command=janela.destroy)
# botao_fechar.grid(row=3, column=0, pady=10, padx=10)

# janela.mainloop()


# ---------- Exercício 3 ----------
# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Conversão para PSI")
# janela.geometry("400x400")
# janela.configure(bg="#3E56A3")

# def converter():
#     try:
#         pressao_bar = float(pressao_entry.get())
#         if pressao_bar <= 0:
#             messagebox.showerror("Erro", "Digite um valor acima de 0")
#         else:
#             psi = float(pressao_bar * 14.5)
#             messagebox.showinfo("Conversão de unidade", f"{pressao_bar} Bar em PSI é igual a {psi}")
#     except ValueError:
#         messagebox.showerror("Erro", "Digite um valor válido")


# lbl_pressao = tk.Label(janela, text= "Digite a pressão em Bar", font=("Arial", 12), fg="#000000")
# lbl_pressao.grid(row=0, column=0, pady=10, padx=60)
# pressao_entry = tk.Entry(janela, width=30, font=("Arial", 12), fg="#000000")
# pressao_entry.grid(row=1, column=0, pady=10, padx=60)

# botao_converter = tk.Button(janela, text="Calcular", font=("Arial", 14), bg= "#077A33", fg="#000000", command=converter)
# botao_converter.grid(row=2, column=0, pady=10, padx=60)
# botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#740303", fg="#000000", command=janela.destroy)
# botao_fechar.grid(row=3, column=0, pady=10, padx=60)

# janela.mainloop()


# ---------- Exercício 4 ----------
# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Média de qualidade")
# janela.geometry("400x400")
# janela.configure(bg="#3E56A3")

# def calcular():
#     try:
#         n1 = float(num1_entry.get())
#         n2 = float(num2_entry.get())
#         n3 = float(num3_entry.get())

#         if n1 == "" and n2 == "" and n3 == "":
#             messagebox.showwarning("Erro", "Digite um valor acima de 0")
#         else:
#             media = (n1+n2+n3)/3
#             messagebox.showinfo("Média de qualidade", f"A média de inspeção dessas peças é de {media}")
#     except ValueError:
#         messagebox.showerror("Erro", "Digite um valor válido")

# lbl_num1 = tk.Label(janela, text= "Digite a nota da primeira peça", font=("Arial", 12), fg="#000000")
# lbl_num1.grid(row=0, column=0, pady=5, padx=60)
# num1_entry = tk.Entry(janela, width=30, font=("Arial", 12), fg="#000000")
# num1_entry.grid(row=1, column=0, pady=5, padx=60)

# lbl_num2 = tk.Label(janela, text= "Digite a nota da serceira peça", font=("Arial", 12), fg="#000000")
# lbl_num2.grid(row=2, column=0, pady=5, padx=60)
# num2_entry = tk.Entry(janela, width=30, font=("Arial", 12), fg="#000000")
# num2_entry.grid(row=3, column=0, pady=5, padx=60)

# lbl_num3 = tk.Label(janela, text= "Digite a nota da terceira peça", font=("Arial", 12), fg="#000000")
# lbl_num3.grid(row=4, column=0, pady=5, padx=60)
# num3_entry = tk.Entry(janela, width=30, font=("Arial", 12), fg="#000000")
# num3_entry.grid(row=5, column=0, pady=5, padx=60)


# botao_calculo = tk.Button(janela, text="Calcular", font=("Arial", 14), bg= "#0A8539", fg="#000000", command=calcular)
# botao_calculo.grid(row=7, column=0, pady=20, padx=60)
# botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 14), bg="#7E0505", fg="#000000", command=janela.destroy)
# botao_fechar.grid(row=8, column=0, pady=5, padx=60)

# janela.mainloop()


# ---------- Exercício 5 ----------
# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Média de qualidade")
# janela.geometry("450x350")
# janela.configure(bg="#3E56A3")

# def medir():
#     try:
#         temperatura = float(temperatura_entry.get())
#         if temperatura < 40:
#             messagebox.showinfo("Notificação de temperatura", "Baixa carga")
#         elif temperatura > 70:
#             messagebox.showwarning("Notificação de temperatura", "ALERTA: Resfriamento Ativado!")
#         else:
#             messagebox.showinfo("Notificação de temperatura", "Normal")
#     except ValueError:
#         messagebox.showerror("Erro", "Digite um valor válido")

# lbl_temperatura = tk.Label(janela, text= "Digite a temperatura do motor", font=("Arial", 14), fg="#000000")
# lbl_temperatura.grid(row=0, column=0, pady=5, padx=60)
# temperatura_entry = tk.Entry(janela, width=30, font=("Arial", 14), fg="#000000")
# temperatura_entry.grid(row=1, column=0, pady=5, padx=60)

# botao_calcular = tk.Button(janela, text="Calcular", font=("Arial", 16), bg= "#0A8539", fg="#000000", command=medir)
# botao_calcular.grid(row=7, column=0, pady=20, padx=60)
# botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 16), bg="#7E0505", fg="#000000", command=janela.destroy)
# botao_fechar.grid(row=8, column=0, pady=5, padx=60)

# janela.mainloop()


# ---------- Exercício 6 ----------
# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("490x350")
# janela.configure(bg="#475CA0")

# def classificar():
#         lote = lote_entry.get()
#         primeira_letra = lote[0]
#         if primeira_letra == "a":
#             messagebox.showinfo("Notificação de lote", "Alimentos")
#         elif primeira_letra == "A":
#             messagebox.showinfo("Notificação de lote", "Alimentos")
#         elif primeira_letra == "e":
#             messagebox.showwarning("Notificação de lote", "Eletrônicos")
#         elif primeira_letra == "E":
#             messagebox.showwarning("Notificação de lote", "Eletrônicos")
#         else:
#             messagebox.showwarning("Erro", "Desconhecido")


# lbl_lote = tk.Label(janela, text= "Insira o código do produto [Alimentos/Eletrônicos]", font=("Arial", 14), fg="#000000")
# lbl_lote.grid(row=0, column=0, pady=20, padx=30)
# lote_entry = tk.Entry(janela, width=30, font=("Arial", 14), fg="#000000")
# lote_entry.grid(row=1, column=0, pady=5, padx=30)

# botao_verificar = tk.Button(janela, text="Verificar", font=("Arial", 16), bg= "#11863E", fg="#000000", command=classificar)
# botao_verificar.grid(row=6, column=0, pady=10, padx=30)
# botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 16), bg="#860D0D", fg="#000000", command=janela.destroy)
# botao_fechar.grid(row=7, column=0, pady=10, padx=30)

# janela.mainloop()


# ---------- Exercício 7 ----------
# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# import tkinter as tk
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("450x400")
# janela.configure(bg="#6075BB")

# def verificar_maquina():
#         porta = str(sensor_porta_entry.get())
#         primeira_letra_porta = porta[0]
#         botao = str(botao_emergencia_entry.get())
#         primeira_letra_botao = botao[0]

#         if primeira_letra_porta == "a" and True:
#             if primeira_letra_botao == "l" and True:
#                 messagebox.showwarning("Aviso", "A máquina não pode iniciar.\nA porta está aberta e o botão de emergência está ligado")
#             else:
#                 messagebox.showwarning("Aviso", "A máquina não pode iniciar.\nA porta está aberta")
#         elif primeira_letra_botao == "l" and True:
#             messagebox.showwarning("Aviso", "A máquina não pode iniciar.\nO botão de emergência está ligado")
#         else:
#             messagebox.showinfo("Aviso", "A máquina pode iniciar!")

# lbl_sensor_porta = tk.Label(janela, text= "Informe o estado da porta\n[Aberta/Fechada]", bg="#6075BB",font=("Arial", 15), fg="#000000")
# lbl_sensor_porta.grid(row=0, column=0, pady=10, padx=30)
# sensor_porta_entry = tk.Entry(janela, width=30, font=("Arial", 14), fg="#000000")
# sensor_porta_entry.grid(row=1, column=0, pady=5, padx=30)

# lbl_botao_emergencia = tk.Label(janela, text= "Informe o estado do botão de emergencia\n[Ligado/Desligado]", bg="#6075BB", font=("Arial", 15), fg="#000000")
# lbl_botao_emergencia.grid(row=2, column=0, pady=10, padx=30)
# botao_emergencia_entry = tk.Entry(janela, width=30, font=("Arial", 14), fg="#000000")
# botao_emergencia_entry.grid(row=3, column=0, pady=5, padx=30)

# botao_verificar = tk.Button(janela, text="Verificar", font=("Arial", 16), bg= "#11863E", fg="#000000", command=verificar_maquina)
# botao_verificar.grid(row=6, column=0, pady=10, padx=30)
# botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 16), bg="#860D0D", fg="#000000", command=janela.destroy)
# botao_fechar.grid(row=7, column=0, pady=10, padx=30)

# janela.mainloop()


# ---------- Exercício 8 ----------
# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# import tkinter as tk
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("400x400")
# janela.configure(bg="#6075BB")

# def verificar_pecas():
#         pecas_total = int(pecas_produzidas_entry.get())
#         pecas_defeituosas = int(pecas_defeituosas_entry.get())
#         porcentagem = (pecas_defeituosas/pecas_total)*100
#         if porcentagem > 5:
#             messagebox.showwarning("Aviso", "Revisar Processo")
#         else:
#             messagebox.showinfo("Aviso", "Processo Otimizado")

# lbl_pecas_produzidas = tk.Label(janela, text= "Informe o total de peças produzidas", bg="#6075BB",font=("Arial", 15), fg="#000000")
# lbl_pecas_produzidas.grid(row=0, column=0, pady=10, padx=30)
# pecas_produzidas_entry = tk.Entry(janela, width=30, font=("Arial", 14), fg="#000000")
# pecas_produzidas_entry.grid(row=1, column=0, pady=5, padx=30)

# lbl_pecas_defeituosas = tk.Label(janela, text= "Informe o total de peças defeituosas", bg="#6075BB", font=("Arial", 15), fg="#000000")
# lbl_pecas_defeituosas.grid(row=2, column=0, pady=10, padx=30)
# pecas_defeituosas_entry = tk.Entry(janela, width=30, font=("Arial", 14), fg="#000000")
# pecas_defeituosas_entry.grid(row=3, column=0, pady=5, padx=30)

# botao_calculo = tk.Button(janela, text="Calcular", font=("Arial", 16), bg= "#148D43", fg="#000000", command=verificar_pecas)
# botao_calculo.grid(row=6, column=0, pady=10, padx=30)
# botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 16), bg="#811111", fg="#000000", command=janela.destroy)
# botao_fechar.grid(row=7, column=0, pady=10, padx=30)

# janela.mainloop()


# ---------- Exercício 9 ----------
# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

# import tkinter as tk
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("400x350")
# janela.configure(bg="#4C87AF")

# medida_minima = 9.8
# medida_maxima = 10.2

# def validar_medida():
#     medida = float(medida_peca_entry.get())
#     if medida < medida_minima:
#         messagebox.showwarning("Aviso", "A medida da peça está abaixo da tolerância")
#     elif medida > medida_maxima:
#         messagebox.showwarning("Aviso", "A medida da peça está acima da tolerância")
#     else:
#         messagebox.showinfo("Aviso", "A medida da peça está dentro da tolerância")

# lbl_medida_peca = tk.Label(janela, text= "Informe a medida da peça em mm", bg="#4C87AF",font=("Arial", 16), fg="#000000")
# lbl_medida_peca.grid(row=0, column=0, pady=10, padx=30)
# medida_peca_entry = tk.Entry(janela, width=30, font=("Arial", 14), fg="#000000")
# medida_peca_entry.grid(row=1, column=0, pady=5, padx=30)

# botao_calcular = tk.Button(janela, text="Calcular", font=("Arial", 15), bg= "#148D43", fg="#000000", command=validar_medida)
# botao_calcular.grid(row=6, column=0, pady=10, padx=30)
# botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 15), bg="#811111", fg="#000000", command=janela.destroy)
# botao_fechar.grid(row=7, column=0, pady=10, padx=30)

# janela.mainloop()


# ---------- Exercício 10 ----------
# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# import tkinter as tk
# from time import sleep
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Contagem regressiva")
# janela.geometry("380x350")
# janela.configure(bg="#728A07")

# def iniciar():
#     numero = 10
#     while numero != 0:
#         messagebox.showinfo("Contagem", f"{numero}!")
#         numero -= 1
#     messagebox.showinfo("Aviso", "Prensa Ativada!")

# botao_iniciar = tk.Button(janela, text=" Iniciar contagem ", font=("Arial", 18), bg= "#148D43", fg="#000000", command=iniciar)
# botao_iniciar.grid(row=0, column=0, pady=10, padx=80)
# botao_fechar = tk.Button(janela, text=" Fechar ", font=("Arial", 16), bg="#811111", fg="#000000", command=janela.destroy)
# botao_fechar.grid(row=1, column=0, pady=10, padx=80)

# janela.mainloop()


# ---------- Exercício 11 ----------
# 11.Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.

# janela.mainloop()

# import tkinter as tk
# from time import sleep
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Calculadora de Produção")
# janela.geometry("400x250")
# janela.configure(bg="#3564AA")

# peso_total = 0

# def adicionar_caixa():
#     global peso_total
#     peso = float(entrada_peso.get())
#     if peso == 0:
#         messagebox.showinfo("Calculadora de produção", f"Peso total acumulado: {peso_total}")
#         peso_total = 0
#     else:
#         peso_total += peso

#     entrada_peso.delete(0, tk.END)

# lbl_peso_caixa = tk.Label(janela, text="Digite o peso da caixa (kg):", font=("Arial", 16), bg= "#4479A3", fg="#000000")
# lbl_peso_caixa.grid(row=1, column=0, pady=10, padx=80)

# entrada_peso = tk.Entry(janela, width=15, font=("Arial", 14), bg= "#4479A3", fg="#000000")
# entrada_peso.grid(row=2, column=0, pady=10, padx=80)

# botao_adicionar = tk.Button(janela, text="Adicionar", font=("Arial", 16), bg= "#4479A3", fg="#000000", command=adicionar_caixa)
# botao_adicionar.grid(row=3, column=0, pady=10, padx=80)

# janela.mainloop()