from time import sleep

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
    print('FIM')
    print('-=' * 15)
    sleep(2)


contador(1, 10, 1)
contador(10, 0, -2)

valores = input('Digite o início, fim e o intervalo respectivamente (separados por um espaço): ').split()
inicioVar, fimVar, intervaloVar = map(int, valores)
contador(inicioVar, fimVar, intervaloVar)
