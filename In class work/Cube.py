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

        if self.controls.get('space') and keys[self.controls['space']]:
            self.y -= self.speed
            self.direction = 'space'

     def move(Self):
            if self.direction == 'right':