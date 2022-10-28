# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
homemVelho = 0
mulherMenor20 = 0
nomeHomemVelho = ""

for i in range(1, 5):
    nome = input(f'Insira o nome da {i}a pessoa: ')
    idade = int(input(f'Insira a idade da {i}a pessoa: '))
    sexo = input(f'Insira o sexo da {i}a pessoa [F para feminino/ M para masculino]: ').upper()
    if sexo != 'F' and sexo != 'M':
        print('Opção inválida!')
        quit()
    soma = soma + idade

    if sexo == 'M' and i == 1:
        homemVelho = idade
    elif sexo == 'M' and i != 1:
        if idade > homemVelho:
            homemVelho = idade
            nomeHomemVelho = nome

    if sexo == 'M' and idade < 20:
            mulherMenor20 += 1
print(f'Média das idades: {soma / 4} anos.\nHomem mais velho: {nomeHomemVelho} {homemVelho} anos\nMulheres com menos de 20 anos: {mulherMenor20}')

