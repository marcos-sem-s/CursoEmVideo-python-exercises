from random import randint
from time import sleep

winningNumbers = []
jogosQtd = int(input('Digite quantos jogos serão gerados? '))

for i in range(jogosQtd):
    sortedNumbers = []

    for i in range(6):
        number = randint(1, 61)

        while number in sortedNumbers:
            number = randint(1, 61)

        sortedNumbers.append(number)

    sortedNumbers.sort()
    winningNumbers.append(sortedNumbers)

print('Os números sorteados foram:')
for num in winningNumbers:
    print(num)
    sleep(0.5)
    