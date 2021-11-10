l1 = int(input('Qual a medida do 1° lado? '))
l2 = int(input('Qual a medida do 2° lado? '))
l3 = int(input('Qual a medida do 3° lado? '))
if (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1:
    print('É possível a criação de um triângulo')
    if l1 == l2 == l3:
        print('Seu triângulo é um equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Seu triângulo é um isósceles')
    else:
        print('Seu triângulo é um escaleno')
else:
    print('Impossível fazer um triângulo com tais medidas')
