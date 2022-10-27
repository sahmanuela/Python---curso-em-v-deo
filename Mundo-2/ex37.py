# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
import math
print('-=' * 10, 'Bases de Conversão', '-=' * 10)
num = int(input('Insira um número inteiro: '))
base = int(input('Insira a base de conversão desejada:\n[ 1 ] BINÁRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL\n Insira a sua opção: '))
print('-=' * 25)

if base == 1:
    print(f'BINÁRIO do número {num} = {bin(num)[2:]}')
elif base == 2:
    print(f'OCTAL do número {num} = {oct(num)[2:]}')
elif base == 3:
    print(f'HEXADECIMAL do número {num} = {hex(num)[2:]}')
else:
    print('Opção inválida!! Tente novamente.')
