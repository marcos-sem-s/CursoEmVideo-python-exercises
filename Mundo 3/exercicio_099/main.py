from time import sleep

def maior(*numeros):
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
        print(num, end=', ', flush=True)
        sleep(0.5)
    print(f'\nO maior número foi o {maiorVar}')


maior(0, 7, 6, 5, 3, 1)
maior(4, 2, 1)
maior(6, 9)
maior()
