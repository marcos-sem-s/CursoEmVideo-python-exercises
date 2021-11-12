print('Bem vindo ao Gerenciador de Pagamentos!')
p = float(input('Qual o valor do seu produto? R$'))
print('''Escolha dentre as opções possíveis:
1)Seu produto à vista em dinheiro/cheque terá 10% de desconto
2)À vista no cartão terá 5% de desconto
3)Parcelando em até 2 vezes o preço fica normal
4)Parcelando em 3 ou mais vezes fica com 20% de juros
''')
op = int(input('Qual sua opção? '))
if op == 1:
    print(f'Você terá 20% de desconto, pagando R${p*0.90}')
elif op == 2:
    print(f'Você terá 5% de desconto, pagando R${p*0.95}')
elif op == 3:
    print('Você pagará o valor normal do produto')
else:
    juro = p*1.20
    par = int(input('Quantas vezes desejas parcelar? '))
    print(f'O montante total terá 20% de juros, pagando no total R${juro}')
    print(f'Cada parcela será de R${(juro)/par}')
