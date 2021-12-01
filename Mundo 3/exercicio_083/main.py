operacao = str(input('Digite uma expressão matemática com parênteses: '))
parentesesL = []
contadorBarraEsquerda = 0
contadorBarraDireta = 0
isValid = False

for elemento in operacao:
    if elemento == '(':
        contadorBarraEsquerda += 1
    elif elemento == ')':
        contadorBarraDireta += 1

    if contadorBarraDireta > contadorBarraEsquerda:
        isValid = False
        break
    elif contadorBarraDireta == contadorBarraEsquerda:
        isValid = True
if contadorBarraDireta < contadorBarraEsquerda:
    isValid = False

if isValid:
    print('Sua operação matemática É válida')
else:
    print('Sua operação matemática NÃO é válida')
