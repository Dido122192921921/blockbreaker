import pygame
import math
from paddle import *
class Ball:

    def __init__(self, x, y, window, image):
        self.window = window
        self.image = image
        self.ball_rect = self.image.get_rect(x = x, y = y)
        self.angle = math.pi / -3
        self.velocity = 100
        self.velocity_x = self.velocity * math.cos(self.angle)
        self.velocity_y = self.velocity * math.sin(self.angle)
        self.is_collide = False

    def draw(self, delta_time, paddle):
        self.move(delta_time, paddle)
        self.window.blit((self.image), (self.ball_rect.x, self.ball_rect.y))

    def move(self, delta_time, paddle):
        self.ball_rect.x += self.velocity_x * delta_time
        self.ball_rect.y += self.velocity_y * delta_time

        if self.is_collide:
            self.ball_rect.bottom = paddle.paddle_rect.top
            self.velocity_y *= -1
            self.is_collide = False

        if self.ball_rect.y < 0:
            self.ball_rect.y = 0
            self.velocity_y *= -1

        if self.ball_rect.x > self.window.get_width() - self.ball_rect.w:
            self.ball_rect.x = self.window.get_width() - self.ball_rect.w
            self.velocity_x *= -1
        if self.ball_rect.x < 0:
            self.ball_rect.x = 0
            self.velocity_x *= -1
    def collide_block(self):
        self.velocity_y *= -1

    def increase_velo(self):
        self.velocity_x *= 1.06
        self.velocity_y *= 1.06