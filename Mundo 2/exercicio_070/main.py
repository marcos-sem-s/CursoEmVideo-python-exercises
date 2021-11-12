c = total = co = 0
while True:
    resp = ' '
    nome = str(input('Qual o nome do produto? '))
    preço = float(input('Qual seu preço? R$'))
    if co == 0 or preço < mpreço:
        mnome = nome
        mpreço = preço
    '''else:
        if preço < mpreço:
            mnome = nome'''
    co += 1
    total += preço
    if preço > 1000:
        c += 1
    while resp not in 'SN':
        resp = str(input('Você deseja conitnuar o programa? [S/N] ')).upper().strip()[0]
    print('-=' * 20)
    if resp == 'N':
        break 
print(f'''
- O total gasto na compra foi de R${total}
- Há {c} produtos acima de R$1000 na lista
- O nome do produto mais barato é {mnome}, custando R${mpreço}
''')
