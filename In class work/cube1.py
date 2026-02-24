import pygame
import time
class Cube:
    def __init__(self, x, y, color, speed, direction, hitValue, controls=None):
       self.x = x
       self.y = y
       self. color = color
       self.speed = speed
       self.direction = direction
       self.controls = controls or {}
       self.stunned_until = 0
       self.hitValue = hitValue

       while self.controls.get('space') and controls[self.controls['space']]:

        if self.controls.get('space') and controls[self.controls['space']]:
            self.y -= self.speed
            self.direction = 'space'

            def move(self):
                if self.direction == 'right':
                    self.x += self.speed