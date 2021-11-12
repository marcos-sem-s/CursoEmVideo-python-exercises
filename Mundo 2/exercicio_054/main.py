from datetime import date
M = 0
for i in range(1, 8):
    n = int(input(f'Qual o ano de nascimento da {i}° pessoa? '))
    n = date.today().year - n
    if n>=21:
        M+=1

m = 7 - M
print(f'Há {M} adultos e {m} menores de idade no grupo')
