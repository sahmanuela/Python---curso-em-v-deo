# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = input('Insira seu nome completo: ')
letras = nome.split()
juntar = ''.join(letras)


print(f'{nome}\n{nome.upper()}\n{nome.lower()}')
print(f'Número de letras do seu nome completo: {len(juntar)}')
print(f'Número de letras do seu primeiro nome: {len(letras[0])}')

