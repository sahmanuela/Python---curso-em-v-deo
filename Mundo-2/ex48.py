# Exercício Python 48: Faça um programa que calcule a soma entre todos os números  ÍMPARES que são múltiplos de três e que se encontram no intervalo de 1 até 500.
cont = 0
soma = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        cont = cont + 1
        soma = soma + i
print(f'Números são múltiplos de 3 nesse intervalo: {cont}\nSoma entre eles: {soma}')