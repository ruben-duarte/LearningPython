import pygame
from pong import Game

WIDTH, HEGHT = 700, 500
window = pygame.display.set_mode((WIDTH,HEGHT))

game = Game(window, WIDTH,HEGHT)

run = True
clock  = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        game.move_paddle(left=True, up=True)
    if keys[pygame.K_s]:
        game.move_paddle(left=True, up=False)

    game_info = game.loop()
    print(game_info.left_score, game_info.left_hits)
    game.draw()
    pygame.display.update()

pygame.quit()