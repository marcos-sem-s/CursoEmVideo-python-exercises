fn = 1
n1 = n = int(input('Escolha um número para calcularmos seu fatorial: '))
while n != 0:
    fn *= n
    n -= 1
print(f'O resultado de {n1}! é {fn}')
