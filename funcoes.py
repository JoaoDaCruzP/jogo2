import pygame

def matar(tiro,player):
    if pygame.sprite.collide_mask(player, tiro):
        print('matou')