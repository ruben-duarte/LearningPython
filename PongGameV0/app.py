import pygame

WIDTH = 700
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The Pong game!")

FPS = 60 # frame per sec

BLUE = (10,33,180) 
BLACK = (0,0,0)
FOREST_GREEN = (47, 117, 80)
LIGHT_GREEN = (21, 100, 194)

PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20

class Paddle:
    COLOR = BLUE
    VELOCITY = 3

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self,WINDOW):
        pygame.draw.rect(WINDOW,self.COLOR,(self.x,self.y,self.width,self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY



def draw(WINDOW, paddles):
    WINDOW.fill(LIGHT_GREEN)

    for paddle in paddles:
        paddle.draw(WINDOW)

    for i in range(10,HEIGHT,HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(WINDOW,BLACK,(WIDTH//2 - 5, i , 10,HEIGHT//20))

    pygame.display.update()

def handle_paddle_move(keys,left_paddle,right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VELOCITY >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VELOCITY + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VELOCITY >= 0 :
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VELOCITY + right_paddle.height<= HEIGHT:
        right_paddle.move(up=False)
    

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10,HEIGHT//2 - PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH,HEIGHT//2 - PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(WINDOW, [left_paddle,right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_move(keys, left_paddle, right_paddle)


    pygame.quit()

if __name__ == "__main__":
    main()