import pygame
import time
class Ball:
    def __init__(self, x, y, radius, color, speed, direction, hitValue, controls=None):
       self.x = x
       self.y = y
       self.radius = radius
       self. color = color
       self.speed = speed
       self.direction = direction
       self.controls = controls or {}
       self.stunned_until = 0
       self.hitValue = hitValue


    def stun(self, seconds: float):  
        self.stunned_until = time.time() + seconds


    def is_stunned(self):
        return time.time() < self.stunned_until


    def move(self, keys, width: int, height: int,enemy):


        if self.is_stunned():
            return
       
        if self.controls.get('up') and keys[self.controls['up']]:
            self.y -= self.speed
            self.direction = 'up'
            if self.y <= self.radius:
                self.y = self.radius
        if self.controls.get('down') and keys[self.controls['down']]:
            self.y += self.speed
            self.direction = 'down'
            if self.y >= height - self.radius:
                self.y = height - self.radius
        if self.controls.get('left') and keys[self.controls['left']]:
            self.x -= self.speed
            self.direction = 'left'
            if self.x <= self.radius:
                self.x = self.radius
        if self.controls.get('right') and keys[self.controls['right']]:
            self.x += self.speed
            self.direction = 'right'
            if self.x >= width - self.radius:
                self.x = width - self.radius


    def fall(self):
        self.y += self.speed
   
    def fly(self):
        if self.direction == 'left':
            self.x -= self.speed
        if self.direction == 'right':
            self.x += self.speed


    def collideCheck(self, ball_x, ball_y, ball_radius):
        distance = ((self.x - ball_x) ** 2 + (self.y - ball_y) ** 2) ** 0.5
        return distance <= self.radius + ball_radius
   
    def draw(self, surface):
        if self.is_stunned():
            if int(time.time() * 10) % 2 == 0:
                pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        else:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
