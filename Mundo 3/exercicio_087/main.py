matriz = [[], [], []]
somaPares = 0
soma3Coluna = 0
maiorValor2Linha = 0

for i in range(3):
    for j in range(3):
        matriz[i].append(int(input('Digite um número: ')))

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()

for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]

for i in range(3):
    soma3Coluna += matriz[i][2]

for i in range(3):
    if matriz[1][i] > maiorValor2Linha:
        maiorValor2Linha = matriz[1][i]

print(f'A soma dos valores pares é {somaPares}')
print(f'S soma dos valores da terceira coluna é {soma3Coluna}')
print(f'O maior valor da segunda linha é: {maiorValor2Linha}')
