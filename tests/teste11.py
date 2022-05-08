# filme = {
# 'título': 'Star Wars',
# 'ano': 1977,
# 'diretor': 'George Lucas'
# }

# filme2 = {
# 'título': 'Avengers',
# 'ano': 2012,
# 'diretor': 'Joss Whedon'
# }

locadora = [{
'título': 'Star Wars',
'ano': 1977,
'diretor': 'George Lucas'
}, {
'título': 'Avengers',
'ano': 2012,
'diretor': 'Joss Whedon'
}]
# locadora.append(filme)
# locadora.append(filme2)

# print(filme)
# print(filme.items())
# print(filme.values())
# print(filme.keys())

# for keys, values in filme.items():
#     print(f'O {keys} é {values}')


for filmes in locadora:
    for keys, values in filmes.items():
        print(keys, values)
