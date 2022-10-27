# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = input('Insira um número inteiro de 0 a 9999: ')
print('-=' * 20)
print(f'Analisando o número {int(num)}')
print('-=' * 20)

print(f'{num[0]}\n{num[1]}\n{num[2]}\n{num[3]}')
print('-=' * 20)

print(f'Unidade digito: {(int(num) // 1 % 10)}')
print(f'Dezena digito: {(int(num) // 10 % 10)}')
print(f'Centena digito: {(int(num) // 100 % 10)}')
print(f'Milhar digito: {(int(num) // 1000 % 10)}')
