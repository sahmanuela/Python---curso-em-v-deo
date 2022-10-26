# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))
num3 = float(input('Insira outro número: '))
print('=-' * 24)

print(f'Os números escolhidos foram: {num1}, {num2} e {num3}')

# maiores
if num1 > num2 and num1 > num3:
    print(f'O maior número é o {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é o {num2}')
elif num3 > num2 and num3 > num1:
    print(f'O maior número é o {num3}')

# menores
if num1 < num2 and num1 < num3:
    print(f'O menor número é o {num1}')
elif num2 < num1 and num2 < num3:
    print(f'O menor número é o {num2}')
elif num3 < num2 and num3 < num1:
    print(f'O menor número é o {num3}')