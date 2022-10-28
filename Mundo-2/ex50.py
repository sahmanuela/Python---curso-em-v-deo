# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0

for i in range(6):
    num = int(input('Insira um número inteiro: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'Quantidade de números pares: {cont}\nSoma entre eles: {soma}')