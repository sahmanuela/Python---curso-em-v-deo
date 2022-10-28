# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
# Um número é dito primo quando é possível dividir ele (divisão de inteiro com inteiro) por 1 e por ele mesmo.

# Exemplos de números primos:
# 2, 3, 5, 7,  11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373 ...
num = int(input('Insira um número inteiro: '))

count = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\33[33m', end=' ')
        count += 1
    else:
        print('\33[34m', end=' ')
    print(i, end=' ')

print(f'\n\033[m O número {num} foi divisível {count} vezes (números em amarelo).')
if count == 1:
    print('\033[m Não é um número primo')
elif count <= 2:
    print('\033[m É um número primo!!')
else:
    print('\033[m Não é um número primo')