import tkinter as tk
from PIL import Image, ImageTk
from time import sleep
import os

def menu():
    janela = tk.Tk()
    janela.title("inicio")
    janela.geometry("1000x700")

    imagem_original2 = Image.open(r"1TERMO\LOGICA_PROGRAMACAO\Projetos_Python\Projetos\imagens\200a002dad331dc9d5027bc45cf03f1d.png")
    imagem_redimensionada2 = imagem_original2.resize((1000, 700))
    imagem_fundo2 = ImageTk.PhotoImage(imagem_redimensionada2)

    label_fundo2 = tk.Label(janela, image=imagem_fundo2, bd=0)
    label_fundo2.place(x=0, y=0, relwidth=1, relheight=1)
    label_fundo2.image = imagem_fundo2

    tk.Label(janela, text=" Menu ", bg="#77C3D4", font=("Minecraft", 48)).place(x = 400, y = 100)
    
    def abrir_jornadadoheroi():
        janela.destroy()
        os.system("python 1TERMO\LOGICA_PROGRAMACAO\Projetos_Python\Projetos\jornadadoheroi.py")
    
    def abrir_superclicker():
        janela.destroy()
        os.system("python 1TERMO\LOGICA_PROGRAMACAO\Projetos_Python\Projetos\superclicker.py")

    tk.Button(janela, text="    Jornada do Heroi    ", bg="#D10B0B", font=("Minecraft", 30), command=abrir_jornadadoheroi).place(x = 280, y = 300)
    tk.Button(janela, text="      SuperClicker      ", bg="#10BB00", font=("Minecraft", 30), command=abrir_superclicker).place(x = 290, y = 430)
    tk.Button(janela, text="FECHAR", bg="#D10B0B", font=("Minecraft", 16), command=janela.destroy).place(x = 850, y = 20)

    janela.mainloop()

menu()