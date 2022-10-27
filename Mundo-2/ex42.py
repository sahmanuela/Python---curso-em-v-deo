# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
l1 = float(input('Insira o comprimento da linha 1 (em metros): '))
l2 = float(input('Insira o comprimento da linha 2 (em metros): '))
l3 = float(input('Insira o comprimento da linha 3 (em metros): '))

# Basta fazer a soma entre os dois lados menores. Se a soma entre eles for maior que o terceiro lado, então, a soma entre qualquer um deles e o terceiro lado (que é o maior) terá o mesmo resultado.
if (l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2):
    print(f'É possível formar um triângulo com as retas {l1}, {l2} e {l3}!')
    if l1 == l2 == l3:
        print('Triângulo EQUILÁTERO')
    elif (l1 != l2 and l1 != l3 and l2 == l3) or (l2 != l1 and l2 != l3 and l1 == l3) or (l3 != l2 and l3 != l1 and l2 == l1):
        print('Triângulo ISÓSCELES.')
    elif l1 != l2 != l3:
        print('Triângulo ESCALENO.')
else:
    print(f'NÃO É possível formar um triângulo com as retas {l1}, {l2} e {l3}!')
