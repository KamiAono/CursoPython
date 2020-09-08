import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('copie e cole uma musica em .mp3 aqui')
pygame.mixer.music.play()
pygame.event.wait()

