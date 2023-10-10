import os
import pygame


class Bouton:
    def __init__(self,message,position):
        #self.police = pygame.font.SysFont('Corbel',25)
        self.message = message
        self.image  = pygame.image.load((os.path.join('image/bouton', 'spr_bouton.png'))).convert_alpha()        
        self.rect   =  self.image.get_rect()
        self.rect.topleft = position
        
    def check_click(self,mouse):
        if self.rect.collidepoint(mouse):
           return True



class TexteBouton:
    def __init__(self,message,bouton):
        font = pygame.font.SysFont('Corbel',30)
        red = pygame.Color(255, 255, 255)
        self.image = font.render(message, True, red)
        self.rect = self.image.get_rect()
        self.rect.center = bouton.center
      
