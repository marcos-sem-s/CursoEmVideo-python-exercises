H = int(input('Quantos homens compareceram à festa? '))
M = int(input('Quantas mulheres compareceram à festa? '))

def mdc(H, M):
    while M !=0:
        resto = H % M
        H,M = M,resto 

    return H

print(mdc(H, M))
