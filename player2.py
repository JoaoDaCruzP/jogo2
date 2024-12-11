import pygame
from variaveis import *

class Player_2 (pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        #variaveis
        self.x = largura /2 + 650
        self.y = altura /2
        self.speed = 5
        self.w = 50
        self.h = 50
        self.image = pygame.image.load('data/images/player2a.png')
        self.image = pygame.transform.scale(self.image,[self.w,self.h])
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
        self.direcao = 'left'


    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.image = pygame.image.load('data/images/player2w.png')
            self.image = pygame.transform.scale(self.image,[self.w,self.h])
            self.direcao = 'up'
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.image = pygame.image.load('data/images/player2s.png')
            self.image = pygame.transform.scale(self.image,[self.w,self.h])
            self.direcao = 'down'
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = pygame.image.load('data/images/player2a.png')
            self.image = pygame.transform.scale(self.image,[self.w,self.h])
            self.direcao = 'left'
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = pygame.image.load('data/images/player2d.png')
            self.image = pygame.transform.scale(self.image,[self.w,self.h])
            self.direcao = 'right'
        
        
        # define limine nas bordas para o player1
        
        if self.rect.x >= largura - 50:
            self.rect.x = largura - 50 
        elif self.rect.x <= largura - largura:
            self.rect.x = largura - largura
        if self.rect.y >= altura - 50:
            self.rect.y = altura - 50
        elif self.rect.y <= altura - altura:
            self.rect.y = altura - altura
        
