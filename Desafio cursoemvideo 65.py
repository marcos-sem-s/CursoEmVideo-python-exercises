n = t = c = 0
while n != 999:
    n = int(input('Digite qualquer número exceto 999 para continuar o programa: '))
    if n != 999:
        c += 1
        t += n
'''if c == t == 0:
    print('Você não digitou nada')
else:'''
print(f'Você digitou {c} números e suas somas dão {t}')
