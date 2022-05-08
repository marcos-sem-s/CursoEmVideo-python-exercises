def ficha(nome = '<desconhecido>', gols = 0):
    if gols.isnumeric():
        int(gols)
    else:
        gols = 0
    if nome.isalpha():
        str(nome).capitalize()
    else:
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


name = input('Digite o nome do jogador: ').capitalize()
goals = input('Digite quantos gols o jogador fez: ')

ficha(name, goals)
