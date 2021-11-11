idade = [10, 50, 3]
sexo =  ['F', 'F', 'M']
nome = ['a', 'b', 'c']
mulherm = 0
c = 0

maior_idade = max(idade)
#print(maior_idade)
for i in sexo:
    if i == 'M' and idade[c] == maior_idade:
        esc = c
        print(esc)
    print(c)
    c += 1

'''for i in sexo:
    if i == 'F' and idade[c] < 20:
        mulherm +=1
    c += 1
print(c)
print(mulherm)'''
