# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import time
import random

print('-=' * 10, 'PEDRA, PAPEL, TESOURA', '-=' * 10)
opcao = int(input('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\nQual sua jogada? '))

if opcao != 0 and opcao != 1 and opcao != 2:
    print('JOGADA INVÁLIDA!! Tente novamente')
    quit()

time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')
time.sleep(1)

print('-=' * 20)
if opcao == 0:
    print('Você jogou PEDRA')
elif opcao == 1:
    print('Você jogou PAPEL')
else:
    print('Você jogou TESOURA')

computador = random.randint(0, 3)
if computador == 0:
    print('Computador jogou PEDRA')
elif computador == 1:
    print('Computador jogou PAPEL')
else:
    print('Computador jogou TESOURA')
print('-=' * 20)

if opcao == computador:
    print('EMPATE!!')
elif opcao == 0 and computador == 1:
    print('COMPUTADOR VENCEU!!')
elif opcao == 0 and computador == 2:
    print('VOCÊ VENCEU!!')
elif opcao == 1 and computador == 0:
    print('VOCÊ VENCEU!!')
elif opcao == 1 and computador == 2:
    print('COMPUTADOR VENCEU!!')
elif opcao == 2 and computador == 0:
    print('COMPUTADOR VENCEU!!')
elif opcao == 2 and computador == 1:
    print('VOCÊ VENCEU!!')
