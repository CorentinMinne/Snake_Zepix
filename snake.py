"""
Snake
1 Joueur
files : snake.py + images
"""

#Importations
import pygame 
import os
import random
from pygame.locals import *

#Initialisation
continuer = True
continuer_jeu = False
continuer_accueil = True
direction = "none"
vitesse = 50
there_is_a_fruit = False
x = []
y = []
x.append(500)
y.append(500)
x_fruit = -200
y_fruit = -200
score = 0

#Fenetre
fenetre = pygame.display.set_mode((1000,1000), RESIZABLE)
pygame.init()
accueil = pygame.image.load("images/accueil.jpg").convert()
fond = pygame.image.load("images/fond.jpg").convert()
snake = pygame.image.load("images/snake.jpg").convert()
fruit = pygame.image.load("images/fruit.jpg").convert()



#Boucle Principale
while continuer:
	#Chargement et affichage de l'écran d'accueil
    fenetre.blit(accueil, (0,0))
    pygame.display.flip()
    continuer_jeu = False
    continuer_accueil = True

    while continuer_accueil:
		#Limitation à 30 FPS
        pygame.time.Clock().tick(30)

		#Evenements
        for event in pygame.event.get():
		
		#Si l'utilisateur quitte, on met les variables de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = False
                continuer_jeu = False
                continuer = False

            elif event.type == KEYDOWN and event.key == K_SPACE:
                continuer_accueil = False
                continuer_jeu = True

    fenetre.blit(fond, (0,0))
    fenetre.blit(snake, (x[0],y[0]))

    while continuer_jeu:
        #Limitations à 30 FPS
        pygame.time.Clock().tick(30)
        #Boucle d'affichage
        fenetre.blit(fond, (0,0))
        fenetre.blit(fruit, (x_fruit,y_fruit))
		#Affichage du Snake
        for i in range(score + 1):
            fenetre.blit(snake, (x[i],y[i]))
		
        pygame.display.flip()

        for event in pygame.event.get():

			#Si l'utilisateur quitte, on met la variable qui continue le jeu ET la variable générale à 0 pour fermer la fenêtre
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_jeu = False
                continuer = False
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = "left"
                    print("left")
                if event.key == K_RIGHT:
                    direction = "right"
                    print("right")				
                if event.key == K_UP:  
                    direction = "up"
                    print("up")
                if event.key == K_DOWN:
                    direction = "down"
                    print("down")

        if there_is_a_fruit == False:
            x_fruit = random.randint(0,19) * 50
            y_fruit = random.randint(0,19) * 50
            there_is_a_fruit = True

        if (x_fruit == x[score] and y_fruit == y[score]):
            score += 1
            x_fruit = -200
            y_fruit = -200
            there_is_a_fruit = False
            x.append(x[score - 1])
            y.append(y[score - 1])
        if direction == "up":
            y[score] -= vitesse
        if direction == "down":
            y[score] += vitesse
        if direction == "right":
            x[score] += vitesse
        if direction == "left":
            x[score] -= vitesse
        print (x[score], y[score])
        if (x[score] < 0 or y[score] < 0 or x[score] >= 1000 or y[score] >= 1000):
            continuer_jeu = False
            continuer_accueil = True
            there_is_a_fruit = False
            x = []
            y = []
            x.append(500)
            y.append(500)
            x_fruit = -200
            y_fruit = -200
            score = 0
            direction = "none"
            
        pygame.time.wait(100)
    








		
			






