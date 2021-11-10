t = 0
for i in range(6):
    n = int(input('Escolha um número: '))
    if n % 2 == 0:
        t += n
print(f'A soma do valor de todos os números pares é: {t}')
