# mano = {'num': 7}
# mano1 = {'num': 8}
# lista = []

# lista.append(mano)
# lista.append(mano1)

# lista.sort()

# print(lista)


from operator import itemgetter
lista = [(2, 1), (1, 2)]
sorted_lista = sorted(lista, key=itemgetter(1), reverse=True)


print(sorted_lista)