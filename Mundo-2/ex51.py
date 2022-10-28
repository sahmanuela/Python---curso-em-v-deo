# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
primTermo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))

ultimoTermo = (primTermo + (10-1)*razao) + 1

for i in range(primTermo, ultimoTermo, razao):
    print(i, end=' ')