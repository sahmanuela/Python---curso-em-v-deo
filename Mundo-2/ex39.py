# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
current_time = datetime.datetime.now() 

ano = int(input('Insira o ano de nascimento: '))
idade = (current_time.year) - ano

if idade < 18:
    print(f'Você tem {idade} anos. Ainda não está na hora de fazer o alistamento!!')
    print(f'Falta(m) {18 - idade} ano(s)!!')
elif idade == 18:
    print(f'Você tem {idade} anos. Está na hora de fazer o alistamento!!')
else:
    print(f'Você tem {idade} anos. Já passou da hora de fazer o alistamento!!')

