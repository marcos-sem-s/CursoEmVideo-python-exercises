p1 = int(input('Qual o primeiro termo da sua Progressão Aritmética? '))
r = int(input('Qual a razão da sua PA? '))
p10 = p1 + r * 9
print('Os primeiros 10 termos desta PA serão: ')
for i in range(p1, p10 + 1, r):
    print(f'{i} -> ', end='')
print('Acabou')
