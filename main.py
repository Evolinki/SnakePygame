import pygame
import sys
import random
from Cherry import *
from Snake import *
from Wall import *
from Game import *
     
pygame.init
score_value=0
VERTICAL = 15
HORIZONTAL = 15
TAILLE_CASE = 40

Point = Game.repas
FENETRE = pygame.display.set_mode(size=(VERTICAL * TAILLE_CASE, HORIZONTAL * TAILLE_CASE))
FPS = pygame.time.Clock()
F_UPDATE = pygame.USEREVENT
pygame.time.set_timer(F_UPDATE, 200)

game_on = True
cherry = Cherry()
snake = Snake()
game = Game()
wall = Wall()
pygame.init()

font = pygame.font.SysFont("monospace", 16)
textx= 10
texty= 10

def compteur(VERTICAL,HORIZONTAL):       
    score = font.render("Score :" + str(score_value),True, (255,255,255))
    FENETRE.blit(score, (VERTICAL,HORIZONTAL))
def Grille():
    for i in range(0, VERTICAL):
        for j in range(0,HORIZONTAL):
            rect = pygame.Rect(i * TAILLE_CASE, j * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
            pygame.draw.rect(FENETRE, pygame.Color(0,0,255), rect, width=1)

while game_on:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == F_UPDATE:
            game.update()
            
            
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_UP:
                if game.snake.direction != "DOWN":
                    game.snake.direction = "TOP"
            if event.key == pygame.K_DOWN:
                if game.snake.direction != "TOP":
                    game.snake.direction = "DOWN"
            if event.key == pygame.K_LEFT:
                if game.snake.direction != "RIGHT":
                    game.snake.direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                if game.snake.direction != "LEFT":
                    game.snake.direction = "RIGHT"
                    
    FENETRE.fill(pygame.Color(0,0,0))
    Grille()
    Game()    
    game.draw_game()
    compteur(textx,texty)
    pygame.display.update()
    FPS.tick(60)