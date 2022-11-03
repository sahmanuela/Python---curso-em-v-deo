# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('-=' * 20)
print('Gerador de PA → Progressão Aritmética!')
print('-=' * 20)

primTermo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
ultimoTermo = (primTermo + (10-1)*razao) + 1
print('-=' * 20)

n = 0
termos = 10
while n < termos:
    print(primTermo, end=' → ')
    primTermo += razao
    n += 1
print('PAUSA')

print('-=' * 20)
maisTermos = int(input('Quantos termos você quer mostrar a mais? '))
termos = termos + maisTermos


while maisTermos != 0:
    while n <= termos - 1:
        print(primTermo, end=' → ')
        primTermo += razao
        n += 1
    else:
        print('PAUSA')
        print('-=' * 20)
        maisTermos = int(input('Quantos termos você quer mostrar a mais? '))
        termos = termos + maisTermos
else:
    print(f'PA finalizada com {n} termos!')
