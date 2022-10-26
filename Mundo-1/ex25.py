# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

name = input('Insira o seu nome completo: ')
name.lower()

if ('silva' in name.split()):
  print(f'O nome "{name.title()}" contém "Silva"')
else:
  print(f'O nome "{name.title()}" NÃO contém "Silva"')