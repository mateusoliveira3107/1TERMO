import tkinter as tk
from tkinter import messagebox
import time
import os

META_PONTOS = 50
TEMPO_MINIMO = 0.08
pontos_j1 = 0
pontos_j2 = 0
jogo_ativo = False
tecla_a_pressionada = False
tecla_l_pressionada = False
ultimo_clique_j1 = 0
ultimo_clique_j2 = 0

def atualizar_interface():
    label_j1.config(text=f"Jogador 1 [A]\n\n{pontos_j1} / {META_PONTOS}")
    label_j2.config(text=f"Jogador 2 [L]\n\n{pontos_j2} / {META_PONTOS}")

    altura_barra_j1 = int((pontos_j1 / META_PONTOS) * 300)
    altura_barra_j2 = int((pontos_j2 / META_PONTOS) * 300)

    barra_progresso_j1.place_configure(height=altura_barra_j1)
    barra_progresso_j2.place_configure(height=altura_barra_j2)

def clicar_iniciar():
    botao_iniciar.place_forget()
    botao_fechar.place_forget()
    iniciar_contagem(3)

def iniciar_contagem(contador):
    global jogo_ativo
    cores = {3: "#FF5555", 2: "#FFCC00", 1: "#55FFB8"}
   
    label_sombra.place(x=459, y=324, width=90, height=120)
    label_contagem.place(x=455, y=320, width=90, height=120)
   
    if contador > 0:
        label_sombra.config(text=str(contador))
        label_contagem.config(text=str(contador), fg=cores[contador])
        janela.after(1000, iniciar_contagem, contador - 1)
    else:
        label_sombra.config(text="JÁ!")
        label_contagem.config(text="JÁ!", fg="#24B424")
        jogo_ativo = True
        janela.after(1000, sumir_contagem)

def sumir_contagem():
    label_contagem.place_forget()
    label_sombra.place_forget()

def contar_j1(event):
    global pontos_j1, jogo_ativo, tecla_a_pressionada, ultimo_clique_j1
    if not jogo_ativo or tecla_a_pressionada:
        return

    tecla_a_pressionada = True
    agora = time.time()

    if agora - ultimo_clique_j1 < TEMPO_MINIMO:
        return

    ultimo_clique_j1 = agora
    pontos_j1 += 1

    atualizar_interface()
    verificar_vitoria()

def contar_j2(event):
    global pontos_j2, jogo_ativo, tecla_l_pressionada, ultimo_clique_j2
    if not jogo_ativo or tecla_l_pressionada:
        return

    tecla_l_pressionada = True
    agora = time.time()

    if agora - ultimo_clique_j2 < TEMPO_MINIMO:
        return

    ultimo_clique_j2 = agora
    pontos_j2 += 1

    atualizar_interface()
    verificar_vitoria()

def soltar_a(event):
    global tecla_a_pressionada
    tecla_a_pressionada = False

def soltar_l(event):
    global tecla_l_pressionada
    tecla_l_pressionada = False

def verificar_vitoria():
    global jogo_ativo

    if pontos_j1 >= META_PONTOS:
        jogo_ativo = False
        messagebox.showinfo("🏆 FIM DE JOGO", "O JOGADOR 1 (TECLA A) É O CAMPEÃO!")
        reiniciar()
    elif pontos_j2 >= META_PONTOS:
        jogo_ativo = False
        messagebox.showinfo("🏆 FIM DE JOGO", "O JOGADOR 2 (TECLA L) É O CAMPEÃO!")
        reiniciar()

def reiniciar():
    global pontos_j1, pontos_j2, jogo_ativo

    pontos_j1 = 0
    pontos_j2 = 0
    jogo_ativo = False

    atualizar_interface()

    botao_iniciar.place(x=375, y=280, width=250, height=90)
    botao_fechar.place(x=375, y=380, width=250, height=60)

janela = tk.Tk()
janela.title("Super Clicker Arena - 2 Jogadores")
janela.geometry("1000x700")
janela.configure(bg="#111111")

label_titulo = tk.Label(janela, text="CLIQUE!\nQUEM CHEGAR EM 50 PRIMEIRO VENCE", font=("Minecraft", 26, "bold"), bg="#111111", fg="#FFFFFF")
label_titulo.pack(pady=40)

frame_j1 = tk.Frame(janela, bg="#222222", bd=5, relief="ridge")
frame_j1.place(x=100, y=180, width=350, height=450)

label_j1 = tk.Label(frame_j1, text=f"Jogador 1 [A]\n\n0 / {META_PONTOS}",  font=("Minecraft", 22), bg="#222222", fg="#FF5555")
label_j1.pack(pady=20)

fundo_barra_j1 = tk.Frame(frame_j1, bg="#442222", width=40, height=300)
fundo_barra_j1.pack(side="bottom", pady=20)

barra_progresso_j1 = tk.Frame(fundo_barra_j1, bg="#FF5555", width=40, height=0)
barra_progresso_j1.place(x=0, y=300, anchor="sw")

frame_j2 = tk.Frame(janela, bg="#222222", bd=5, relief="ridge")
frame_j2.place(x=550, y=180, width=350, height=450)

label_j2 = tk.Label(frame_j2, text=f"Jogador 2 [L]\n\n0 / {META_PONTOS}", font=("Minecraft", 22), bg="#222222", fg="#55FFFF")
label_j2.pack(pady=20)

fundo_barra_j2 = tk.Frame(frame_j2, bg="#224444", width=40, height=300)
fundo_barra_j2.pack(side="bottom", pady=20)

barra_progresso_j2 = tk.Frame(fundo_barra_j2, bg="#55FFFF", width=40, height=0)
barra_progresso_j2.place(x=0, y=300, anchor="sw")

label_sombra = tk.Label(janela, font=("Impact", 52), bg="#111111", fg="#333333")
label_contagem = tk.Label(janela, font=("Impact", 52), bg="#111111")

botao_iniciar = tk.Button(janela, text="INICIAR JOGO", font=("Courier", 20, "bold"), bg="#1CC438", fg="#FFFFFF",
    activebackground="#0C7C35", activeforeground="#FFFFFF", bd=4, relief="raised", cursor="hand2", command=clicar_iniciar)
botao_iniciar.place(x=375, y=280, width=250, height=80)

botao_fechar = tk.Button(janela, text="FECHAR", font=("Courier", 16, "bold"), bg="#8B0000", fg="#FFFFFF", 
                         activebackground="#5A0000", activeforeground="#FFFFFF", bd=4, relief="raised", cursor="hand2", command=lambda: [janela.destroy(), os.system("python 1TERMO\LOGICA_PROGRAMACAO\Projetos_Python\Projetos\MENU.py")])
botao_fechar.place(x=375, y=380, width=250, height=60)

janela.bind("<KeyPress-a>", contar_j1)
janela.bind("<KeyPress-A>", contar_j1)
janela.bind("<KeyRelease-a>", soltar_a)
janela.bind("<KeyRelease-A>", soltar_a)

janela.bind("<KeyPress-l>", contar_j2)
janela.bind("<KeyPress-L>", contar_j2)
janela.bind("<KeyRelease-l>", soltar_l)
janela.bind("<KeyRelease-L>", soltar_l)

atualizar_interface()
janela.mainloop()