import pygame
import sys
import random
from Block import *

VERTICAL = 10
HORIZONTAL = 15
TAILLE_CASE = 40

FENETRE = pygame.display.set_mode(size=(VERTICAL * TAILLE_CASE, HORIZONTAL * TAILLE_CASE))
FPS = pygame.time.Clock()
        
        
class Wall:
    def __init__(self):
        x = 1
        y = 2
        self.block = Block(x, y)
        
    def draw_Wall(self):
        rect = pygame.Rect(self.block.x * TAILLE_CASE,self.block.y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
        pygame.draw.rect(FENETRE,(2,42,98), rect)