# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Insira o valor do produto a ser analisado: R$'))
precoFinal = preco - (preco * 5/100)
desconto = preco - precoFinal

print(f'Com 5% de desconto, o valor passará de R${preco:.2f} para R${precoFinal:.2f}, com um desconto de R${desconto:.2f}')