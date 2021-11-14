
from random import choice
# import pyglet

n = [0, 1, 2, 3, 4, 5]
nn = choice(n)
pc = int(input('Adivinhe o número de 0 a 5: '))

if pc == nn:
    print('Parabéns você acertou de primeira! :)')
    # music = pyglet.resource.media('acerto mizeravi.mp3')
    # music.play()
    # pyglet.app.run()
else:
    print('Que pena, você errou o número, que tal uma segunda chance?')
    # music = pyglet.resource.media('Errou.mp3')
    # music.play()
    sc = int(input('Digite outro número de 0 a 5: '))

    if sc == nn:
        print('Parabéns, você acertou na segunda tentativa! :)')
        # music = pyglet.resource.media('acerto mizeravi.mp3')
        # music.play()
        # pyglet.app.run()
    else:
        print(f'Você errou todas as chances, seu número era o {nn}')
        # music = pyglet.resource.media('ERROU FEIO, ERROU RUDE.mp3')
        # music.play()
        # pyglet.app.run()

# pyglet comentado devido à erro de tempo de execução