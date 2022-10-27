# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
num = int(input('Insira um número inteiro: '))
print(f'Dobro de {num}: {num * 2}\nTriplo de {num}: {num * 3}\nRaíz de {num}: {math.sqrt(num):.2f}')