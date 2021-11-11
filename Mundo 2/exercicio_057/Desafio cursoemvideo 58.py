sexo = input('Informe seu sexo: [M/F] ').strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos, por obséquio informe-os corretamente: [M/F] ')).upper()
print(f'Seu sexo é {sexo}')
 