n1 = int(input('Digite o valor da primeira linha: '))
n2 = int(input('Segunda linha: '))
n3 = int(input('Terceira linha: '))
if (n1+n2)>n3 and (n1+n3)>n2 and (n2+n3)>n1:
    print('Com os comprimento supracitados, é possível formar um triângulo')
else:
    print('Com os comprimentos supracitados, não é possível formar um triângulo')
