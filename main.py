import pygame
from paddle import *
from ball import *

class Game():
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode( (736, 414) )
        pygame.display.set_caption("Block Breaker")
        self.bg = pygame.image.load("images/bg7.jpg")
        self.paddle_img = pygame.image.load("images/paddle.png")
        self.paddle_img = pygame.transform.scale(self.paddle_img, (self.paddle_img.get_width() * 2, self.paddle_img.get_height() * 2))
        self.ball_img = pygame.image.load("images/ball.png")
        self.ball_img = pygame.transform.scale(self.ball_img, (self.ball_img.get_width() * 1, self.ball_img.get_height( ) * 1))
        self.ball = Ball(350, 400, self.window, self.ball_img)
        #paddle
        self.paddle = Paddle(350, 378, self.window, self.paddle_img)
        
        #time
        self.clock = pygame.time.Clock()
    
    def run(self):
        running = True

        
        while running:
        
            self.delta_time = self.clock.tick(60) / 1000
            self.window.blit(self.bg, (0, 0))    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.paddle.draw(self.delta_time)
            self.ball.draw(self.delta_time, self.paddle)
            self.check_collision()
            pygame.display.update()
                    
        pygame.quit()
    def check_collision(self):
        if self.ball.ball_rect.colliderect(self.paddle.paddle_rect):
            self.ball.is_collide = True
        
        
if __name__ == "__main__":
    game = Game()
    game.run()
        