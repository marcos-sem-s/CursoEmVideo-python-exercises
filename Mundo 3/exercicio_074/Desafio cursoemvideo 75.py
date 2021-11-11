from random import randint

num1 = randint(0, 100)
num2 = randint(0, 100)
num3 = randint(0, 100)
num4 = randint(0, 100)
num5 = randint(0, 100)
numeros = (num1, num2, num3, num4, num5)

print(f'A lista de números aleatórios será: {numeros}')
print(f'O maior número será {max(numeros)} e o menor será {min(numeros)}')
