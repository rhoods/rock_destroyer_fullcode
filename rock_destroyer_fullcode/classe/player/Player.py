import os
import pygame
import math

class Player:
    def __init__(self):
        pygame.mixer.init()
        self.mort_sound = pygame.mixer.Sound("sounds/son_rockdestroy/son_rockdestroy.wav")
        self.mort_sound.set_volume(1.5)  

        self.angle = 0
        self.old_angle = 0
        self.vitesse = [0,0]
        self.origin_image = pygame.image.load((os.path.join('image/player', 'spr_player.png'))).convert_alpha()
        self.image = pygame.image.load((os.path.join('image/player', 'spr_player.png'))).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (270,300)
        

    def rotate(self, angle):      
        self.angle += angle
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)
     

    def accelerer(self, acceleration):
        if acceleration >= 0:
            self.vitesse[0] += acceleration
            self.vitesse[0] = min(self.vitesse[0], 4)
        else:
            self.vitesse[0] += acceleration
            self.vitesse[0] = max(self.vitesse[0], -4)

        angle = math.radians(self.angle)
        self.old_angle = math.radians(self.angle)
        #if self.angle >= 0: #matrice sens anti horaire
        M=[[math.cos(angle),  math.sin(angle)],[math.sin(angle), math.cos(angle)]]
        #else: #matrice sens horaire
        #    M=[[math.cos(angle), math.sin(angle)],[ math.sin(angle), math.cos(angle)]]
        
        x = self.vitesse[0] * M[0][0] + self.vitesse[1] * M[0][1]
        y = self.vitesse[0] * M[1][0] + self.vitesse[1] * M[1][1]  
        self.rect = self.rect.move(x,-y) #- car axe y inversé


    def deplacement(self, acceleration):
        if acceleration >= 0:
            self.vitesse[0] += acceleration
            self.vitesse[0] = min(self.vitesse[0], 4)
        else:
            self.vitesse[0] += acceleration
            self.vitesse[0] = max(self.vitesse[0], -4)

        M=[[math.cos(self.old_angle),  math.sin(self.old_angle)],[math.sin(self.old_angle), math.cos(self.old_angle)]]
        #M=[[math.cos(abs(self.old_angle-self.angle)),  math.sin(abs(self.old_angle-self.angle))],[math.sin(abs(self.old_angle-self.angle)), math.cos(abs(self.old_angle-self.angle))]]
        #else: #matrice sens horaire
        #    M=[[math.cos(angle), math.sin(angle)],[ math.sin(angle), math.cos(angle)]]
        x = self.vitesse[0] * M[0][0] + self.vitesse[1] * M[0][1]
        y = self.vitesse[0] * M[1][0] + self.vitesse[1] * M[1][1]  
        self.rect = self.rect.move(x,-y) #- car axe y inversé

    def repop(self):
        if self.rect.x > 1000:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = 1000
        if self.rect.y > 1000:
            self.rect.y = 0
        if self.rect.y < 0:
            self.rect.y = 1000

    def mort(self):
        self.mort_sound.play()

    