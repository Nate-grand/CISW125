import pygame

class Bullet:

    def __init__(self, color1, direction, x, y,ballRadius, speed):
        self.color = color1
        self.direction = direction
        self.x = x
        self.y = y
        self.radius = .2 * ballRadius
        self.speed = speed + 3
        self.canFire = True

    def drawBullet(self, screen):
        if self.canFire:
            if self.direction in ['left', 'right']:
                width = int(self.radius * 4)
                height = int(self.radius * 2)
            else:  # 'up' or 'down'
                width = int(self.radius * 2)
                height = int(self.radius * 4)
                
            
            rect = pygame.Rect(
                int(self.x - width // 2),
                int(self.y - height // 2),
                width,
                height
            )

            pygame.draw.ellipse(screen, self.color, (rect))

    def move(self):
        if self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed

    def collideCheck(self, ball_x, ball_y, ball_radius):
        # Simple circle collision
        distance = ((self.x - ball_x) ** 2 + (self.y - ball_y) ** 2) ** 0.5
        return distance <= ball_radius