import pygame
import sys
import random

VERTICAL = 10
HORIZONTAL = 15
TAILLE_CASE = 40

FENETRE = pygame.display.set_mode(size=(VERTICAL * TAILLE_CASE, HORIZONTAL * TAILLE_CASE))
FPS = pygame.time.Clock()



class Block:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position