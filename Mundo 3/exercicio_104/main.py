def leiaInt(num):
    num = input('Digite um número: ')
    while not num.isnumeric():
        num = input('Digite um número válido: ')

    return num


numero = leiaInt('Digite um número: ')
print(f'Você digitou o número {numero}')
