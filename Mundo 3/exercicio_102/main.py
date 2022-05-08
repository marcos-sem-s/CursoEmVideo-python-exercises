def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um numero
    : parametro numero : O numero a ser calculado
    : parametro show : (opcional) Mostra ou nao a conta
    : return : O valor do fatorial de 'numero'
    """

    fatorialNum = 1
    numeros = ''

    for numero in range(numero, 0, -1):
        if show == True:
            numeros += str(numero)
            if numero > 1:
                numeros += ' * '
            else:
                numeros += ' = '
            
        fatorialNum *= numero
    
    return numeros + str(fatorialNum)
    

print(fatorial(5))
# help(fatorial)
