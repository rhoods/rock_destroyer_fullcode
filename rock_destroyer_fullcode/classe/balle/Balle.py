import os
import pygame
import math

class Balle:
    def __init__(self,coordonnee,angle):
        #son tir
        pygame.mixer.init()
        self.tir_sound = pygame.mixer.Sound("sounds/son_shoot/son_shoot.wav")
        self.tir_sound.set_volume(1)
        self.tir_sound.play()

        self.angle = angle
        self.time = pygame.time.get_ticks()/1000
        self.vitesse = [15,0]
        self.image = pygame.image.load((os.path.join('image/balle', 'spr_balle.png'))).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (coordonnee)
        self.clock = pygame.time.Clock()
        self.tir

    def get_dureeVie(self):
       current_time = pygame.time.get_ticks()/1000
       return current_time - self.time

    def tir(self):
        angle = math.radians(self.angle)
        M=[[math.cos(angle),  math.sin(angle)],[math.sin(angle), math.cos(angle)]]
        
        x = self.vitesse[0] * M[0][0] + self.vitesse[1] * M[0][1]
        y = self.vitesse[0] * M[1][0] + self.vitesse[1] * M[1][1]  
      
        self.rect = self.rect.move(x,-y)
        
