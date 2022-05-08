def leiaMoney():
    num = input('Digite um valor em dinheiro: ').replace(',', '.').strip()

    while num.isalpha() or (num == ''):
        num = input('Digite um valor em dinheiro VÁLIDO: ').replace(',', '.').strip()

    return float(num)
