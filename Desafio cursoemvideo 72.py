v = int(input('Qual o valor a ser sacado? R$'))
print('-==' * 15)
c50 = c20 = c10 = c1 = 0
while v >= 50:
    c50 += 1
    v -= 50
while v >= 20:
    c20 += 1
    v -= 20
while v >= 10:
    c10 += 1
    v -= 10
while v >= 1:
    c1 += 1
    v -= 1
print(f'''No total foram:
{c50} cédulas de R$50
{c20} cédulas de R$20
{c10} cédulas de R$10
{c1} cédulas de R$1''')
print('-==' * 15)
