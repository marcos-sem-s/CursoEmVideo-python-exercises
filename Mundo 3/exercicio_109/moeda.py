def aumentar(num, tax, cond=False):
    numero =  num * (tax + 100)/100

    if cond == True:
        return moeda(numero)
    else:
        return numero


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
