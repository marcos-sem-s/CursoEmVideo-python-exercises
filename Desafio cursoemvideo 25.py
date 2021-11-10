cidade = str(input('Escolha uma cidade: ')).title().strip().split()
S = cidade[0]
if 'Santo' in S:
    print('Sua cidade começa com a palavra Santo!')
else:
    print('Sua cidade não começa com a palavra Santo!')
    