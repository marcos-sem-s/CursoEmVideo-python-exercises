boletim = []

while True:
    join = []
    nome = []
    notas = []

    nome.append(input('Digite o nome de um aluno: '))
    notas.append(float(input('Digite o valor da primeira nota: ')))
    notas.append(float(input('Digite o valor da segunda nota: ')))

    join.append(nome)
    join.append(notas)

    boletim.append(join)

    choice = int(input('Digite "-1" para sair: '))
    if choice == -1:
        break

print('-=' * 15)
print(f"{'Nº':<7}{'NOME':<15}{'MÉDIA'}")

for c in range(len(boletim)):
    print(f"{c:<7}{boletim[c][0][0]:<15}{(round(((boletim[c][1][0] + boletim[c][1][1])/2), 1))}")

while True:  
    choice = int(input('Digite o número do aluno para mostrar suas notas ["-1" para sair]: '))
    if choice == -1:
        break
    elif choice in range(len(boletim)):
        print(f'As notas de {boletim[choice][0][0]} foram: {boletim[choice][1]}')
    else:
        print('Não existe aluno correspondente ao número, tente novamente')

print('Programa finalizado.')
