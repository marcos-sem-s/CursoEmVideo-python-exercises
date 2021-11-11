from math import cos, tan, sin, radians
angle = int(input('Qual o valor do ângulo? '))
cang = cos(radians(angle))
tang = tan(radians(angle))
sang = sin(radians(angle))
print(f'Para o número escolhido, seu Cosseno é {cang:.2f}, sua Tangente é {tang:.2f} e seu Seno é {sang:.2f}')
