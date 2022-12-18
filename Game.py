import pygame
import sys
import random
from Cherry import *
from Snake import *
from Wall import *
from Game import *

pygame.font.init()

class Game:
    def __init__(self):
        self.snake = Snake()
        self.cherry = Cherry()
        self.wall = Wall()
        self.score_value=0
        self.font = pygame.font.SysFont("monospace", 16,False,False)
        self.textx= 10
        self.texty= 10
        
    def update(self):
        self.snake.action_snake()
        self.repas()
        self.game_over()
        
    def draw_game(self):
        self.snake.draw_snake()
        self.cherry.draw_Cherry()
        self.wall.draw_Wall()
        
    def repas(self):
        snake_taille = len(self.snake.body)
        snake_tete = self.snake.body[snake_taille - 1]
        cherry_case = self.cherry.block
        if snake_tete.x == cherry_case.x and snake_tete.y == cherry_case.y:
            self.reload_cherry()
            self.score_value += 1
        else:
            self.snake.body.pop(0)
            
        
    def reload_cherry(self):
        self.cherry = Cherry()
        
            
        
    def game_over(self):
        snake_taille = len(self.snake.body)
        snake_tete = self.snake.body[snake_taille - 1]  
        wall_case = self.wall.block
        if (snake_tete.x not in range(0, VERTICAL)) or (snake_tete.y not in range(0, HORIZONTAL)): 
            print('Le serpent est mort :,(')
            pygame.quit()
            sys.exit
        for block in self.snake.body[0:snake_taille - 1]:
            if block.x == snake_tete.x and block.y == snake_tete.y:
                print("Tellement affamé, le  serpent s'est manger lui-même :/")
                pygame.quit()
                sys.exit
        if snake_tete.x == wall_case.x and snake_tete.y == wall_case.y:
            print("Aie, le Serpent a confondu un mur avec une cerise :,(")
            pygame.quit()
            sys.exit
            
    def compteur(self,VERTICAL,HORIZONTAL):       
        score = self.font.render("Score :" + str(self.score_value),True, (255,255,255))
        FENETRE.blit(score, (VERTICAL,HORIZONTAL))
    
    