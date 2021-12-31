def escreva(mensagem):
    tamanho = len(mensagem) + 4

    print(f'{"-" * tamanho}')
    print(f'{mensagem:^{tamanho}}')
    print(f'{"-" * tamanho}')
    
    
escreva('Ninniet5670')
escreva('Curso de Python no YouTube')
escreva('CeV')
