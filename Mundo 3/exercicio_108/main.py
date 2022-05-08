import moeda

preço = float(input('Digite um preço qualquer: R$'))

print(f'''
Aumentando 15% temos: {moeda.moeda(moeda.aumentar(preço, 15))}
Diminuindo 30% temos: {moeda.moeda(moeda.diminuir(preço, 30))}
O dobro de {moeda.moeda(preço)} é: {moeda.moeda(moeda.dobro(preço))}
A metade de {moeda.moeda(preço)} é: {moeda.moeda(moeda.metade(preço))}
''')
