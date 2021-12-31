pessoas = []
mediaIdade = 0

while True:
    pessoa = {
        'nome': str(input('Digite o nome de uma pessoa: ')).capitalize(),
        'idade': int(input('Digite a sua idade: ')),
        'sexo': str(input('Digite seu sexo: [M/F] ')).upper()
    }
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input('ERRO, digitar apenas M ou F: ').upper()
        
    pessoas.append(pessoa)
    
    choice = str(input('Deseja continuar o cadastro? [S/N] ')).upper()
    if choice == 'N':
        break

for i in range(len(pessoas)):
    mediaIdade += (pessoas[i]['idade'])
mediaIdade /= len(pessoas)

print(f'''
Foram cadastradas no total {len(pessoas)} pessoas
A média de idade das pessoas cadastradas foi de {mediaIdade:.2f} anos
A lista com todas as mulheres é: ''', end='')
for mulher in pessoas:
    if mulher['sexo'] == 'F':
        print(mulher['nome'], end=', ')
print()
print('A lista com todas as pessoas com idade acima da média é: ', end='')
for maiorMedia in pessoas:
    if maiorMedia['idade'] > mediaIdade:
        print(maiorMedia['nome'], end=', ')
