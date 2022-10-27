# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
n1 = float(input('Digite um número: '))
n1int = math.trunc(n1)
print(f'A porção inteira de {n1} é {n1int}')