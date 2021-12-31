from random import randint
from time import sleep
# from operator import itemgetter

resultados = {}
sorted_resultados = []

input('Digite qualquer coisa para começar: ')

for i in range(1,5):
    resultados[f'jogador_{i}'] = randint(1, 6)

print('Valores sorteados: ')
for jogadores, apostas in resultados.items():
    sleep(1)
    print(f'{jogadores} com {apostas}')
    
sorted_resultados = sorted(resultados.items(), key=lambda x:x[1], reverse=True) # Ou este ou o de baixo
# sorted_resultados = sorted(resultados.items(), key=itemgetter(1), reverse=True)

print('-=' * 10)
print('Ranking de jogadores: ')
for c, jogadores in enumerate(sorted_resultados):
    sleep(1)
    print(f'{c+1}° lugar: {jogadores[0]} com {jogadores[1]}')
    