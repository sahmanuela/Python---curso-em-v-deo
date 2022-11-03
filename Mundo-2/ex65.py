# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
print('-=' * 20)
print('LEITURA E ANÁLISE DE NÚMEROS')
print('-=' * 20)

n = cont = soma = 0
resposta = "S"

while resposta == 'S':
    n = int(input('Insira um valor: '))
    resposta = input('Deseja continuar? [S/N] ').upper()
    cont += 1
    soma += n

    if resposta != 'S' and resposta != 'N':
        print('Opção inválida!')

print(f'Você digitou {cont} números e a soma entre eles foi de {soma}.')