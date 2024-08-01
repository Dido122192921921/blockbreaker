import pygame
from paddle import *

class Game():
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode( (1200, 600) )
        pygame.display.set_caption("Block Breaker")
        self.bg = pygame.image.load("images/bg.jpeg")
        self.paddle_img = pygame.image.load("images/paddle.png")
        self.paddle_img = pygame.transform.scale(self.paddle_img, (self.paddle_img.get_width() * 2, self.paddle_img.get_height() * 2))
        
        #paddle
        self.paddle = Paddle(350, 450, self.window, self.paddle_img)
        
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
            pygame.display.update()
                    
        pygame.quit()
        
        
if __name__ == "__main__":
    game = Game()
    game.run()
        