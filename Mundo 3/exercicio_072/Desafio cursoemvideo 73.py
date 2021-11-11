extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'desenove', 'vinte')
resp = 1

while resp == 1:
    num = int(input('Escolha um número de um a vinte: '))
    while (0 <= num <= 20) == False:
        num = int(input('Número indisponível, escolha novamente um número de um a vinte: '))

    print(f'Seu número em extenso será: {extenso[num]}')
    resp = int(input('Deseja continuar? [1 para continuar] '))

print('Fim do programa')
