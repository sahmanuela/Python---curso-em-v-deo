# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random

print('=-' * 10, 'Jogo da Adivinhação', '=-' * 10)
print('Tente adivinhar o número que estou pensando!!')
print('O número vai de 0 a 10!')
print('=-' * 31)

comp = random.randint(0, 10)
num = int(input('Insira sua opção: '))
cont = 0

while comp != num:
    if num > comp:
        print(f'Ainda não acertou!!\nO número que eu estou pensando é MENOR do que {num}!!')
        num = int(input('Tente novamente. Insira sua opção: '))
        cont += 1
    else:
        print(f'Ainda não acertou!!\nO número que eu estou pensando é MAIOR do que {num}!!')
        num = int(input('Tente novamente. Insira sua opção: '))
        cont += 1

print(f'Depois de {cont} tentativas você GANHOUU!!')