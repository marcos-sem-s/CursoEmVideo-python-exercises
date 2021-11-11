print('-$-' * 13)
print('Programa de conversão Real para Dólar \n Dados de 29/12/2019, 1US$ = R$4,05')
r = float(input('Quanto de dinheiro em Reais você possui? R$'))
pc = r / 4.05 
print(f'Com o seu dinheiro atual, é possível converter seus R${r} em {pc:.2f} US$')
