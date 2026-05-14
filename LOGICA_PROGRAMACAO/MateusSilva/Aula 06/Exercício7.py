# Exercício 7
# Crie um programa que receba dois dados: a pressão atual (float) e as horas de uso acumuladas (int) de uma turbina
# O programa deve classificar o estado da máquina seguindo esta hierarquia:
# Crítico (Prioridade 1): Se a pressão for maior que 100 ou as horas de uso forem maiores que 10.000.
# Mensagem: "PARADA IMEDIATA: Risco de falha catastrófica"
# Alerta (Prioridade 2): Se a pressão estiver entre 80 e 100 (inclusive).
# Mensagem: "MANUTENÇÃO AGENDADA: Pressão acima do ideal."
# Monitoramento (Prioridade 3): Se as horas de uso forem entre 8.000 e 10.000
# Mensagem: "AVISO: Máquina aproximando-se da revisão de 10k horas."
# Normal: Para qualquer outro caso que não se encaixe nos acima
# Mensagem: "SISTEMA OPERAL: Todos os parâmetros dentro da normalidade."

pressao = float(input("Pressão atual: "))
horas = int(input("Horas acumuladas: "))

if pressao > 100 and horas > 10000:
    print("PARADA IMEDIATA: Risco de falha catastrófica")

if pressao > 80:
    print("PARADA IMEDIATA: Risco de falha catastrófica")

elif pressao < 100:
    print("MANUTENÇÃO AGENDADA: Pressão acima do ideal")

if horas > 8000:
    print("AVISO: Máquina aproximando-se da revisão de 10k horas.")

elif horas < 10000:
    print("AVISO: Máquina aproximando-se da revisão de 10k horas.")

else:
    print("SISTEMA OPERAL: Todos os parâmetros dentro da normalidade.")