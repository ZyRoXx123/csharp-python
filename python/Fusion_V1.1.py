#Importation des bibliothèques
import pygame,sys,time
from pygame.locals import *
import random


#Initialisation de la bibliothèque pygame #kevin
pygame.init()
pygame.font.init()

#Variables Marc
Horlogeprincipal= pygame.time.Clock()
fenetre=pygame.display.set_mode((1366,768),RESIZABLE)   	# Creation de la fenètre + Taille fenêtre du jeu ( 1366,768 pour le petit pc de MarKo)
pygame.display.set_caption('Try It Again')        # titre de la fenêtre
Texte = pygame.font.Font("SuperMario256.ttf", 65) #Police du Text
Obj_texte = Texte.render("Try It Again",0, (255,0,0))#Placement du titre du jeu
clock = pygame.time.Clock()
continuer = 1
font = pygame.font.SysFont('SuperMario256.ttf', 70)
bouton = pygame.image.load("boutonjouer.png").convert_alpha()


taille_img=(841,474)    #definir la taille de l'image
mainclock= pygame.time.Clock()
clock = pygame.time.Clock()
image = pygame.image.load("background.png")
x_fond=0
Gauche=False
Droite=False
gameover = pygame.image.load("ragequit.png")



red = (255,0,0)
black = (0,0,0)



## KEVIN

def fondjeux():
    global x_fond        #definir le fond egal a 0 au debut
    fenetre.blit(image,(x_fond,0))
    fenetre.blit(image,(x_fond+taille_img[0],0))
    if x_fond<=-taille_img[0]:
                        x_fond=0


def evenement():
        global x_fond, Gauche,Droite,jeu,intro
        for event in pygame.event.get():	# Traiter les évènements du clavier
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:   # Quitter le jeu
                    fenetre.blit(gameover,(320,175))
                    pygame.display.update()
                    time.sleep(3)
                    jeu=False
                    intro=True
##                    pygame.quit()
##                    sys.exit()
                if event.key == K_a:
                    Gauche = True        #Personnage vers la gauche
                    print("Gauche")
                if event.key == K_d:
                    Droite = True        #Personnage vers la droite
                if event.key == K_SPACE:
                    #Personnage fait un saut
                    print("Saut")
                if event.key == K_w:
                    #Personnage fait un saut
                    print("Saut")
            if event.type== KEYUP:                  #Quand la touche est relacher
             if event.key==K_d:
                Droite = False
             if event.key==K_a:
                Gauche = False

            if event.type==QUIT: # Quitter le jeu
                pygame.quit()
                sys.exit()

# Fonctions MARC


def evenement_m():
        ''' Fonction de marc qui gère les évènements du clavier dans le menu'''
        for event in pygame.event.get():	# Traiter les évènements du clavier
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:   # Quitter le jeu
                    pygame.quit()
                    sys.exit()
            if event.type==QUIT: # Quitter le jeu
                pygame.quit()
                sys.exit()






def game_intro():

    global intro,jeu,fenetre

    while intro:
        fenetre.fill (0x8258FA)# Remplir l'arrieère plan avec la couleur en hexa=(0x) Bleu foncé
        fenetre.blit(Obj_texte,(450,100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()

        mouse = pygame.mouse.get_pos()


        if 540+241 > mouse[0] > 550 and 265+70 > mouse[1] > 265:
            fenetre.blit(bouton, (540,250))     # image bouton survolé
            pygame.draw.rect(fenetre, (0, 255, 150),(150,450,100,50))
            if pygame.mouse.get_pressed()[0]==1:
                intro=False
                jeu=True
                fenetre=pygame.display.set_mode(taille_img,0,32)

        else:
            fenetre.blit(bouton, (540,250)) # image bouton nornal
            pygame.draw.rect(fenetre, (0, 255, 0),(150,450,100,50),63)

        pygame.display.update()

intro=True
jeu=False

while continuer:


##    evenement_m()
    if intro:

        game_intro()

    if jeu:
        fondjeux()
        evenement()
        if Droite:
            x_fond-=7
        if Gauche:
            x_fond+=7
        pygame.display.update()
        clock.tick(30)

##    clock.tick(30)



