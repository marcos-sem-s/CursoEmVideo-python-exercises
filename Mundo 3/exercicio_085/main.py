pares = []
impares = []
numeros = []

for i in range(7):
    num = int(input('Digite um número: '))

    if num % 2:
        impares.append(num)
    else:
        pares.append(num)

pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])

print(f'Os valores pares em ordem crescente foram: {numeros[0]}')
print(f'Os valores impares em ordem crescente foram: {numeros[1]}')
