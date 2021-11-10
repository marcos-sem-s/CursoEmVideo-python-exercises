n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1>n2 and n1>n3:
    print(f'O {n1} é o maior')
elif n2>n1 and n2>n3:
    print(f'O {n2} é o maior')
else:
    print(f'O {n3} é o maior')

if n1<n2 and n1<n3:
    print(f'O {n1} é o menor')
elif n2<n1 and n2<n3:
    print(f'O {n2} é o menor')
else:
    print(f'O {n3} é o menor')
    