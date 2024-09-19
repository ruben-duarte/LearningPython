import pygame
from pygame.locals import *

def draw_block():
    surface.fill((44,44,84))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000,500)) #window size
    surface.fill((44,44,84)) #window color
    block = pygame.image.load('block.png').convert()
    block = pygame.transform.scale(block, (20,20))
    #surface is the background, blit is draw this
    block_x, block_y = 100, 100
    surface.blit(block, (block_x, block_y))


    pygame.display.flip()#update changes in window

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False