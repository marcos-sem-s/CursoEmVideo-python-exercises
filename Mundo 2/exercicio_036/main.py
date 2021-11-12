Salario = float(input('Qual o seu salário? R$'))
ValordaCasa = float(input('Qual o valor da casa à venda? R$'))
AnosPag = float(input('Em quantos anos é pretendido financiar a casa? '))
meses = AnosPag*12
Prestacao = ValordaCasa/meses
#Prestacao = (ValordaCasa/meses*Salario)-meses (conta errada?)
print(f'A prestação será de R${Prestacao:.2f}')
if Prestacao > (Salario*0.3): 
    print('Empréstimo negado!')
else:
    print('Seu empréstimo foi aprovado!')
