def voto(ano):
    from datetime import datetime
    
    idade = datetime.now().year - ano
    if idade >= 18:
        return f'Com {idade} anos, seu voto é OBRIGATÓRIO'
    if idade >= 16:
        return f'Com {idade} anos, seu voto é OPCIONAL'
    else:
        return f'Com {idade} anos, seu voto é NEGADO'

    
ano = int(input('Digite seu ano de nascimento: '))
print(voto(ano))
