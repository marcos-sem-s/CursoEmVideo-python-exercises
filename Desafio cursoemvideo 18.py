from math import pow,sqrt,hypot 
c1 = float(input('Qual o primeiro cateto? '))
c2 = float(input('Qual o segundo cateto? '))
h = sqrt(pow(c1, 2) + pow(c2, 2)) #h = hypot(c1, c2)
print(f'O valor da hipotenusa é {h:.2f}')

