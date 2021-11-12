valores = ( int(input('Digite 1° número: ')),
            int(input('Digite 2° número: ')),
            int(input('Digite 3° número: ')),
            int(input('Digite 4° número: ')))
pares = []

cont9 = 0

for i in valores:
    if i == 9:
        cont9 += 1
    if i % 2 == 0:
        pares.append(i)

print(f'O número 9 apareceu {cont9} vez') # .count()
if 3 in valores:
    print(f'O primeiro 3 apareceu na {valores.index(3) + 1}° posição')
else:
    print('O número 3 não aparece')
print('Os números pares foram: -', pares)
