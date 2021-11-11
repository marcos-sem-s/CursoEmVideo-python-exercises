n1 = float(input('Qual a sua primeira nota? '))
n2 = float(input('Qual a sua segunda nota? '))
m = (n1+n2)/2
if m < 5:
    print('Sua média foi {m:.1f}, menor que 5, você está reprovado!')
elif 6.9 > m >=5:
    print('Sua média foi {m:.1f}, abaixo de 7, recuperação!')
else:
    print('Sua média foi{m:.1f}, acima ou igual a 7, aprovado!')
