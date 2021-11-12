suportes = ('Rakan', 'Nami', 'Lulu', 'Yuumi', 'Leona', 'Zyra', 'Thresh', 'Pyke', 'Morgana', 'Karma')
vogais = ('a', 'e', 'i', 'o', 'u')

for palavras in suportes:
    print(f'\nNo suporte {palavras.upper()} tem como vogais: ', end='')
    for letras in palavras:
        if letras in vogais:
            print(letras, '', end='')
