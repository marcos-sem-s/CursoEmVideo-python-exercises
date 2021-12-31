from datetime import date

pessoa = {
    'nome': input('Digite seu NOME: ').capitalize(),
    'idade': (date.today().year - int(input('Digite seu ANO DE NASCIMENTO: '))),
    'ctps': int(input('Digite seu número de CARTEIRA DE TRABALHO: [0 caso não tenha] ')),
}

if pessoa['ctps'] != 0:
    pessoa['ano de contratação'] = int(input('Qual seu ano de contratação? '))
    pessoa['salario'] = float(input('Qual seu salário? R$'))


print(f'''
O nome da pessoa é {pessoa['nome']}
Sua idade é de {pessoa['idade']} anos
Seu CTPS tem o valor de {pessoa['ctps']}''')
if pessoa['ctps'] != 0:
    pessoa['aposentadoria'] = ((pessoa['ano de contratação'] + 35) - date.today().year) + pessoa['idade']

    print(f'''Sua data de contratação é do ano de {pessoa['ano de contratação']}
Seu salário é de R${pessoa['salario']}
Esta pessoa irá se aposentar com {pessoa['aposentadoria']} anos
''')
