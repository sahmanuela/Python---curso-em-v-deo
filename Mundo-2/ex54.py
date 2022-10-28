# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
import math

current_time = datetime.datetime.today() 
maior = 0
menor = 0

for i in range(1, 8):
    dia = int(input(f'Insira o dia de nascimento (DD) da {i}a pessoa: '))
    mes = int(input(f'Insira o mes de nascimento (MM)  da {i}a pessoa: '))
    ano = int(input(f'Insira o ano de nascimento (YYYY)  da {i}a pessoa: '))

    dataNasc = datetime.date(ano, mes, dia)
    print(dataNasc)
    diferenca = ((current_time.date()) - dataNasc)
    idade = (diferenca.days / 365.25)
    print(f'Idade = {math.trunc(idade)} anos')
    print('-=' * 30)

    if idade > 18:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas já atingiram a maioridade!\n{menor} pessoas são menores de idade!')
