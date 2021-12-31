def área(l, w): # l = length, w = width
    A = l * w
    print(f'Em um terreno {l}x{w}, sua área total será de {A}m²')


l = float(input('Digite o valor da LARGURA (m): '))
w = float(input('Digite o valor do COMPRIMENTO (m): '))

área(l, w)

