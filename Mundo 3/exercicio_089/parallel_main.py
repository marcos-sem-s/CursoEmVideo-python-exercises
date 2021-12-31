boletim = []

while True:
    nome = input('Digite o nome de um aluno: ')
    nota1 = float(input('Digite o valor da primeira nota: '))
    nota2 = float(input('Digite o valor da segunda nota: '))

    media = (nota1 + nota2) / 2

    boletim.append([nome, [nota1, nota2], media])
    choice = int(input('Digite "-1" para sair: '))
    if choice == -1:
        break

print('-=' * 15)
print(f"{'Nº':<7}{'NOME':<15}{'MÉDIA'}")

for c in range(len(boletim)):
    print(f"{c:<7}{boletim[c][0]:<15}{round(boletim[c][2], 2)}")

while True:  
    choice = int(input('Digite o número do aluno para mostrar suas notas ["-1" para sair]: '))
    if choice == -1:
        break
    elif choice in range(len(boletim)):
        print(f'As notas de {boletim[choice][0]} foram: {boletim[choice][1]}')
    else:
        print('Não existe aluno correspondente ao número, tente novamente')

print('Programa finalizado.')
