# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
from num2words import num2words

numero = int( input('Digite um número de 0 a 20: '))

while True:
  if numero > 20 or numero < 0:
    print('Opção inválida, tente novamente!')
    numero = int( input('Digite um número de 0 a 20: '))
  else:
    num_ptbr = num2words(numero, lang='pt-br')
    print(f'Número: {num_ptbr}')
    break


