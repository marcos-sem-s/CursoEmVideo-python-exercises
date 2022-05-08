import moeda

preço = float(input('Digite um preço qualquer: R$'))

print(f'''
Aumentando 15% temos: {moeda.aumentar(preço, 15, True)}
Diminuindo 30% temos: {moeda.diminuir(preço, 30, True)}
O dobro de {moeda.moeda(preço)} é: {moeda.dobro(preço, True)}
A metade de {moeda.moeda(preço)} é: {moeda.metade(preço, True)}
''')
