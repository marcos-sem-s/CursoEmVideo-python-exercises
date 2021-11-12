from datetime import date
ano = date.today().year
gen = input('Qual seu gênero? ')
alist = int(input('Em qual ano você nasceu? '))
idade = ano - alist

if gen == 'homem' or gen == 'masculino':
    print(f'Quem nasceu em {alist} tem {idade} anos em {ano}')
    if idade < 18:
        print(f'Faltam {18-idade} anos se alistar ao servço militar')
        print(f'Seu ano de alistamento será {alist+18}')
    elif idade == 18:
        print('Parabéns! É o seu ano de alistamento!')
    else:
        print(f'Sua idade para o prazo do alistamento excedeu {idade-18} anos')
        print(f'Você deveria ter se alistado em {alist+18}')
elif gen == 'feminino' or gen == 'mulher':
    print(f'Quem nasceu em {alist} tem {idade} anos em {ano}')
    print('Mulher não precisa se alistar obrigatoriamente, boa tarde.')
