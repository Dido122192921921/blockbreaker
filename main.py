import pygame
from paddle import *
from ball import *
from block import *

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
        self.ball = Ball(400, 300, self.window, self.ball_img)
        #paddle
        self.paddle = Paddle(350, 378, self.window, self.paddle_img)
        
        #time
        self.clock = pygame.time.Clock()

        self.block_img = pygame.image.load("images/pink_block.png")
        self.block_img = pygame.transform.scale(self.block_img, (64, 32))
        self.blocks = []

        self.x_pos = self.cal_x_pos()
        self.block = Block(0, 0, self.window, self.block_img)
        self.x_pos = self.cal_x_pos()
        self.y_pos = self.cal_y_pos()
        for y in self.y_pos:
            for x in self.x_pos:
                self.blocks.append(Block(x, y, self.window, self.block_img))

    def cal_x_pos(self):
        block_w = self.block_img.get_width()
        gap = 10
        total_blocks = self.window.get_width() // (block_w + gap)
        side_gap = (self.window.get_width() - ((block_w + gap) * total_blocks) + gap) // 2
        lst = []
        for x in range(total_blocks):
            lst.append(side_gap + (block_w + gap)* x)
        return lst

    def cal_y_pos(self):
        gap = 10
        block_h = self.block_img.get_height()
        lst = []
        for y in range(4):
            lst.append(gap + (block_h + gap) * y)
        return lst


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
            for block in self.blocks:
                block.draw()
            self.check_collision()
            pygame.display.update()
                    
        pygame.quit()
    def check_collision(self):
        if self.ball.ball_rect.colliderect(self.paddle.paddle_rect):
            self.ball.is_collide = True

        for block in self.blocks:
            if self.ball.ball_rect.colliderect(block.block_rect):
                self.blocks.remove(block)
                self.ball.increase_velo()
                self.ball.collide_block()
        
        
if __name__ == "__main__":
    game = Game()
    game.run()
        