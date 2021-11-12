esc = 0
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: ')) 
while esc != 5:
    esc = int(input('''
[1] Somar
[2] Multiplicar
[3] Qual o maior?
[4] Novos números
[5] Sair do programa
Escolha uma das ações acima: '''))
    if esc == 1:
        print(f'O resultado da soma será: {n1 + n2}')
    elif esc == 2:
        print(f'O resultado da multiplicação será: {n1 * n2}')
    elif esc == 3:
        print(f'O maior número entre ambos será o: {max(n1, n2)}')
    elif esc == 4:
        n1 = float(input('Escolha um novo número: '))
        n2 = float(input('Escolha outro número novo: '))
    else:
        print('Opção inválida, tente novamente')
    print('=-' * 20)
print('Encerrando programa...')
