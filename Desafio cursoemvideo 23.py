name = input('Digite seu nome: ').strip()
uname = name.upper()
lname = name.lower()
lenname = len(name.replace(' ', ''))
dname = name.split()
lenfname = len(dname[0])
print(f"""
Nome com todas letras maiúsculas: 
{uname}
Nome com todas letras minúsculas:
{lname}
A quantidade de letras no nome todo é: {lenname}
A quantidade de letras no primeiro nome é: {lenfname}
""")
