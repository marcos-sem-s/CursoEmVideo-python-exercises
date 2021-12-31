from time import sleep

def maior(numeros):
    if len(numeros) == 0:
        maiorVar = 0
    else:
        for c, num in enumerate(numeros):
            if c == 0:
                maiorVar = num
            else:
                if num > maiorVar:
                    maiorVar = num
    print('-=' * 20)
    print(f'Foram informados {len(numeros)} valores: ', end='', flush=True)
    for num in numeros:
        sleep(0.5)
        print(num, end=', ', flush=True)
    print(f'\nO maior número foi o {maiorVar}')


lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)

    choice = input('Digite 0 para sair do loop: ')
    if choice == '0':
        break

maior(lista)
