# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

a1 = input('Insira o nome do aluno 1: ')
a2 = input('Insira o nome do aluno 2: ')
a3 = input('Insira o nome do aluno 3: ')
a4 = input('Insira o nome do aluno 4: ')

alunos = [a1, a2, a3, a4]
randomico = random.choice(alunos)
print(f'Alunos: {alunos}\nEscolhido: {randomico}')

