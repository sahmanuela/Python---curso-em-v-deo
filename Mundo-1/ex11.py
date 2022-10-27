# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
import math
larg = float(input('Insira a largura em metros: '))
alt = float(input('Insira a altura em metros: '))
area = alt * larg
tinta = math.ceil(area / 2)

print(f'Área da parede: {area}\nQuantidade necessária: {tinta} litros de tinta.')
