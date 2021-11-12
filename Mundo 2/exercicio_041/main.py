from datetime import date
print('Confederação Nacional de Natação! Cheque sua categoria segundo sua idade!')
ani = int(input('Digite seu ano de aniversário: '))
ano = date.today().year - ani
print(f'O atleta tem {ano} anos')
etc = 'Sua categoria será'
if ano <= 9:
    print(f'{etc} mirim!')
elif ano < 14:
    print(f'{etc} infantil!')
elif ano < 20:
    print(f'{etc} junior!')
elif ano == 20:
    print(f'{etc} sênior!')
else:
    print(f'{etc} master!')
 