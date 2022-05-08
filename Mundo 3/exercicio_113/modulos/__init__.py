def leiaInt():
    while True:
        try:
            num = int(input('Digite um número: '))
        except (TypeError, ValueError):
            print('\033[1;31mValor inválido\033[m')
            continue
        else:
            return num


def leiaFloat():
    while True:
        try:
            num = float(input('Digite um número em decimal: ').replace(',', '.').strip())
        except (TypeError, ValueError):
            print('\033[1;31mValor inválido\033[m')
            continue
        else:
            return num
