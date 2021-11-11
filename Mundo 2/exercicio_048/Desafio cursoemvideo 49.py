s = 0
c = 0
for i  in range(1, 501):
    if i%2!=0 and i%3==0:
        s+=i
        c+=1
print(f'A soma dos {c} numeros ÍMPARES e MÚLTIPLOS DE 3 entre 1 e 500 é: {s}')

#for i in range(1, 501, 2): 