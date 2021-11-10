p = float(input('Qual o seu peso? '))
a = float(input('Qual sua altura? '))
imc = p/(a**2)

if imc < 18.5:
    print('Você está abaixo do peso')
elif 25 > imc >=18.5:
    print('Você está com o peso ideal, parabéns')
elif 30 > imc >=25:
    print('Você está com sobrepeso')
elif 40 > imc >=30:
    print('Você está com obesidade, cuidado!')
else:
    print('Você está com obesidade mórbida, procura ajuda médica imediatemente!')
