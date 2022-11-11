# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import time, random

print('-=' * 30)
print('{:^60}'.format('PAR OU ÍMPAR'))
print('-=' * 30)

vitoria = 0
while True:
    jogador = int(input('Escolha 1 número de 0 a 5: '))
    computador = random.randint(0, 5)

    while jogador not in [0, 1, 2, 3, 4, 5]:        
        print('Opção inválida! Tente novamente.')
        jogador = int(input('Escolha 1 número de 0 a 5: '))

    jogadorPouI = ' '
    while jogadorPouI not in 'PI':
        jogadorPouI = input('Par ou ímpar [P/I]? ').upper().strip()[0]
        if jogadorPouI not in 'PI':
            print('Opção inválida! Tente novamente.')

    total = jogador + computador

    print('-=' * 30)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total = {total} -> ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    if jogadorPouI == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!!')
            vitoria += 1
        else:
            print('Você PERDEU.')
            break
    elif jogadorPouI == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!!')
            vitoria += 1
        else:
            print('Você PERDEU.')
            break
    
    time.sleep(1)
    print('-=' * 30)
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vez(es).')