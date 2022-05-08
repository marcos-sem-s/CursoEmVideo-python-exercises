import moeda

preço = float(input('Digite um preço qualquer: R$'))

print(f'''
Aumentando 15% temos: R${moeda.aumentar(preço, 15)}
Diminuindo 30% temos: R${moeda.diminuir(preço, 30)}
O dobro de R${preço} é: R${moeda.dobro(preço)}
A metade de R${preço} é: R${moeda.metade(preço)}
''')
