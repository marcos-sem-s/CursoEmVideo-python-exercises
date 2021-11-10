nome = []
idade = []
sexo =  []
idadeh = []
mulherm = 0
c1 = 0
c2 = 0
c3 = 0

for i in range(1, 5):
    n = str(input(f'Qual o nome da {i}° pessoa? '))
    d = int(input(f'Qual a idade dessa pessoa? '))
    s = str(input(f'Qual seu sexo? (M/F) ')).upper()
    nome.append(n)
    idade.append(d)
    sexo.append(s)

#Média de idado do grupo
media = sum(idade)/4

#Nome do homem mais velho
for i in sexo:
    if i == 'M':
        idadeh.append(idade[c1])
    c1 += 1
maior_idadeh = max(idadeh)

for i in nome:
    if maior_idadeh == idade[c2] and sexo[c2] == 'M':
        older = i
    c2 += 1

#Quantidade de mulheres menores de 20 anos
for i in sexo:
    if i == 'F' and idade[c3] < 20:
        mulherm +=1
    c3 += 1

#Resolvidos
print(f'A média de idade do grupo é {media}')
print(f'O nome do HOMEM mais velho é o {older} e tem {maior_idadeh} anos')
print(f'No grupo há {mulherm} mulheres menores de 20 anos')
