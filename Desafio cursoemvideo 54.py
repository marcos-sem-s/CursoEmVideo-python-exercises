p = str(input('Digite alguma frase ou palavra: ')).replace(' ', '')

c = p[::-1]
print(f'o inverso de {p} é: \n{c}')

#for i in p[::-1]:

if p == c:
    print('Esta frase/palavra é um palíndromo!')
else:
    print('Esta é uma frase normal')
