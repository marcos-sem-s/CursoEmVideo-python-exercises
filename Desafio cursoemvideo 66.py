num = []
c = 1
n = int(input('Digite um número: '))
r = str(input('Deseja continuar o progrma? [S/N] ')).upper()
num.append(n)
while r == 'S':
    n = int(input('Digite outro número: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
    c += 1
    num.append(n)

print(f'A média dos {c} números digitados será {sum(num)/c}')
print(f'O maior número será {max(num)}, e o menor será {min(num)}')
