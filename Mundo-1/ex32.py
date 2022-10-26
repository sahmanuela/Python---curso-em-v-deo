# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
# Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
# Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
# O ano é bissexto (tem 366 dias).
# O ano não é um ano bissexto (tem 365 dias).

ano = int(input('Insira o ano que deseja analisar: '))

if ano % 4 == 0 and ano % 100 and ano % 400:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto')
