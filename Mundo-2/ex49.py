# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Insira um número inteiro: '))

for i in range(0, 11):
    print(f'{num} x {i} = {num * i}')