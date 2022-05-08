from utilidadesCeV.menu import escreva
from utilidadesCeV.errorTreatment import *


def fileExists(file):
    try:
        fileFinal = open(file, 'rt')
        fileFinal.close()
    except:
        return False
    else:
        return True


def fileCreate(file):
    try:
        fileFinal = open(file, 'wt+')
        fileFinal.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')


def fileRead(file):
    try:
        fileFinal = open(file, 'rt')
    except:
        print('ERRO! Não foi possível abrir o arquivo')
    else:
        escreva('Usuários Cadastrados')
        
        print(f'NOME                               IDADE')
        for i in fileFinal.readlines():
            id = i.split(';')

            print(f'{id[0]:<37}{id[1]:>3}', end='')
    fileFinal.close()
    print()


def fileAdd(file):    
    try:
        fileFinal = open(file, 'at')
    except:
        print('ERRO! Não foi possível abrir o arquivo')
    else:
        escreva('Cadastrando Usuário')
    
        name = input('Digite seu NOME: ')
        if  name.isnumeric():
            print('ERRO! Foi digitado um valor inválido para NOME')
            print('Cadastro cancelado')
            return 0
            
        age = input('Digite sua IDADE: ')
        if not age.isnumeric():
            print('ERRO! Foi digitado um valor inteiro inválido para IDADE')
            print('Cadastro cancelado')
            return 0

        if len(age) > 3:
            print('ERRO! Convenhamos que não existe ser humano vivo com mais de 3 casas decimais')
            print('Cadastro cancelado')
            return 0

        fileFinal.write(name + ';') # checar se há erro nesta parte
        fileFinal.write(age + '\n') # checar se há erro nesta parte
        print('Cadastro efetuado com sucesso')
        