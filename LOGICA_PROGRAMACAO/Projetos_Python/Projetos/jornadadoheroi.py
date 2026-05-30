import time
import os
import random

posicao_defesa = False

pocoes = 2
apagadores = 1


def orc():
    print("\033[38;2;255;165;0m╔════════════════════════════╗  \033[0m")
    print("\033[38;2;255;165;0m║\033[0m\033[92m          ,      ,          \033[0m\033[38;2;255;165;0m║\033[0m  ")
    print("\033[38;2;255;165;0m║\033[0m\033[92m         /(.-''-.)\\         \033[0m\033[38;2;255;165;0m║  \033[0m")
    print("\033[38;2;255;165;0m║\033[0m\033[92m     |\\  \\/      \\/  /|     \033[0m\033[38;2;255;165;0m║  \033[0m")
    print("\033[38;2;255;165;0m║\033[0m\033[92m     | \\ /  \\  /  \\ / |     \033[0m\033[38;2;255;165;0m║  \033[0m")
    print("\033[38;2;255;165;0m║\033[0m\033[92m     \\( \\   o\\/o   / )/     \033[0m\033[38;2;255;165;0m║  \033[0m")
    print("\033[38;2;255;165;0m║\033[0m\033[92m      \\_, '-/  \\-' ,_/      \033[0m\033[38;2;255;165;0m║  \033[0m")
    print("\033[38;2;255;165;0m║\033[0m\033[92m        /   \\__/   \\        \033[0m\033[38;2;255;165;0m║  \033[0m")
    print("\033[38;2;255;165;0m║\033[0m\033[92m        \\ \\__/\\__/ /        \033[0m\033[38;2;255;165;0m║  \033[0m")
    print("\033[38;2;255;165;0m║\033[0m\033[92m      ___\\ \\|--|/ /___      \033[0m\033[38;2;255;165;0m║  \033[0m")
    print("\033[38;2;255;165;0m║\033[0m\033[92m    /`    \\      /    `\\    \033[0m\033[38;2;255;165;0m║  \033[0m")  
    print("\033[38;2;255;165;0m╚════════════════════════════╝  \033[0m")    
     
  
def status():
    print("\033[38;2;255;165;0m╔═══════════════════════════╗\033[0m")
    print("\033[38;2;255;165;0m║\033[0m   == STATUS DE JOGO  ==   \033[38;2;255;165;0m║\033[0m")
    print("\033[38;2;255;165;0m║═══════════════════════════║\033[0m")
    print(f"\033[38;2;255;165;0m║\033[0m\033[32m Vida do Jogador: {vida_jogador:<2}/15\033[m    \033[38;2;255;165;0m║\033[0m")
    print(f"\033[38;2;255;165;0m║\033[0m\033[91m Vida do Inimigo: {vida_inimigo:<2}/20\033[0m    \033[38;2;255;165;0m║\033[0m")
    print("\033[38;2;255;165;0m╚═══════════════════════════╝\033[0m")

