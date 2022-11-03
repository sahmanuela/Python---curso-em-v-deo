# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
# A Sequência de Fibonacci tem como primeiros termos os números 0 e 1 e, a seguir, cada termo subsequente é obtido pela soma dos dois termos predecessores

print('-=' * 20)
print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 20)

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1

proxTermo = 0
cont = 3
print(t1, '→', t2, end=" → ")

while n >= cont:
    proxTermo = t1 + t2
    print(proxTermo, end=" → ")
    t1 = t2
    t2 = proxTermo
    cont += 1
print('Acabou!')
