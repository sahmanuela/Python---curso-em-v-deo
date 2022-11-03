# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Insira o sexo da pessoa - F para feminino e M para masculino: ').lower()
while sexo != "f" and sexo != "m":
    print('Opção inválida, tente novamente!')
    sexo = input('Insira o sexo da pessoa - F para feminino e M para masculino: ').lower()
print('Fim do programa!')