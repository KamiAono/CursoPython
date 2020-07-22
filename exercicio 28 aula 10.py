from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número 0 a 5, tente adivinhar.')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei?')) #O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == pc:
    print('VOCÊ ACERTOU, PARABÉNS!')
    import pygame

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('acertou-mizeravijk_eifzvEs.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
else:
    print('VOCÊ ERROU!, EU PENSEI NO NÚMERO {} E NÃO NO NÚMERO {}'.format(pc, jogador))
    import pygame
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('faustao-errou_qxgOLcE.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
