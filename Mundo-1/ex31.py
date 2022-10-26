# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = float(input('Insira a distância da viagem em km: '))

if dist > 200:
    valor = dist * 0.45
    print(f'Com {dist}km, você irá gastar R${valor}')
else:
    valor = dist * 0.5
    print(f'Com {dist}km, você irá gastar R${valor}')
