# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
frase = str(input('Digite seu nome completo: ')).lower()
print(f'Primeiro nome: {frase.split()[0]}\nÚltimo nome:{frase.split()[-1]}')