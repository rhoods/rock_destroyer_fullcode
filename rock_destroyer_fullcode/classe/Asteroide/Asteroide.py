import os
import pygame
import math
import random


class Asteroide:
    def __init__(self):
        #son explosion
        pygame.mixer.init()
        self.explo_sound = pygame.mixer.Sound("sounds/son_rockdestroy/son_rockdestroy.wav")
        self.explo_sound.set_volume(1.5)  

        self.type = 1 #pour differencier grand de petit asteroids
        self.angle = 0
        self.time = pygame.time.get_ticks()/1000
        self.origin_image = pygame.image.load((os.path.join('image/asteroide', 'spr_big_asteroid.png'))).convert_alpha()
        self.image = pygame.image.load((os.path.join('image/asteroide', 'spr_big_asteroid.png'))).convert_alpha()
        self.rect = self.image.get_rect()
        self.apparition()
        
        self.clock = pygame.time.Clock()
    
    def apparition(self):
        f_choice = random.randint(0,3)
        if f_choice == 0:
            x = random.randint(-100,-50)
            y = random.randint(0,1000)
        if f_choice == 1:
            x = random.randint(1050,1100)
            y = random.randint(0,1000)
        if f_choice == 2:
            y = random.randint(-100,-50)
            x = random.randint(0,1000)
        if f_choice == 3:
            y = random.randint(-100,-50)
            x = random.randint(0,1000)
        self.rect.topleft = (x,y)
        self.rotate()
        self.direction()

    def rotate(self):      
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)
     
       
    def direction(self):
        self.x = 1
        self.y = 1
        if self.rect.x > 500:
            self.x = -1
        if self.rect.y > 500:
            self.y = -1
        self.rect = self.rect.move(self.x,self.y)

    def deplacement(self):
        self.rotate()
        self.rect = self.rect.move(self.x,self.y)
        current_time = pygame.time.get_ticks()/1000
        if (current_time - self.time) > 2:
            self.time = current_time
            self.repop()

    def repop(self):
        if self.rect.x > 1000 or self.rect.x < 0 or self.rect.y > 1000 or self.rect.y < 0:
            self.apparition()

    def destroy(self):
        self.explo_sound.play()
        



class miniAsteroide(Asteroide):
    def __init__(self,posx,posy):
        super().__init__()
        self.origin_image = pygame.image.load((os.path.join('image/asteroide', 'spr_mini_asteroid.png'))).convert_alpha()
        self.image = pygame.image.load((os.path.join('image/asteroide', 'spr_mini_asteroid.png'))).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (posx,posy)
        self.type = 2 #pour differencier grand de petit asteroids
       # self.rect = self.rect.move(random.Random(-1,1),random.Random(-1,1))
      