# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
print('-=' * 45)
print('{:^90}'.format('CAMPEONATO BRASILEIRO DE FUTEBOL 2022'))
print('-=' * 45)
print()

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print(f'5 PRIMEIROS TIMES: ', end=' ')
for cont in range(5):
  print(times[cont], end='  ')
print()
print('-' * 90)

print(f'4 ÚLTIMOS TIMES: ', end=' ')
for cont in range(4):
  print(times[16:][cont], end='  ')
print()
print('-' * 90)

print(f'ORDEM ALFABÉTICA: ', end=' ')
print(sorted(times))
print('-' * 90)

print(f'O CHAPECOENSE ESTÁ NA POSIÇÃO: ', end='')
print(times.index('Ceará'))