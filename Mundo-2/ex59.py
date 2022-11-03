# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
import time

num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira outro número inteiro: '))

opcao = 0
while opcao != 5:
    print('-=' * 25)
    opcao = int(input(f'O que deseja fazer com os números {num1} e {num2}?\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n Insira sua opção: '))
    print('-=' * 25)

    if opcao == 1:
        time.sleep(0.6)
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
        time.sleep(0.6)

    elif opcao == 2:
        time.sleep(0.6)
        multiplicar = num1 * num2
        print(f'{num1} x {num2} = {multiplicar}')
        time.sleep(0.6)

    elif opcao == 3:
        time.sleep(0.6)
        if num1 > num2:
            print(f'{num1} > {num2}')
            time.sleep(0.6)
        else:
            print(f'{num2} > {num1}')
            time.sleep(0.6)

    elif opcao == 4:
        time.sleep(0.6)
        num1 = int(input('Insira um número inteiro: '))
        num2 = int(input('Insira outro número inteiro: '))
        time.sleep(0.6)

    elif opcao == 5:
        time.sleep(0.6)
        print('Finalizando...')
        time.sleep(0.6)
        break
    
    else:
        time.sleep(0.6)
        print('Opção inválida!! Tente novamente.')
        time.sleep(0.6)
