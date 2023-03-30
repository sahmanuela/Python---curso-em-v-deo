# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
num = float(input('Insira um valor em reais: R$'))
dolar = (num / 5.2)
print(f'Com R${num} você pode comprar US${dolar:.2f}')
