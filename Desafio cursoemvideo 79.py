valores = []
for i in range(5):
    valores.append(int(input(f'Digite o {i+1}° número: ')))

print('Sua lista foi: ', valores)
maior = max(valores)
menor = min(valores)
print(f'O maior valor foi {maior} nas posições: ', end='')
for c, valor in enumerate(valores):
    if valor == maior:
        print(c+1, '...', end='')
print(f'\nO menor valor foi {menor} nas posições: ', end='')
for c, valor in enumerate(valores):
    if valor == menor:
        print(c+1, '...', end='')
