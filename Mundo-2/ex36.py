# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Insira o valor da casa: R$'))
salario = float(input('Insira o seu salário: R$'))
anos = int(input('Em quantos anos você deseja quitar a casa? '))
prestacao = (valor/(anos * 12))

if prestacao >= (salario * 30 / 100):
    print('Emprestimo NEGADO!')
else:
    print(f'Empréstimo ACEITO! Suas parcelas mensais serão de R${prestacao:.2f}.')

