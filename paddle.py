import pygame

class Paddle:
    
    def __init__(self, x: int, y: int, window: pygame.Surface, image: pygame.Surface):
        self.window = window
        self.image = image
        self.paddle_rect = self.image.get_rect(topleft=(x, y))
        self.velocity = 0
        self.acceleration = 200
        self.max_velocity = 400
        self.friction = 0.9
        
    def draw(self, delta_time):
        self.window.blit(self.image, (self.paddle_rect.x, self.paddle_rect.y))
        self.control(delta_time)
        
    def control(self, delta_time):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_LEFT]:
            self.velocity -= self.acceleration * delta_time
        elif pressed[pygame.K_RIGHT]:
            self.velocity += self.acceleration * delta_time
        else:
            self.velocity *= self.friction
        
        if self.velocity > self.max_velocity:
            self.velocity = self.max_velocity
        elif self.velocity < -self.max_velocity:
            self.velocity = -self.max_velocity
        
        self.paddle_rect.x += self.velocity * delta_time
        
        if self.paddle_rect.left < 0:
            self.paddle_rect.left = 0
            self.velocity = 0
        elif self.paddle_rect.right > self.window.get_width():
            self.paddle_rect.right = self.window.get_width()
            self.velocity = 0