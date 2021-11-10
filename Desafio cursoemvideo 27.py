fra = input('Digite qual quer frase: ').strip().upper()
cfra = fra.count('A')
ffra = fra.find('A')
lffra = fra.rfind('A')
print(f"""
A letra "A" aparece {cfra} vezes
Ela aparece pela primeira vez na posição {ffra} e pela última vez na posição {lffra}
""")
