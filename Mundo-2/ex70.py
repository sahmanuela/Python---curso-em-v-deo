# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
print('-=' * 20)
print('{:^40}'.format('PRODUTOS E PREÇOS'))
print('-=' * 20)

soma = maisMil = precoProdutoBarato = cont = 0
produtoBarato = ' '
while True:
    produto = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o valor do produto: R$'))

    soma += preco
    cont += 1

    if preco > 1000:
        maisMil += 1
    
    if cont == 1:
        precoProdutoBarato = preco
        produtoBarato = produto
    else:
        if preco < precoProdutoBarato:
            precoProdutoBarato = preco
            produtoBarato = produto
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar [S/N]? ').upper().strip()[0]
        if continuar not in 'SN':
            print('Opção inválida! Tente novamente.')
        print('-' * 40)
        
    if continuar == 'N':
        break

print(f'Total gasto na compra: R${soma}')
print(f'Total de produtos que custam mais de R$1000: {maisMil}')
print(f'Produto mais barato: {produtoBarato} R${precoProdutoBarato}')
