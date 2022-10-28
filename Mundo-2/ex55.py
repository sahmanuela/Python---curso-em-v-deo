# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = menor = 0
for i in range(1, 6):
    peso = float(input(f'Insira o peso em kg da {i}a pessoa: '))
    if i == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('-=' * 25)
print(f'Maior peso: {maior}kg\nMenor peso: {menor}kg')