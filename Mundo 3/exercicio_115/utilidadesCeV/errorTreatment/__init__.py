def mainMenu_EH(choice):
    if not choice.isnumeric():
        print('ERRO! Digite um número inteiro válido.')
    elif choice not in '123':
        print('ERRO! Digite uma das opções acima.')
    else:
        return int(choice)
        