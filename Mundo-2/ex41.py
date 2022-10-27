# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
import datetime
import math

current_time = datetime.datetime.today() 

dia = int(input('Insira o dia de nascimento (DD): '))
mes = int(input('Insira o mes de nascimento (MM): '))
ano = int(input('Insira o ano de nascimento (YYYY): '))

dataNasc = datetime.date(ano, mes, dia)
diferenca = ((current_time.date()) - dataNasc)
idade = (diferenca.days / 365.25)

if idade <= 9:
    print(f'Idade: {math.trunc(idade)} anos. Categoria: MIRIM')
elif idade <= 14:
    print(f'Idade: {math.trunc(idade)} anos. Categoria: INFANTIL')
elif idade <= 19:
    print(f'Idade: {math.trunc(idade)} anos. Categoria: JÚNIOR')
elif idade <= 25:
    print(f'Idade: {math.trunc(idade)} anos. Categoria: SÊNIOR')
else:
    print(f'Idade: {math.trunc(idade)} anos. Categoria: MASTER')



