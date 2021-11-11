
from random import choice
from playsound import playsound
n = [0, 1, 2, 3, 4, 5]
nn = choice(n)
pc = int(input('Adivinhe o número de 0 a 5: '))
if pc == nn:
    print('Parabéns você acertou de primeira! :)')
    playsound('c:/Users/Marco Neto/Desktop/Aulas/Python CursoEmVideo/acerto mizeravi.mp3')
else:
    print('Que pena, você errou o número, que tal uma segunda chance?')
    playsound('c:/Users/Marco Neto/Desktop/Aulas/Python CursoEmVideo/Errou.mp3')
    sc = int(input('Digite outro número de 0 a 5: '))
    if sc == nn:
        print('Parabéns, você acertou na segunda tentativa! :)')
        playsound('c:/Users/Marco Neto/Desktop/Aulas/Python CursoEmVideo/acerto mizeravi.mp3')
    else:
        print(f'Você errou todas as chances, seu número era o {nn}')
        playsound('c:/Users/Marco Neto/Desktop/Aulas/Python CursoEmVideo/ERROU FEIO, ERROU RUDE.mp3')
        