km = int(input('Qual a distância em km da sua viagem? '))
if km <= 200:
    p = float(km * 0.5)
else:
    p = float(km * 0.45)
print(f'Sua viagem irá custar R${p}')
