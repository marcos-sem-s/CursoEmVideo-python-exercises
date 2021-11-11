d = int(input('Por quantos dias o carro foi alugado? '))
Km = float(input('Quantos quilômetros ele percorreu? '))
P = (d * 60) + (Km * 0.15)
print(f'O preço a ser pago é de R${P:.2f}')