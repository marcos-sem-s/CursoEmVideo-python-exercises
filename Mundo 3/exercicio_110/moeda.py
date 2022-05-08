def aumentar(num, tax, cond=False):
    numero =  num * (tax + 100)/100

    if cond == True:
        return moeda(numero)
    else:
        return numero
    # return moeda(numero) if cond is True else numero


def diminuir(num, tax, cond=False):
    numero =  num * (100 - tax)/100

    if cond == True:
        return moeda(numero)
    else:
        return numero


def dobro(num, cond=False):
    numero =  num * 2

    if cond == True:
        return moeda(numero)
    else:
        return numero


def metade(num, cond=False):
    numero =  num / 2

    if cond == True:
        return moeda(numero)
    else:
        return numero


def moeda(num):
    return f'R${num}'


def resumo(num, taxPlus, taxMinus):
    print(f'''
    {f'Aumentando {taxPlus}% temos:':<25} {aumentar(num, taxPlus, True)}
    {f'Diminuindo {taxMinus}% temos:':<25} {diminuir(num, taxMinus, True)}
    {f'O dobro de {num} é:':<25} {dobro(num, True)}
    {f'A metade de {num} é:':<25} {metade(num, True)}
    ''')
