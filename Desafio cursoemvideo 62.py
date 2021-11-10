a1 = int(input('Qual o primeiro termo da sua PA? '))
r = int(input('Qual a razão da sua PA? '))
c = 1
#a = a1
#a10 = a1 + 9 * r
#while a <= a10:
while c <= 10:
    print(a1, '->' , end=' ')
    a1 += r
    #a = a1 + c * r
    c += 1
print('Acabou') 
