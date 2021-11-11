v1 = input('Digite qualquer coisa: ')

print(f'O tipo primitivo desse valor é {type(v1)}')
print(f'É numérico? {v1.isnumeric()}')
print(f'É alfabético? {v1.isalpha()}')
print(f'É alfa-numérico? {v1.isalnum()}')
print(f'É composto somente por letras maiúsculas? {v1.isupper()}')
print(f'É composto somente por letras minúsculas? {v1.islower()}')