def acoes():
    global vida_inimigo, vida_jogador, posicao_defesa
    global pocoes, apagadores
    print("ESCOLHA SUA AÇÃO:")
    print("\033[91m╔════════════╗\033[0m \033[34m╔═════════════╗\033[m\033[93m ╔══════════╗\033[m\033[38;2;255;165;0m ╔══════════════════╗\033[0m")
    print("\033[91m║ 1. Atacar  ║\033[0m \033[34m║ 2. Defender ║\033[m\033[93m ║ 3. Item  ║\033[m\033[38;2;255;165;0m ║ 4. Bola de fogo  ║\033[0m")
    print("\033[91m╚════════════╝\033[0m \033[34m╚═════════════╝\033[m\033[93m ╚══════════╝\033[m\033[38;2;255;165;0m ╚══════════════════╝\033[0m")
    opcao = int(input("Opção: "))
    if opcao == 1:
        print("Você ataca o Orc com seu canetão!")
        time.sleep(2)
        print("4 de dano causado!")
        vida_inimigo = max(0, vida_inimigo - 4)
    elif opcao == 2:
        print("Você escolheu se defender com seu teclado escudo")
        time.sleep(2)
        print("Em guarda!")
        posicao_defesa = True
    elif opcao == 3:
        print("\nBOLSA:")
        print("\033[32m╔═════════════════════╗ ╔════════════════════════════╗ ╔═══════════╗\033[m")
        print(f"\033[32m║\033[m 1. Poção de vida x{pocoes:<2}\033[32m║ ║\033[m 2. Apagador arremesável x{apagadores:<2}\033[32m║ ║\033[m 3. Voltar \033[32m║\033[m")
        print("\033[32m╚═════════════════════╝ ╚════════════════════════════╝ ╚═══════════╝\033[m")
        item_usado = int(input("Opção: "))
        if item_usado == 1:

            if pocoes > 0:
                pocoes -= 1
                print("Você bebe a poção...")
                time.sleep(2)
                print("Recuperou 5 pontos de vida!")
                vida_jogador = min(15, vida_jogador + 5)
            else:
                print("Você não possui mais poções!")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                orc()
                status() 
                acoes()

        if item_usado == 2:
            if apagadores > 0:
                apagadores -= 1
                print("Você epicamente arremessa um apagador no Orc...")
                time.sleep(2)
                print("5 de dano nele!")
                vida_inimigo = max(0, vida_inimigo - 5)
            else:
                print("Você não possui mais apagadores!")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                orc()
                status() 
                acoes()
                
        if item_usado == 3:
            print("Voltando para as ações...")
            time.sleep(2)

            os.system("cls" if os.name == "nt" else "clear")
        
            orc()
            status() 
            acoes()  
    elif opcao == 4:

        print("Você conjura uma Bola de Fogo...")
        time.sleep(3)

        chance = random.randint(1, 100)

        if chance <= 50:

            dano = random.randint(2, 8)

            print("A Bola de Fogo acerta o Orc!")
            time.sleep(2)

            print(f"{dano} de dano causado!")
            vida_inimigo = max(0, vida_inimigo - dano)
            time.sleep(3)

        else:

            print(" A Bola de Fogo errou!")
            time.sleep(2)

    else:
        print("Opção inválida!")        


