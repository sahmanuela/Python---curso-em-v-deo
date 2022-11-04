# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import time, random

print('-=' * 30)
print('PAR OU ÍMPAR')
print('-=' * 30)

jogador = int(input('Escolha 1 número de 0 a 5: '))

while jogador not in [0, 1, 2, 3, 4, 5]:        
    print('Opção inválida! Tente novamente.')
    jogador = int(input('Escolha 1 número de 0 a 5: '))

jogadorPouI = int(input('Escolha par ou ímpar:\n[ 1 ] PAR\n[ 2 ] ÍMPAR\nQual a sua escolha? '))
computador = random.randint(0, 5)

print('-=' * 30)

cont = 1
while True:
    if jogadorPouI == 1: #Jogador escolheu PAR
        soma = jogador + computador
        if soma % 2 == 0:
            time.sleep(1)
            print('-=' * 30)
            print(f'VOCÊ GANHOU!\nVocê jogou {jogador} e o computador jogou {computador}!\n{jogador} + {computador} = {soma} -> PAR')
            break
        else:
            time.sleep(1)
            print(f'VOCÊ PERDEU!\nVocê jogou {jogador} e o computador jogou {computador}!\n{jogador} + {computador} = {soma} -> ÍMPAR')
            cont += 1
            time.sleep(1)
            print('Vamos mais uma vez...')
            time.sleep(1)
            
            print('-=' * 30)
            print('PAR OU ÍMPAR')
            print('-=' * 30)

            jogador = int(input('Escolha 1 número de 0 a 5: '))
            while jogador not in [0, 1, 2, 3, 4, 5]:        
                print('Opção inválida! Tente novamente.')
                jogador = int(input('Escolha 1 número de 0 a 5: '))
            jogadorPouI = int(input('Escolha par ou ímpar:\n[ 1 ] PAR\n[ 2 ] ÍMPAR\nQual a sua escolha? '))
            
    elif jogadorPouI == 2: #Jogador escolheu ÍMPAR
        soma = jogador + computador
        if soma % 2 == 1:
            time.sleep(1)
            print('-=' * 30)
            print(f'VOCÊ GANHOU!\nVocê jogou {jogador} e o computador jogou {computador}!\n{jogador} + {computador} = {soma} -> ÍMPAR')
            break
        else:
            time.sleep(1)
            print(f'VOCÊ PERDEU!\nVocê jogou {jogador} e o computador jogou {computador}!\n{jogador} + {computador} = {soma} -> PAR')  
            cont += 1
            time.sleep(1)
            print('Vamos mais uma vez...')
            time.sleep(1)

            print('-=' * 30)
            print('PAR OU ÍMPAR')
            print('-=' * 30)

            jogador = int(input('Escolha 1 número de 0 a 5: '))
            while jogador not in [0, 1, 2, 3, 4, 5]:        
                print('Opção inválida! Tente novamente.')
                jogador = int(input('Escolha 1 número de 0 a 5: '))
            jogadorPouI = int(input('Escolha par ou ímpar:\n[ 1 ] PAR\n[ 2 ] ÍMPAR\nQual a sua escolha? '))
    
    else:
        print('Opção Inválida! Tente novamente.')
        time.sleep(1)
        jogadorPouI = int(input('Escolha par ou ímpar:\n[ 1 ] PAR\n[ 2 ] ÍMPAR\nQual a sua escolha? '))

print(f'FIM DE JOGO! Foram necessárias {cont} tentativas para você ganhar.')
