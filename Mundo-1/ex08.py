# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
medida = float(input('Insira um valor em metros: '))
cm = medida * 100
mm = medida * 1000

print(f'Número: {medida}\ncm: {cm}\nmm: {mm}')