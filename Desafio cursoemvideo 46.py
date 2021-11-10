from random import choice
import time

para = 'Você ganhou! Parabéns'
m1 = input('Escolha entre pedra, papel e tesoura: ')
time.sleep(2)
move = choice(['pedra', 'papel', 'tesoura'])
print('A máquina escolheu', move)
time.sleep(2)

if m1 == move:
    print('Empate!')
elif m1 == 'pedra' and move == 'tesoura':
    print(para)
elif m1 == 'papel' and move == 'pedra':
    print(para)
elif m1 == 'tesoura' and move == 'papel':
    print(para)
else:
    print('Você perdeu, mais sorte na próxima!')
    