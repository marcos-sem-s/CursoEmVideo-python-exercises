print('-Calculando a área e quantidade de litros de tinta por 2m²-')
h = float(input('Qual a altura da parede em metros? '))
w = float(input('Qual o seu largura? '))
a = h * w
l = a / 2
print(f'A área total é {a}, como 1 litro de tinta cobre 2m², será necessário {l} Litros de tinta')
