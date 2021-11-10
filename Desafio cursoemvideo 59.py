from random import choice
ce = 1
sn = choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
#usar randint() seria muito melhor e prático
cn = int(input('Escolha um número entre 0 e 10: '))
if cn == sn:
    print('Parabéns! você acertou de primeira!')
else:
    while cn != sn:
        if cn < sn:
            cn = int(input('Mais... tente novamente: '))
        else:
            cn = int(input('Menos... tente novamente: '))
        ce += 1
print(f'Você finalmente acertou! foram {ce} tentativas até o chute correto.')
