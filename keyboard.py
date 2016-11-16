
import pygame
from pygame.locals import *

pygame.init()

def getKeys():
    pygame.event.pump()
    press = pygame.key.get_pressed()
    print(press)
