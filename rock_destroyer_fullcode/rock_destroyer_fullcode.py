import os
import pygame
import math

from pygame.locals import *

import classe.player.Player as Player
import classe.balle.Balle as Balle
import classe.Asteroide.Asteroide as Asteroide
import classe.bouton.Bouton as Bouton
    
    

def menuJeu():
    pygame.init()
    pygame.key.set_repeat(400,30)
    clock = pygame.time.Clock() #pour gener le frame rate

    fenetreMenu = pygame.display.set_mode((1000, 1000))
    fond = pygame.image.load((os.path.join('image/fond', 'background.png'))).convert()
    
    boutonJeu = Bouton.Bouton("Jouer",(400,300))
    texteJeu = Bouton.TexteBouton("Jouer",boutonJeu.rect)
    boutonQuitter = Bouton.Bouton("Quitter",(400,450))
    texteQuitter = Bouton.TexteBouton("Quitter",boutonQuitter.rect)
    
    
    fenetreMenu.blit(fond,(0,0))

    jouer = 0
    quitter = 0
    continuer = True
    while continuer :
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if event.type == QUIT:     
                continuer = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boutonJeu.check_click(event.pos):
                    jouer = 1
                    continuer = False
                if boutonQuitter.check_click(event.pos):
                    quitter = 1
                    continuer = False

        clock.tick(60) #limite a 60 fps
        fenetreMenu.blit(fond,(0,0))
        fenetreMenu.blit(boutonJeu.image,boutonJeu.rect)
        fenetreMenu.blit(texteJeu.image,texteJeu.rect)

        fenetreMenu.blit(boutonQuitter.image,boutonQuitter.rect)
        fenetreMenu.blit(texteQuitter.image,texteQuitter.rect)

        pygame.display.update()
    
    if jouer == 1:
        pygame.quit()
        niveau1()
    else:
        pygame.quit()

    
def niveau1():
    
    pygame.init()
    pygame.key.set_repeat(400,30)
  
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/son_music/son_music.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1) #-1 pour jouer en boucle

    clock = pygame.time.Clock() #pour gener le frame rate
    fenetre = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Collision")
    fond = pygame.image.load((os.path.join('image/fond', 'background.png'))).convert()

    player = Player.Player()
    balle = []
    l_asteroide = []

    i=0
    while i < 6:
        i += 1
        l_asteroide.append(Asteroide.Asteroide())


    fenetre.blit(fond,(0,0))
    fenetre.blit(player.image,player.rect)
    for element in l_asteroide:
        fenetre.blit(element.image,element.rect)

    continuer = True
    while continuer :

        player.repop() #si le player sort de l ecran

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            #deplacements du player
            if event.type == KEYDOWN:
                fenetre.blit(fond,(0,0))
                dicKeys = pygame.key.get_pressed()
                if dicKeys[K_LEFT] :
                    player.rotate(12) 
                if dicKeys[K_RIGHT] :    
                    player.rotate(-12) 
                if dicKeys[K_UP] :
                    player.accelerer(1)
                if dicKeys[K_DOWN] : 
                    player.accelerer(-1)
            #tirs du player
            if event.type == MOUSEBUTTONDOWN:
                balle.append(Balle.Balle(player.rect.center,player.angle))
        
        # supression des balles eloignees
        for element in balle:
            if element.get_dureeVie() > 3:
                balle.remove(element)
        try:
            player.deplacement(0) #Pour que le player continu d avancer en fonction de sa vitesse
            fenetre.blit(fond,(0,0))
            fenetre.blit(player.image,player.rect)
        except:
            pass
   
        #deplacement des asteroids
        try:
            for element in l_asteroide:
                element.deplacement()
                #collision player/asteroid
                if player.rect.colliderect(element.rect):
                   player.mort()
                   player = None
                   continuer = False
                   break
                #collision balles/asteroid
                for bullet in balle:
                    if bullet.rect.colliderect(element.rect):
                        balle.remove(bullet)
                        element.destroy()
                        if element.type == 1:
                            i=0
                            while i < 2:
                                i += 1
                                l_asteroide.append(Asteroide.miniAsteroide(element.rect.x,element.rect.y))
                        elif len(l_asteroide) < 12:
                            l_asteroide.append(Asteroide.Asteroide())

                        l_asteroide.remove(element)

                fenetre.blit(element.image,element.rect)
        except:
            continuer = False
        #deplacement des balles
        try:
            for element in balle:
                element.tir()
                fenetre.blit(element.image,element.rect)
        except:
            pass
   
        clock.tick(60) #limite a 60 fps
        pygame.display.update()
    pygame.quit()
    menuJeu()

menuJeu()
pygame.quit()
