import pygame
from funcoes import matar
from variaveis import *
from player1 import Player_1
from player2 import Player_2
from disparo import Bala

pygame.init()

# Inicializa a tela do jogo
display = pygame.display.set_mode([largura, altura])  # Tamanho da janela
pygame.display.set_caption('JOGO DE TIRO')  # Nome da janela

fundo = pygame.image.load('data/images/fundo.jpg')
fundo = pygame.transform.scale(fundo, [largura, altura])

# Atualização de frames por segundo
relogio = pygame.time.Clock()

# Grupos de objetos
playerGrupo = pygame.sprite.Group()
tiroGrupo = pygame.sprite.Group()

player1 = Player_1(playerGrupo)
player2 = Player_2(playerGrupo)


# Atualização e edição de tela
def draw(display, relogio):
    relogio.tick(60)  # Controle de FPS
    display.blit(fundo, (0, 0))  # Desenha o fundo na tela
    playerGrupo.update()
    playerGrupo.draw(display)
    tiroGrupo.update()
    tiroGrupo.draw(display)
    verificar_colisoes()
    
# Função para verificar colisões
def verificar_colisoes():
    for tiro in tiroGrupo:  # Itera sobre os tiros no grupo
        if pygame.sprite.collide_mask(tiro, player2):
            print('Player1 matou Player2!')
            tiro.kill()
         
            player2.rect.x = largura /2 + 650
            player2.rect.y = altura /2 - 350

        if pygame.sprite.collide_mask(tiro, player1):
            print('Player2 matou Player1!')
            tiro.kill()

            player1.rect.x = largura /2 - 650
            player1.rect.y = altura /2 + 280

    


gameLoop = True;
if __name__ == "__main__":
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False;
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('Player1 atirou')
                    novo_tiro = Bala(player1,player1.direcao, tiroGrupo)
                    
                if event.key == pygame.K_KP_ENTER:
                    print('player2 atirou')
                    novo_tiro = Bala(player2,player2.direcao,tiroGrupo)

                    
       
                    
        
        draw(display,relogio)
        pygame.display.update()
        
    
    pygame.quit()
