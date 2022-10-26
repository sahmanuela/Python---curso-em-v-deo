# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Insira o seu salário: R$'))

if sal > 1250:
    aumento = sal + (sal * (10/100))
    print(f'Com um aumento de 10%, seu salário vai de {sal} para R${aumento}')
else:
    aumento = sal + (sal * (15/100))
    print(f'Com um aumento de 15%, seu salário vai de {sal} para R${aumento}')

