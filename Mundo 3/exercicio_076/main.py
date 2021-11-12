comidas = (('Banana', 3.00), ('Maçã', 4.00), ('Laranja', 2.00), ('Pitaya', 15.00), ('Tomate', 3.50))
local = 'Mercadinho do seu Zé'

print('-=-'*15)
print(f'{local:^45}')
print('-=-'*15)

for fruta, preço in comidas:
    print(f'{fruta:.<36}R${preço:>6}')

print('-=-'*15)
