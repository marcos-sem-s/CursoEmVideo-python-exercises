p = h = mm = 0
while True:
    sexo = resp = ' '
    idade = int(input('Qual a idade da pessoa? '))
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F] ')).upper().strip()[0]
    if idade > 18:
        p += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        mm += 1
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    print('-==' * 20)
    if resp == 'N':
        break
print(f'''Dos dados apresentados:
- Há {p} pessoas que tem mais de 18 anos
- Foram cadastrados {h} homens
- Tem {mm} mulheres com menos de 20 anos
''')
