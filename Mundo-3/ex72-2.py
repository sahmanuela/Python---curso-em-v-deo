# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
num_ptbr = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int( input('Digite um número de 0 a 20: '))

while True:
  if numero > 20 or numero < 0:
    print('Opção inválida, tente novamente!')
    numero = int( input('Digite um número de 0 a 20: '))
  else:
    print(f'Número: {num_ptbr[numero]}')
    break


