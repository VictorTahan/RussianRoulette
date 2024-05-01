import random

# Função para inserir a quantidade de balas no revólver
def inserir(x):
    indice_aleatorio = random.sample(range(len(revolver)), x)
    for indice in indice_aleatorio:
        revolver[indice] = 'bullet'
    print(f"{x} balas foram inseridas no tambor.")

# Lista de 6 espaços para bala no revólver
revolver = ['empty','empty','empty','empty','empty','empty']

while True:
    start = int(input("Este é um revólver calibre .38 com 6 espaços para munição no tambor.\nDigite a quantidade de balas que deseja inserir no tambor: "))
    
    if start == 0:
        print("Você tem que obrigatoriamente inserir ao menos uma bala no tambor!")
        continue
    
    elif 1 <= start < 6:
        inserir(start)
    
    else:
        print("Impossível inserir mais do que 5 balas no tambor!")
        continue
    
    while True:
        menu = int(input("Digite 1 para engatilhar e atirar\nDigite 2 para girar o tambor, engatilhar e atirar."))
        if menu == 1:
            choose = int(input("Digite 1 para atirar em si mesmo.\nDigite 2 para atirar no adversário."))
            if choose == 1:
                shoot = revolver[0]
                if shoot == 'bullet':
                    print("PLOW! Você morreu!")
                    restart = int(input("Jogar novamente?\nDigite 1 para reiniciar o jogo.\nDigite qualquer outro número para sair."))
                    if restart != 1:
                        break
                else:
                    print("TEC! TEC! Você escapou!\nÉ a vez do seu adversário!")               
                    print("Seu adversário girou o tambor, engatilhou e apontou pra sua cara!")
                    enemy_shoot = random.choice(revolver)
                    if enemy_shoot == 'bullet':
                        print("PLOW! Você morreu!")
                        restart = int(input("Jogar novamente?\nDigite 1 para reiniciar o jogo.\nDigite qualquer outro número para sair."))
                        if restart !=1:
                            break
                    else:
                        print("TEC! TEC! Você escapou!")
                        continue
            elif choose == 2:
                shoot = revolver[0]
                if shoot == 'bullet':
                    print("PLOW! Você matou seu adversário!")
                    restart = int(input("Jogar novamente?\nDigite 1 para reiniciar o jogo.\nDigite qualquer outro número para sair."))
                    if restart != 1:
                        break
                else:
                    print("TEC! TEC! Seu adversário escapou!\nÉ a vez do seu adversário!")
                    print("Seu adversário girou o tambor, engatilhou e apontou pra sua cara!")
                    enemy_shoot = random.choice(revolver)
                    if enemy_shoot == 'bullet':
                        print("PLOW! Você morreu!")
                        restart = int(input("Jogar novamente?\nDigite 1 para reiniciar o jogo.\nDigite qualquer outro número para sair."))
                        if restart !=1:
                            break
                    else:
                        print("TEC! TEC! Você escapou!")
                        continue
            else: 
                print("Digite um número válido!")
                continue
        elif menu == 2:
            choose = int(input("Digite 1 para atirar em si mesmo.\nDigite 2 para atirar no adversário."))
            if choose == 1:
                shoot = random.choice(revolver)
                if shoot == 'bullet':
                    print("PLOW! Você morreu!")
                    restart = int(input("Jogar novamente?\nDigite 1 para reiniciar o jogo.\nDigite qualquer outro número para sair."))
                    if restart != 1:
                        break
                else:
                    print("TEC! TEC! Você escapou!\nÉ a vez do seu adversário!")
                    print("Seu adversário girou o tambor, engatilhou e apontou pra sua cara!")
                    enemy_shoot = random.choice(revolver)
                    if enemy_shoot == 'bullet':
                        print("PLOW! Você morreu!")
                        restart = int(input("Jogar novamente?\nDigite 1 para reiniciar o jogo.\nDigite qualquer outro número para sair."))
                        if restart !=1:
                            break
                    else:
                        print("TEC! TEC! Você escapou!")
                        continue
            elif choose == 2:
                shoot = random.choice(revolver)
                if shoot == 'bullet':
                    print("PLOW! Você matou seu adversário!")
                    restart = int(input("Jogar novamente?\nDigite 1 para reiniciar o jogo.\nDigite qualquer outro número para sair."))
                    if restart != 1:
                        break
                else:
                    print("TEC! TEC! Seu adversário escapou!\nÉ a vez do seu adversário!")
                    print("Seu adversário girou o tambor, engatilhou e apontou pra sua cara!")
                    enemy_shoot = random.choice(revolver)
                    if enemy_shoot == 'bullet':
                        print("PLOW! Você morreu!")
                        restart = int(input("Jogar novamente?\nDigite 1 para reiniciar o jogo.\nDigite qualquer outro número para sair."))
                        if restart !=1:
                            break
                    else:
                        print("TEC! TEC! Você escapou!")
                        continue
            else: 
                print("Digite um número válido!")
                continue
        else: 
            print("Digite um número válido!")
            continue