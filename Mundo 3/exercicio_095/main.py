jogadores = []

while True:
    jogador = {
        'nome': input('Digite o nome do jogador de futebol: ').capitalize(),
        'partidas': int(input('Quantas partidas o mesmo jogou? ')),
        'gols': []
    }

    for i in range(jogador['partidas']):
        jogador['gols'].append(int(input(f'Quantos gols foram feitos no {i+1}° jogo? ')))
    jogador['totalGols'] = sum(jogador['gols'])

    choice = input('Deseja continuar? [S/N] ').upper()

    jogadores.append(jogador)

    if choice == 'N':
        break

print('-=' * 35)
print(f"{'Jog.':<6}{'Nome':<15}{'Qtd de gols':<25}{'Total':<5}")
for c, jogador in enumerate(jogadores):
    print(f'{c:<6}{jogador["nome"]:<15}{str(jogador["gols"]):<25}{jogador["totalGols"]:<5}')

while True:
    print('-=' * 35)
    escolha = int(input('- Deseja vizualizar o aproveitamento de qual jogador? [-1 para sair] '))

    if escolha == -1:
        break
    elif escolha in range(len(jogadores)):
        print(f'Aproveitamento do jogador {jogadores[escolha]["nome"]}:')
        for c, gols in enumerate(jogadores[escolha]['gols']):
            print(f'=> No jogo {c} foram marcados {gols} gols')

    else:
        print('Escolha inválida, tente novamente!')

print('- Programa terminado -')
