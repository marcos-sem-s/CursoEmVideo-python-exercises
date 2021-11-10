num = int(input('Digite um número: '))
print('''Selecione o número para conversão:
1) Binário
2) Octal
3) Hexadecimal
''')
op = int(input('Digite: '))

if op == 1:
    print('Seu número será:', bin(num)[2:])
elif op == 2:
    print('Seu número será:', oct(num)[2:])
else:
    print('Seu número será:', hex(num)[2:])
