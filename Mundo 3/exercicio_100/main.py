from random import randint

números = []

def sorteia(lista):
    for c in range(5):
        randonNumber = randint(0, 100)
        lista.append(randonNumber)

    print(f'Os números sorteados foram: {números}')

    somaPar(números)

def somaPar(lista):
    evenSum = 0
    for num in lista:
        if num % 2 == 0:
            evenSum += num
    
    print(f'A soma dos números pares foi de {evenSum}')


sorteia(números)
