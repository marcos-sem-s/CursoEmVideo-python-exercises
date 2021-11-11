times = ('Coritiba', 'Náutico', 'Sampaio Côrrea', 'Guarani', 'Vasco da Gama',
         'CRB', 'Goiás', 'Avaí', 'Botafogo', 'Brusque',
         'Operário', 'CSA', 'Remo', 'Vila Nova', 'Cruzeiro',
         'Ponte Preta', 'EC Vitória', 'Confiança', 'Londrina', 'Brasil de Pelotas',)

escolha = int(input(
"""1) Printar os 5 primeiros colocados
2) Printar os últimos 4 colocados da tabela
3) Printar a lista com os times em odem alfabética
4) Printar em que posição da tabela está o Remo
Escolha uma opção de um a quatro: """))
print('-=' * 40)

while (1 <= escolha <= 4) == False:
    escolha = int(input(
"""- ERRO - 
1) Printar os 5 primeiros colocados
2) Printar os últimos 4 colocados da tabela
3) Printar a lista com os times em odem alfabética
4) Printar em que posição da tabela está o Remo
Opção indisponível, escolha outra opção de um a quatro: """))
    print('-=' * 40)

if escolha == 1:
    print(f'Os 5 primeiros colocados será: {times[0:5]}')
elif escolha == 2:
    print(f'Os últimos 4 colocados da tabela são: {times[-4:]}')
elif escolha == 3:
    print(f'A lista em ordem alfabética será: {sorted(times)}')
elif escolha == 4:
    remo = times.index('Remo') + 1
    print(f'O Remo está na {remo}° posição')
