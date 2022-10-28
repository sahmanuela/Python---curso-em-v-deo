# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Insira aqui a frase a ser analisada: ').strip().lower()
letras = frase.split()
juntar = ''.join(letras)
juntarInvertido = juntar[::-1]

if juntar == juntarInvertido:
    print(f'A frase "{frase}" é um palíndromo!')
else:
    print(f'A frase "{frase}" NÃO é um palíndromo!')
