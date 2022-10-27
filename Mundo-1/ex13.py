# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Insira seu salário: R$'))
aumento = (salario * 15) / 100
salFinal = salario + aumento
print(f'Salário: R${salario}\n15% do salário: R${aumento:.2f}\nSalário com aumento de 15%: R${salFinal:.2f}')