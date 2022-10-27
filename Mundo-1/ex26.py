# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).lower().strip()

if (frase.count("a")) > 0:
    print(f'A letra A aparece {frase.count("a")} vezes na frase "{frase.title()}".\nEla aparece pela primeira vez na posição {frase.find("a")+1} e a última vez na posição {frase.rfind("a")+1}')
else:
    print(f'A letra A não aparece na frase "{frase.title()}"')