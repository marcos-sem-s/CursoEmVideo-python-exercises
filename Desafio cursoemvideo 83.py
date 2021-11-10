numeros = []
pares = []
impares = []
cond = True

while cond != 0:
    num = int(input('Digite um número: '))
    numeros.append(num)

    cond = int(input('Digite 0 para sair do programa: '))

# a pedido do guanabara:
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('Os valores digitados foram: ', numeros)
print('Os valores pares digitados foram: ', pares)
print('Os valores impares digitados foram: ', impares)
