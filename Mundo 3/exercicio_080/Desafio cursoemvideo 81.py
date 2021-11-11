numeros = []
num = int(input('Digite um número: '))
numeros.append(num)

for c in range(4):
    cond = False
    num = int(input('Digite um número: '))

    for cont, n in enumerate(numeros):
        if num <= n:
            cond = True
            numeros.insert(cont, num)
            break
    if cond == False:
        numeros.append(num)

    print(numeros)
