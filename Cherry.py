import pygame
import sys
import random
from Block import *

VERTICAL = 10
HORIZONTAL = 15
TAILLE_CASE = 40

FENETRE = pygame.display.set_mode(size=(VERTICAL * TAILLE_CASE, HORIZONTAL * TAILLE_CASE))
FPS = pygame.time.Clock()
        
        
class Cherry:
    def __init__(self):
        x = random.randint(0,VERTICAL -1)
        y = random.randint(0,HORIZONTAL -1)
        self.block = Block(x, y)
        
    def draw_Cherry(self):
        rect = pygame.Rect(self.block.x * TAILLE_CASE,self.block.y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
        pygame.draw.rect(FENETRE,(255, 56, 24), rect)