# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

a1 = input('Insira o nome do aluno 1: ')
a2 = input('Insira o nome do aluno 2: ')
a3 = input('Insira o nome do aluno 3: ')
a4 = input('Insira o nome do aluno 4: ')

alunos = [a1, a2, a3, a4]
print(f'Alunos: {alunos}') 

random.shuffle(alunos)
print(f'Ordem de apresentação: {alunos}')