# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = int(input('Insira o valor do ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print(f'Ângulo: {ang}\nSeno: {sen:.2f}\nCosseno: {cos:.2f}\nTangente: {tang:.2f}')