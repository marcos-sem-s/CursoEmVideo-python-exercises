pessoasQtd = 0
pessoas = []
cadastrados = []
maisLeve = 5670
maisPesada = 0

while True:
    varList = []
    nome = input('Digite o nome de uma pessoa: ')
    peso = float(input('Digite o peso desta pessoa: '))
    pessoasQtd += 1

    pessoas.append(nome)
    varList.append(nome)
    varList.append(peso)
    cadastrados.append(varList)

    if peso > maisPesada:
        maisPesada = peso
    if peso < maisLeve:
        maisLeve = peso

    escolha = input('Deseja continuar o cadastro? [S/N] ')
    if escolha in 'Nn':
        break

print(f'Foram {pessoasQtd} pessoas cadastradas no total, sendo elas: {pessoas}')
print(f'O maior peso foi de {maisPesada}, possuindo ele: ', end='')
for c in range(len(cadastrados)):
    if cadastrados[c][1] == maisPesada:
        print(cadastrados[c][0], end=', ')
print(f'\nO menor peso foi de {maisLeve}, possuindo ele: ', end='')
for c in range(len(cadastrados)):
    if cadastrados[c][1] == maisLeve:
        print(cadastrados[c][0], end=', ')
