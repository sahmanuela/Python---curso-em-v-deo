# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Insira um número inteiro: '))
calculo = 1

print(f'{num}! = ', end="")
while num > 0:
    print(num, end="")
    print(' x ' if num > 1 else ' = ', end="")
    calculo *= num
    num -= 1
print(calculo)