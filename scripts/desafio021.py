#desafio21: um programa em python que abra e reproduza o áudio de um arquivo mp3
#
'''import pydub é outra opção interessante'''

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('CUCO _Lover_is_a_Day.mp3')
pygame.mixer.music.play()
pygame.event.wait()
