# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

print('=-' * 10, 'Jogo da Adivinhação', '=-' * 10)
print('Tente adivinhar o número que estou pensando')
print('O número vai de 0 a 5!')
print('=-' * 31)

comp = random.randint(0, 5)
num = int(input('Insira sua opção: '))

if comp == num:
    print(f'Você acertou! O número era {comp}')
else:
    print(f'Errado!!! Eu pensei em {comp}, não {num}!')