from time import sleep
s = int(input('Qual o seu salário atual? R$'))
if s>1250:
    ns = s*110/100
else:
    ns = s*115/100
print('Calculando seu aumento...')
sleep(2)
print(f'Seu salário aumentará para R${ns}')
