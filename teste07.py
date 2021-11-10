mulherm = 0
sexo = ['masculino', 'feminino', 'masculino', 'feminino']
idade = [17, 11, 55, 49]
nome = ['a', 'b', 'c', 'd']
homensl = []

for i in sexo:
    if i == 'feminino':
        Sposition = sexo.index(i)
        if idade[Sposition] < 20:
            mulherm+=1

print(mulherm)
'''for i in sexo:
    if i == 'masculino':
        Hposition = sexo.index('masculino')
        print(idade[Hposition])'''
