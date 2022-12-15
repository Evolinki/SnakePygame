import pygame
import sys
import random
from Cherry import *
VERTICAL = 10
HORIZONTAL = 15
TAILLE_CASE = 40

FENETRE = pygame.display.set_mode(size=(VERTICAL * TAILLE_CASE, HORIZONTAL * TAILLE_CASE))
FPS = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.body = [Block(2,6), Block(3,6), Block(4,6)]
        self.direction = "RIGHT"
    
    def draw_snake(self):
        for block in self.body:
            x_position = block.x * TAILLE_CASE
            y_position = block.y * TAILLE_CASE
            block_rect= pygame.Rect(x_position,y_position,TAILLE_CASE,TAILLE_CASE)
            pygame.draw.rect(FENETRE, (244, 208, 63), block_rect)
    
    def action_snake(self):
        snake_block_count = len(self.body)
        old_head = self.body[snake_block_count - 1]
        
        if self.direction == "RIGHT":
            new_head = Block(old_head.x + 1,old_head.y)
            
        elif self.direction == "LEFT":
            new_head = Block(old_head.x + -1,old_head.y)
        elif self.direction == "DOWN":
            new_head = Block(old_head.x ,old_head.y + 1)
        elif self.direction == "TOP":
            new_head = Block(old_head.x ,old_head.y + -1)
        
        self.body.append(new_head)