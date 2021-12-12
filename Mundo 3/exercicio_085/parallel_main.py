numeros = [[], []]

for i in range(7):
    num = int(input('Digite um número: '))

    if num % 2:
        numeros[1].append(num)
    else:
        numeros[0].append(num)

numeros[0].sort()
numeros[1].sort()

print(f'Os valores pares em ordem crescente foram: {numeros[0]}')
print(f'Os valores impares em ordem crescente foram: {numeros[1]}')
