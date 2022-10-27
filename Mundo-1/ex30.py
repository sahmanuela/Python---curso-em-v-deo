# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('=-' * 10, 'PAR ou ÍMPAR', '=-' * 10)
escolha = int(input('Insira um número inteiro: '))
print('=-' * 27)

if escolha % 2 == 0:
    print(f'O número {escolha} é PAR')
else:
    print(f'O número {escolha} é ÍMPAR')


