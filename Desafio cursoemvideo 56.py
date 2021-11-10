pesos = []
for i in range(1, 6):
    p = int(input(f'Qual o peso da {i}° pessoa? '))
    pesos.append(p)
pesos.sort()
#print(pesos)
print(f'O maior peso medido foi {pesos[4]}, e o menor peso foi {pesos[0]}')
