# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-=' * 20)
print('Gerador de PA → Progressão Aritmética!')
print('-=' * 20)

primTermo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
ultimoTermo = (primTermo + (10-1)*razao) + 1
print('-=' * 20)

n = 0
while n < 10:
    print(primTermo, end=' → ')
    primTermo += razao
    n += 1
print('PAUSA')