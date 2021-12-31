aluno = {}

aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = float(input('Digite qual a sua média escolar: '))

if aluno['media'] < 5:
    aluno['situação'] = 'REPROVADOO'
elif aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'APROVADO'

print(
f'''
O nome do aluno é {aluno['nome']}
Sua média foi {aluno['media']}
E a sua situação é {aluno['situação']}
''')
