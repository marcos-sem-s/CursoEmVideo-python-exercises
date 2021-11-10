cont = 0
cond = True
numeros = []

while cond != 0:
    num = int(input('Digite um número: '))
    numeros.append(num)
    
    cond = int(input('Digite 0 para sair do programa: '))
    cont += 1
    print(numeros)

numeros.sort(reverse=True)

print(f'Foram digitados {cont} números')
print(f'A lista dos valores em ordem decrescente é: {numeros}')
if 5 in numeros:
    print('O valor 5 foi digitado e está na lista')
else:
    print('O valor 5 não foi digitado na lista')
