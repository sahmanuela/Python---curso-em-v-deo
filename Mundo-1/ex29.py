# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Insira a velocidade do carro em km/h: '))

if vel > 80:
    print(f'Você está a {vel}km/h, o limite era de 80km/h!!')
    multa = (vel - 80) * 7
    print(f'Você foi multado! Sua multa é de R${multa:.2f}!!')
else:
    print(f'Você está a {vel}km/h. Está dentro do limite, continue assim!!')
