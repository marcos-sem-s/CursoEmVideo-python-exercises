comidas = ('Banana', 3.00, 'Maçã', 4.00, 'Laranja', 2.00, 'Pitaya', 15.00, 'Tomate', 3.50)
local = 'Mercadinho do seu Zé'

print('-=-'*15)
print(f'{local:^45}')
print('-=-'*15)

for cont in range(0, len(comidas)):
    if cont % 2 == 0:
        print(f'{comidas[cont]:.<36}', end='')
    else:
        print(f'R${comidas[cont]:>6}')
