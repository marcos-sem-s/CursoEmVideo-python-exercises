from random import randint
c = 0
while True:
    v = int(input('Digite um valor: '))
    e = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    vc = randint(0, 10)
    soma = v + vc
    while e != 'P' and e != 'I':
        e = str(input('Escolha inválida. Par ou Ímpar? [P/I]')).upper().strip()[0]
    print(f'Você escolheu {v} e o computador {vc}. Total {soma}, dando ', end='')
    print('PAR' if soma % 2 == 0 else 'ÍMPAR')
    print('-==' * 20)
    if e == 'P' and soma % 2 == 0:
        print('Parabéns! Você venceu. Vamos jogar novamente ..')
    elif e == 'I' and soma % 2 == 1:
        print('Parabéns! Você venceu. Vamos jogar novamente ..')
    else:
        break
    print('-==' * 20)
    c += 1
print(f'Você perdeu!\nGAME OVER! Você venceu {c} vezes')
