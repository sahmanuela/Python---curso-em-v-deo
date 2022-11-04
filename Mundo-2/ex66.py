# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

print('-=' * 20)
print('LEITURA E SOMA DE VALORES')
print('-=' * 20)

n = cont = soma = 0
while True:
    n = int(input('Insira um valor [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Você digitou {cont} números e a soma entre eles foi de {soma}.')