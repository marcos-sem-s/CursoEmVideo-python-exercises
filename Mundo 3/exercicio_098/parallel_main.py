def contador(inicio, fim, intervalo):
    if intervalo == 0:
        intervalo = 1
    if inicio > fim:
        aux = -1

        if intervalo < 0:
            interval = intervalo * -1
        else:
            interval = intervalo
            intervalo *= -1
    else:
        aux = +1
        interval = intervalo

    print(f'Contagem de {inicio} até {fim} de {interval} em {interval}')
    for i in range(inicio, fim + aux, intervalo):
        print(i, end=' ')
    print()

contador(1, 10, 1)
contador(10, 0, -2)

inicioVar = int(input('Digite o início da contagem: '))
fimVar = int(input('Digite o fim da contagem: '))
intervaloVar = int(input('Digite o intervalo da contagem: '))
contador(inicioVar, fimVar, intervaloVar)
