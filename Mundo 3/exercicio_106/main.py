def escreva(mensagem):
    tamanho = len(mensagem) + 4

    print(f'{"-" * tamanho}')
    print(f'{mensagem:^{tamanho}}')
    print(f'{"-" * tamanho}')

def ajuda(func):
    escreva(f'Acessando o manual para {func}:')
    help(func)


resp = 0

escreva('SISTEMINHA DE AJUDA DO PYTHON')

while True:
    resp = input('Digite o que deseja saber sobre o Python: ')
    if resp == 'FIM':
        break

    ajuda(resp)
