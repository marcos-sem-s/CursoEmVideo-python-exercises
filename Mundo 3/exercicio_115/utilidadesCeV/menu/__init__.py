def escreva(mensagem):
    print(f'{"-" * 40}')
    print(f'{mensagem:^{40}}')
    print(f'{"-" * 40}')


def main_menu():
    escreva('MAIN MENU')
    print(
f'''1 - Ver usuários cadastrados
2 - Cadastrar novo usuário
3 - Sair do sistema''')
    print('-' * 39)
    
    
def exit_program():
    escreva('Saindo do sistema...')
