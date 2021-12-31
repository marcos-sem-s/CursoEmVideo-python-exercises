jogador = {
    'nome': input('Digite o nome do jogador de futebol: ').capitalize(),
    'partidas': int(input('Quantas partidas o mesmo jogou? ')),
    'gols': []
}

for i in range(jogador['partidas']):
    jogador['gols'].append(int(input(f'Quantos gols foram feitos no {i+1}° jogo? ')))

jogador['totalGols'] = sum(jogador['gols'])

print('-=' * 30)
print(jogador)
print('-=' * 30)
print(f'''O nome do jogador é {jogador['nome']}
Ele marcou tais gols: {jogador['gols']}
Ele participou de {jogador['partidas']} partidas no total''')
print('-=' * 30)
for c, gols in enumerate(jogador['gols']):
    print(f'=> Na {c+1}° partida ele fez {gols} gols')
print(f'Foi um total de {jogador["totalGols"]} gols')
