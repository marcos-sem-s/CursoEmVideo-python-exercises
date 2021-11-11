cv = int(input('Qual a velocidade do seu carro? '))
al = cv - 80
m = al * 7
if cv > 80:
    print(f'Seu carro foi multado em R${m} po estar {al}km acima do limite')
else:
    print('A velocidade do seu carro está normal, parabéns')
    