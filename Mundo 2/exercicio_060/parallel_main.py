n = int(input('Escolha um número para calcularmos seu fatorial: '))
v = 1
for i in range(1, n + 1):
    v *= i
print(f'O resultado de {n}! será {v}')
