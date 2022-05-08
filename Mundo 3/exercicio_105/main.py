def notas(*notas, situacao=False):
    """
    
    """

    notasGeral = {}

    notasGeral['notasQtd'] = len(notas)
    notasGeral['maiorNota'] = max(notas)
    notasGeral['menorNota'] = min(notas)
    notasGeral['media'] = round(sum(notas) / len(notas), 2)

    if situacao:
        if notasGeral['media'] >= 7:
            notasGeral['situacao'] = 'BOM'
        elif notasGeral['media'] >= 5:
            notasGeral['situacao'] = 'RAZOÁVEL'
        else:
            notasGeral['situacao'] = 'RUIM'

    return notasGeral


escola = notas(5.5, 2.5, 1.5, situacao=True)
print(escola)

escola = notas(5.5, 2.5, 10, 6.5)
print(escola)
