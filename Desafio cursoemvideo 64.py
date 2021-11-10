elem = int(input('Quantos elementos de Fibonacci você deseja vizualizar? '))
c = 0
Fibo = [0, 1]
if elem == 1:
    print('[0]')
elif elem == 0:
    print('Nada')
else:
    while c < elem - 2:
        newv = Fibo[c] + Fibo[c+1]
        Fibo.append(newv)
        c += 1
    print(Fibo)