while True:
    print("\033[93m╔════════════════════════════════════════════════════════════════════════════════╗\033[m")
    print("\033[93m║                                                                                ║\033[m")
    print("\033[93m║            ██╗ ██████╗ ██████╗ ███╗   ██╗ █████╗ ██████╗  █████╗               ║\033[m")
    print("\033[93m║            ██║██╔═══██╗██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔══██╗              ║\033[m")
    print("\033[93m║            ██║██║   ██║██████╔╝██╔██╗ ██║███████║██║  ██║███████║              ║\033[m")
    print("\033[93m║       ██   ██║██║   ██║██╔══██╗██║╚██╗██║██╔══██║██║  ██║██╔══██║              ║\033[m")
    print("\033[93m║       ╚█████╔╝╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝██║  ██║              ║\033[m")
    print("\033[93m║        ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝              ║\033[m")
    print("\033[93m║                                                                                ║\033[m")
    print("\033[93m║                               ██████╗  ██████╗                                 ║\033[m")
    print("\033[93m║                               ██╔══██╗██╔═══██╗                                ║\033[m")
    print("\033[93m║                               ██║  ██║██║   ██║                                ║\033[m")
    print("\033[93m║                               ██║  ██║██║   ██║                                ║\033[m")
    print("\033[93m║                               ██████╔╝╚██████╔╝                                ║\033[m")
    print("\033[93m║                               ╚═════╝  ╚═════╝                                 ║\033[m")
    print("\033[93m║                                                                                ║\033[m")
    print("\033[93m║                    ██╗  ██╗███████╗██████╗  ██████╗ ██╗                        ║\033[m")
    print("\033[93m║                    ██║  ██║██╔════╝██╔══██╗██╔═══██╗██║                        ║\033[m")
    print("\033[93m║                    ███████║█████╗  ██████╔╝██║   ██║██║                        ║\033[m")
    print("\033[93m║                    ██╔══██║██╔══╝  ██╔══██╗██║   ██║██║                        ║\033[m")
    print("\033[93m║                    ██║  ██║███████╗██║  ██║╚██████╔╝██║                        ║\033[m")
    print("\033[93m║                    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝                        ║\033[m")
    print("\033[93m║                                                                                ║\033[m")
    print("\033[93m║                                                                                ║\033[m")
    print("\033[93m║\033[m                            \033[37m► [1] INICIAR JOGO\033[0m                                  \033[93m║\033[m")
    print("\033[93m║\033[m                            \033[91m► [2] ENCERRAR\033[0m                                      \033[93m║\033[m")
    print("\033[93m║                                                                                ║\033[m")
    print("\033[93m║                                                                                ║\033[m")
    print("\033[93m╚════════════════════════════════════════════════════════════════════════════════╝\033[m")
    iniciar = int(input("Opção: "))
    if iniciar == 1:

        print("\033[93m╔════════════════════════════════════╗\033[m")
        print("\033[93m║         HISTÓRIA DO HERÓI          ║\033[m")
        print("\033[93m╚════════════════════════════════════╝\033[m")

        print("Você era apenas um professor comum...")
        time.sleep(2)

        print("Até que um Orc invadiu a escola!")
        time.sleep(2)

        print("A princesa foi sequestrada...")
        time.sleep(2)

        print("E agora só você pode salvá-la.")
        time.sleep(2)

        input("\n\033[32mPressione ENTER para continuar...\033[0m")

        os.system("cls" if os.name == "nt" else "clear")
                
        vida_jogador = 15
        vida_inimigo= 20
        turno_orc = 0
        pocoes = 2
        apagadores = 1

        while vida_jogador > 0 and vida_inimigo > 0:

            os.system("cls")

            orc()
            status()
            acoes()

            if vida_inimigo > 0:
                turno_orc += 1

                if turno_orc == 1:

                    print("\nO Orc avança furiosamente!")
                    time.sleep(2)

                    if posicao_defesa:
                        dano = 2
                        print("Seu teclado escudo absorveu parte do dano!")
                        time.sleep(2)
                    else:
                        dano = 4

                    vida_jogador = max(0, vida_jogador - dano)

                    print(f"Você recebeu {dano} de dano!")
                    time.sleep(3)
                    posicao_defesa = False
                                                                        
                elif turno_orc == 2:

                    print("\nO Orc ergue sua marreta gigantesca...")
                    time.sleep(2)

                    print("\033[91m⚠ O ORC ESTÁ PREPARANDO UM ATAQUE PODEROSO!\033[0m")
                    time.sleep(4)

                # ATAQUE ESPECIAL
                elif turno_orc == 3:

                    print("\n☠ O Orc desfere um golpe devastador!")
                    time.sleep(2)

                    if posicao_defesa:
                        dano = 3
                        print("Você conseguiu bloquear parte do impacto!")
                        time.sleep(2)
                    else:
                        dano = 8

                    vida_jogador = max(0, vida_jogador - dano)

                    print(f"Você recebeu {dano} de dano!")
                    time.sleep(3)
                    posicao_defesa = False

                    turno_orc = 0

        if vida_inimigo <= 0:
            print("\033[33m╔═════════════════════════════════════════════════════╗\033[0m")
            print("\033[33m║                                                     ║\033[0m")
            print("\033[33m║  ██╗   ██╗██╗████████╗ ██████╗ ██████╗ ██╗ █████╗   ║\033[0m")
            print("\033[33m║  ██║   ██║██║╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗  ║\033[0m")
            print("\033[33m║  ██║   ██║██║   ██║   ██║   ██║██████╔╝██║███████║  ║\033[0m")
            print("\033[33m║  ╚██╗ ██╔╝██║   ██║   ██║   ██║██╔══██╗██║██╔══██║  ║\033[0m")
            print("\033[33m║   ╚████╔╝ ██║   ██║   ╚██████╔╝██║  ██║██║██║  ██║  ║\033[0m")
            print("\033[33m║    ╚═══╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝  ║\033[0m")
            print("\033[33m║                                                     ║\033[0m")
            print("\033[33m║                O ORC FOI DERROTADO!                 ║\033[0m")
            print("\033[33m╚═════════════════════════════════════════════════════╝\033[0m")
            time.sleep(2)

            print("╔═════════════════════════════════════════╗  ")
            print("║                                         ║  ")
            print("║\x1b[35m             PRINCESA SALVA!             \x1b[0m║  ")
            print("║\033[33m           _._                           \033[0m║  ")         
            print("║\033[33m         ,'-._'-.                        \033[0m║  ")         
            print("║\033[33m         ;'-._'-.'-.                     \033[0m║  ")         
            print("║\033[33m         :.   '-.`. \\                    \033[0m║  ")         
            print("║\033[33m         `-._  `.\\ ;                     \033[0m║  ")         
            print("║\033[38;2;250;128;114m          :_  _\033[0m\033[33m'.   \\:                   \033[0m║  ")         
            print("║\033[38;2;250;128;114m          ;o: o` \033[0m\033[33m\\  \\;                   \033[0m║  ")         
            print("║\033[38;2;250;128;114m          : ;     )\033[0m\033[33m-. `.                 \033[0m║  ")         
            print("║\033[38;2;250;128;114m           ;=-  .:\033[0m\033[33m\\     '-._             \033[0m║  ")         
            print("║\033[38;2;250;128;114m           :_.-' ; \033[0m\033[33m`.       '-.          \033[0m║  ")         
            print("║\033[38;5;198m     _._    \033[31m\033[38;2;250;128;114m :   :  \033[0m  \033[33m'-._     '-.      \033[0m ║  ")         
            print("║\033[38;5;198m    /   `.\033[38;2;250;128;114m\033[38;2;250;128;114m_.='    \\     \033[0m    \033[33m      `.  \033[0m   ║  ")         
            print("║\033[38;5;198m   :    \\:         `-.__ _._   \033[31m\033[33m'-.  \\    \033[0m║  ")         
            print("║\033[38;5;198m    \\    '.    _      ',' ` ', \033[31m\033[33m   \\  ;   \033[0m║  ")         
            print("║\033[38;5;198m     )-.   `j'^,L_..--'      ;\033[31m\033[33m ,-. : :   \033[0m║  ")         
            print("║\033[38;2;250;128;114m     : \033[0m\033[38;5;198m  )-._;)(:_           /\033[31m\033[33m : ._.' ;  \033[0m║")         
            print("║\033[38;2;250;128;114m     |  :\033[0m\033[38;5;198m   <_.Y( '-..__ _.+'\\ \033[31m\033[33m:     /   \033[0m║")         
            print("║\033[38;2;250;128;114m     ;  ;\033[0m\033[38;5;198m   ;    '      T   \\ \033[31m\033[33m `---'`.   \033[0m║ ")
            print("╚═════════════════════════════════════════╝  ")
            time.sleep(3)
            input("\nPressione ENTER para voltar ao menu...")
            os.system("cls" if os.name == "nt" else "clear")

            continue
                           
        elif vida_jogador <= 0:
            print("╔════════════════════════════════════════════════╗")
            print("║                                                ║")
            print("║\033[91m   ██████╗  █████╗ ███╗   ███╗███████╗          \033[0m║")
            print("║\033[91m  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝          \033[0m║")
            print("║\033[91m  ██║  ███╗███████║██╔████╔██║█████╗            \033[0m║")
            print("║\033[91m  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝            \033[0m║")
            print("║\033[91m  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗          \033[0m║")
            print("║\033[91m   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝          \033[0m║")
            print("║\033[91m                                                \033[0m║")
            print("║\033[91m             ██████╗ ██╗   ██╗███████╗██████╗   \033[0m║")
            print("║\033[91m            ██╔═══██╗██║   ██║██╔════╝██╔══██╗  \033[0m║")
            print("║\033[91m            ██║   ██║██║   ██║█████╗  ██████╔╝  \033[0m║")
            print("║\033[91m            ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗  \033[0m║")
            print("║\033[91m            ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║  \033[0m║")
            print("║\033[91m             ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝  \033[0m║")
            print("║\033[91m                                                \033[0m║")
            print("║\033[91m             Você foi derrotado...              \033[0m║")
            print("╚════════════════════════════════════════════════╝")
            time.sleep(2)
            input("\nPressione ENTER para voltar ao menu...")
            os.system("cls" if os.name == "nt" else "clear")

            continue
            
        
    elif iniciar == 2:
        print("Encerrando jogo...")
        time.sleep(2)
        os.system("python 1TERMO\LOGICA_PROGRAMACAO\Projetos_Python\Projetos\MENU.py")
        break

    else:
        print("Opção inválida")