# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('-=' * 20)
print('{:^40}'.format('CAIXA ELETRÔNICO!\n'))
print('Cédulas disponíveis: R$50, R$20, R$10 e R$1.')
print('-=' * 20)

saque = int(input('Insira o valor a ser sacado: R$'))
total = saque
cedula = 50 #começando pelo maior valor disponível
totalCedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedulas = 0
        if total == 0:
            break