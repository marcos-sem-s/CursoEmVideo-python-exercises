from random import shuffle
i1 = str(input('Primeiro nome: '))
i2 = str(input('Segundo nome: '))
i3 = str(input('Terceiro nome: '))
i4 = str(input('Quarto nome: '))
list = [i1, i2, i3, i4]
shuffle(list)
print(list)
