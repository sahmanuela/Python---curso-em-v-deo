# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('-=' * 20)
print('LEITURA E SOMA DE VALORES')
print('-=' * 20)

n = cont = soma = 0
n = int(input('Insira um valor [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Insira um valor [999 para parar]: '))

print(f'Você digitou {cont} números e a soma entre eles foi de {soma}.')