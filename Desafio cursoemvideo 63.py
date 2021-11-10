a1 = int(input('Qual o primeiro termo da sua PA? '))
r = int(input('Qual a razão da sua PA? '))
c = 1
#a = a1
t = 2
#a10 = a1 + 9 * r
#while a <= a10:
while c <= 10:
    print(a1, '->', end=' ')
    a1 += r
    #a = a1 + c * r
    c += 1
print('Acabou')

while t != 0:
    t = int(input('Quantos mais termos você aceita ser mostrado? '))
    lt = c + t
    while c < lt:
        print(a1, '->', end=' ')
        a1 += r
        c += 1
    print('Acabou novamente!')
print(f'A progressão foi finalizada com {c - 1} termos mostrados')
