import pygame

WIDTH = 700
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The Pong game!  Jugador A : izquierda Jugador B : derecha")

FPS = 60 # frame per sec

BLUE = (10,33,180) 
BLACK = (0,0,0)
FOREST_GREEN = (47, 117, 80)
LIGHT_GREEN = (21, 100, 194)
BALL_RADIUS = 10

PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20

pygame.font.init()
SCORE_FONT = pygame.font.SysFont("comicsans",40)
WINNING_SCORE = 5
 
class Ball:
    MAX_VELOCITY = 5
    COLOR = BLACK

    def __init__(self,x,y,radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VELOCITY
        self.y_vel = 0

    def draw(self,WINDOW):
        pygame.draw.circle(WINDOW, self.COLOR,(self.x,self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1

class Paddle:
    COLOR = BLUE
    VELOCITY = 3

    def __init__(self,x,y,width,height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self,WINDOW):
        pygame.draw.rect(WINDOW,self.COLOR,(self.x,self.y,self.width,self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y



def draw(WINDOW, paddles, ball, left_score, right_score):
    WINDOW.fill(LIGHT_GREEN)

    left_score_text = SCORE_FONT.render(f"{left_score}",1,BLACK)
    right_score_text = SCORE_FONT.render(f"{right_score}",1,BLACK)
    WINDOW.blit(left_score_text,(WIDTH//4 - left_score_text.get_width()//2, 20))
    WINDOW.blit(right_score_text,(WIDTH*3//4 - right_score_text.get_width()//2, 20))

    for paddle in paddles:
        paddle.draw(WINDOW)

    for i in range(10,HEIGHT,HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(WINDOW,BLACK,(WIDTH//2 - 5, i , 10,HEIGHT//20))

    ball.draw(WINDOW)

    pygame.display.update()

def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *=-1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1
    
    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
             if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                 ball.x_vel *= -1

                 middle_y = left_paddle.y + left_paddle.height/2
                 difference_y = middle_y - ball.y
                 reduction_factor = (left_paddle.height / 2) / ball.MAX_VELOCITY
                 y_vel = difference_y / reduction_factor
                 ball.y_vel = -1 * y_vel


    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:      
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1


                middle_y = right_paddle.y + right_paddle.height/2
                difference_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) /ball.MAX_VELOCITY
                y_vel = difference_y / reduction_factor
                ball.y_vel = -1 * y_vel

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
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    while run:
        clock.tick(FPS)
        draw(WINDOW, [left_paddle,right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_move(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        won = False

        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Jugador A ganó !   A player won!"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Jugador B ganó!   B player won!"


        if won:
            text = SCORE_FONT.render(win_text,1,BLUE)
            WINDOW.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)

            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0


    pygame.quit()

if __name__ == "__main__":
    main()