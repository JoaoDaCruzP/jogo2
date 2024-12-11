import pygame

class Bala(pygame.sprite.Sprite):
    def __init__(self,player,player_direcao, grupo):
        super().__init__(grupo)
        self.image = pygame.image.load('data/images/tiro.png')
        self.image = pygame.transform.scale(self.image,[50,50])
        self.rect = self.image.get_rect()
        self.speed = 10
 
        #self.rect.centerx = player.rect.x
        #self.rect.top = player.rect.y

        if player_direcao == 'up':
            self.rect.centerx = player.rect.centerx  # Alinhar com o centro horizontal do jogador
            self.rect.bottom = player.rect.top  # Posição logo acima do jogador
        elif player_direcao == 'down':
            self.rect.centerx = player.rect.centerx  # Alinhar com o centro horizontal do jogador
            self.rect.top = player.rect.bottom  # Posição logo abaixo do jogador
        elif player_direcao == 'left':
            self.rect.centery = player.rect.centery  # Alinhar com o centro vertical do jogador
            self.rect.right = player.rect.left  # Posição à esquerda do jogador
        elif player_direcao == 'right':
            self.rect.centery = player.rect.centery  # Alinhar com o centro vertical do jogador
            self.rect.left = player.rect.right  # Posição à direita do jogador

        self.direcao = player_direcao

    def update(self):
        # Atualiza a posição do tiro com base na sua velocidade
        if self.direcao == 'left':
            self.rect.x -= self.speed
        elif self.direcao == 'right':
            self.rect.x += self.speed
        elif self.direcao == 'up':
            self.rect.y -= self.speed
        elif self.direcao == 'down':
            self.rect.y += self.speed
        
        if self.rect.x > 1370 or self.rect.x < 0 or self.rect.y > 730 or self.rect.y < 0:
            self.kill()
        

        
