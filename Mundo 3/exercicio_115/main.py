from utilidadesCeV.menu import *
from utilidadesCeV.archivesFunc import *
from utilidadesCeV.errorTreatment import *


if __name__ == '__main__':
    file = 'Mundo 3/exercicio_115/registration.txt'

    if fileExists(file):
        print('Arquivo encontrado!')
    else:
        fileCreate(file)

    while True:
        main_menu()
        choice = mainMenu_EH(input('Digite sua opção: '))

        if choice == 1:
            fileRead(file)

        elif choice == 2:
            fileAdd(file)

        elif choice == 3:
            exit_program() 
            break
