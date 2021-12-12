pessoasQtd = 0
pessoas = []
cadastrados = []

while True:
    varList = []
    nome = input('Digite o nome de uma pessoa: ')
    peso = int(input('Digite o peso desta pessoa: '))
    pessoasQtd += 1

    pessoas.append(nome)
    varList.append(nome)
    varList.append(peso)
    cadastrados.append(varList)

    escolha = input('Deseja continuar o cadastro? [S/N] ')
    if escolha in 'Nn':
        break

print(f'Foram {pessoasQtd} pessoas cadastradas no total, sendo elas: {pessoas}')
print('As pessoas mais pesadas foram: ', end='')
for c in range(len(cadastrados)):
    if cadastrados[c][1] > 80:
        print(cadastrados[c][0], end=', ')
print('\nAs pessoas mais leves foram: ')
for c in range(len(cadastrados)):
    if cadastrados[c][1] < 70:
        print(cadastrados[c][0], end=', ')
