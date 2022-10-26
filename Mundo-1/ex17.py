# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Insira o comprimento do cateto oposto: '))
ca = float(input('Insira o comprimento do cateto adjacente: '))
hip = math.sqrt((ca*ca) + (co*co))
print(f'Valor da hipotenusa: {hip:.2f}')