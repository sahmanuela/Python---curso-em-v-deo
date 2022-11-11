# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
print('-=' * 20)
print('{:^40}'.format('CADASTRO DE PESSOAS'))
print('-=' * 20)

mais18 = homens = mulheres20 = 0
while True:
    idade = int(input('Insira a idade de uma pessoa: '))
    
    if idade > 18:
        mais18 += 1
    
    sexo = ' '
    while sexo not in 'FM':
        sexo = input('Insira o sexo dessa pessoa [F/M]: ').upper().strip()[0]
        if sexo not in 'FM':
            print('Opção inválida! Tente novamente.')
    
    if sexo == 'M':
        homens += 1
    
    if sexo == 'F' and idade > 20:
        mulheres20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar [S/N]? ').upper().strip()[0]
        if continuar not in 'SN':
            print('Opção inválida! Tente novamente.')
        
    if continuar == 'N':
        break

print(f'Pessoas cadastradas com mais de 18 anos: {mais18}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres cadastradas com mais de 20 anos: {mulheres20}')
