while True:
    n = int(input('Você deseja ver a tabuada de qual número? '))
    if n < 0:
            break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('-==' * 20)
print('Programa tabuada encerrado')
