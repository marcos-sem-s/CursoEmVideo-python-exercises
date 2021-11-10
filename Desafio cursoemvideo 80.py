cond = True
valores = []
num = 0

while cond != False:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado!')
        print('-=' * 10)
    else:
        print('Valor já presente na lista, portanto, não adicionado')
        print('-=' * 10)
    
    cond = int(input('Digite 0 para sair: '))

print('Programa finalizado, sua lista sorteada será: ')
print(sorted(valores))
