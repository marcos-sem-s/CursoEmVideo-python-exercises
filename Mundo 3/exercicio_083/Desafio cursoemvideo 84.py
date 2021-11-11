operacao = str(input('Digite uma expressão matemática com parênteses: '))
parentesesL = []

for elem in operacao:
    if elem == '(' or elem == ')':
        parentesesL.append(elem)

parenteses = ''.join(parentesesL)
parenteses.replace('()', '')

print(parentesesL, parenteses)

if len(parentesesL) > 0:
    if len(parenteses) == 0:
        print('A Expressão matemática pode ser efetuada')
    else:
        print('A Expressão matemática não pode ser efetuada')
else:
    print('A expressão matemática não teve nem um parênteses')
