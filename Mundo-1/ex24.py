# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
city = input('Insira o nome de uma cidade: ')
city.lower()

if ('santo' in city.split()[0]):
  print('A cidade começa com o nome "Santo"')
else:
  print('A cidade NÃO começa com o nome "Santo"')