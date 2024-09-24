import pygame
from pygame.locals import *
import time

SIZE = 20

class Apple():
    def __init__(self, parent_screen):
       self.image = pygame.image.load('apple.jpg').convert()
       self.image = pygame.transform.scale(self.image, (18,18))
       self.parent_screen = parent_screen
       self.x = SIZE*3
       self.y = SIZE*3
    
    def draw(self):     
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip() #update changes in window       

class Snake():
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load('block.png').convert()
        self.block = pygame.transform.scale(self.block, (20,20))    
        self.block_x = [SIZE]*length
        self.block_y = [SIZE]*length
        self.direction = 'down'
        
    def draw(self):
        self.parent_screen.fill((44,44,84))
        for square in range(self.length):
          self.parent_screen.blit(self.block, (self.block_x[square], self.block_y[square]))
        
        pygame.display.flip() #update changes in window

    def move_up(self):
        self.direction = 'up'


    def move_down(self):
        self.direction = 'down'


    def move_left(self):
        self.direction = 'left'


    def move_right(self):
        self.direction = 'right'

    def walk(self):
        for index in range(self.length -1, 0, -1):
            self.block_x[index] = self.block_x[index - 1]
            self.block_y[index] = self.block_y[index - 1]

        
        if self.direction == 'up':
            self.block_y[0] -= SIZE
        if self.direction == 'down':
            self.block_y[0]+= SIZE
        if self.direction == 'left':
            self.block_x[0] -= SIZE
        if self.direction == 'right':
            self.block_x[0] += SIZE

        self.draw()
        


class Game():
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,500)) #window size
        self.surface.fill((44,44,84)) #window color
        self.snake = Snake(self.surface, 7)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()
    
