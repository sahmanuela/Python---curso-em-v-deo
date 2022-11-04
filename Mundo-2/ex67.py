# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
import time

print('-=' * 30)
print('TABUADA')
print('Insira um número negativo para interromper o programa!')
print('-=' * 30)

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if num > 0:
        for i in range(0, 11):
            print(f'{num} x {i} = {num * i}')
        print('-' * 40)
    else:
        print('Encerrando o programa...')
        time.sleep(1)
        print('PROGRAMA TABUADA ENCERRADO! Volte sempre!')
        break