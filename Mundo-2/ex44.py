# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

valor = float(input('Insira o valor do produto: R$'))
condicao = int(input('Insira a opção desejada:\n[ 1 ] À VISTA!\n[ 2 ] À VISTA NO CARTÃO!\n[ 3 ] EM ATÉ 2x NO CARTÃO!\n[ 4 ] 3x OU MAIS NO CARTÃO\nInsira a sua opção: '))
print('-=' * 20)
if condicao == 1:
    desconto = (valor * 10 / 100)
    print(f'Você obterá um desconto de R${desconto:.2f}!!\nPreço final = R${(valor - desconto):.2f}')
elif condicao == 2:
    desconto = (valor * 5 / 100)
    print(f'Você obterá um desconto de R${desconto:.2f}!!\nPreço final = R${(valor - desconto):.2f}')
elif condicao == 3:
    print(f'Sem desconto e nem juros!!\nValor a ser pago = R${valor:.2f}')
elif condicao == 4:
    juros = (valor * 20 / 100)
    print(f'Você obterá um JUROS de R${juros}!!\nPreço final = R${(valor + juros):.2f}')
else:
    print('OPÇÃO INVÁLIDA! Tente novamente.')