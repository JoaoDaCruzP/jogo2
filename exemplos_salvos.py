import pygame
#colisa de sprite usando MASK

# Supondo que 'outro_sprite' seja o inimigo ou objeto com quem você quer detectar a colisão
'''if pygame.sprite.collide_mask(tiro, outro_sprite):
    print("Colidiu!")
    tiro.kill()  # Remove a bala ou faz a ação de colisão'''


#adicionar controle joystic

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]