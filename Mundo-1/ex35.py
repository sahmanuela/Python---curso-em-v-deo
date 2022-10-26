# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
l1 = float(input('Insira o comprimento da linha 1 (em metros): '))
l2 = float(input('Insira o comprimento da linha 2 (em metros): '))
l3 = float(input('Insira o comprimento da linha 3 (em metros): '))

# Basta fazer a soma entre os dois lados menores. Se a soma entre eles for maior que o terceiro lado, então, a soma entre qualquer um deles e o terceiro lado (que é o maior) terá o mesmo resultado.
if (l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2):
    print(f'É possível formar um triângulo com as retas {l1}, {l2} e {l3}!')
else:
    print(f'NÃO É possível formar um triângulo com as retas {l1}, {l2} e {l3}!')