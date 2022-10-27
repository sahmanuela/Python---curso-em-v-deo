# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira outro número inteiro: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num2} é maior que {num1}')
else:
    print('Os dois valores inseridos são IGUAIS!')