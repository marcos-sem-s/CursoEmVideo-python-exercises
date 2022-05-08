from datetime import datetime

def voto(idade):
    if idade >= 18:
        return 'OBRIGATÓRIO'
    if idade >= 16:
        return 'OPCIONAL'
    else:
        return 'NEGADO'


idadeVar = datetime.now().year - int(input('Digite seu ano de nascimento: '))

print(f'Com {idadeVar} anos, seu tipo de voto nas eleiões é {voto(idadeVar)}')
