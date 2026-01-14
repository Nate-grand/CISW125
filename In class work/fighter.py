# nathan macbeth
# 14/1/26
# Fighter Game

import pygame as py
from Ball2 import Ball
import time
import random
from Bullet import Bullet

py.init()

size = WIDTH, HEIGHT = 980, 720
screen = py.display.set_mode((size))

py.display.set_caption("fire")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRENY = (34, 84, 54)
RED = (255,0, 0)

FPS = 60
clock = py.time.Clock()


mainballcontrols = {
    'left':py.K_LEFT,
    'right':py.K_RIGHT,
}

mainball = Ball(WIDTH/2, HEIGHT-50,25,GRENY,5,'left',5,mainballcontrols)


enemyBalls = []
for i in range(5):
    enemyBalls.append(Ball(random.randint(50, WIDTH -50), random.randint(-50, 0), random.randint(5,10),RED,random.randint(6,7),'down',1))

bullets = []
last_bullet_time = 0
bullet_cooldown = 0.5

running = True

game_over = False

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False


    keys = py.key.get_pressed()

    if not game_over:
        if keys[py.K_SPACE]:
            current_time = time.time()
            if current_time - last_bullet_time > bullet_cooldown:
                bullets.append(Bullet(WHITE, 'up', mainball.x, mainball.y,mainball.radius, mainball.speed))
                last_bullet_time = current_time

            for bullet in bullets[:]:
                if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
                    bullets.remove(bullet)


        for bullet in bullets[:]:
            bullet.move()
            bullet.drawBullet(screen)

        for enemy in enemyBalls:
            enemy.fall()
            if mainball.collideCheck(enemy.x, enemy.y, enemy.radius):
                if(not mainball.is_stunned()):
                    mainball.hitValue -= 1
                    enemyBalls.remove(enemy)
                    enemyBalls.append(Ball(random.randint(50, WIDTH -50), random.randint(-50, 0), random.randint(5,10),BLUE,random.randint(6,7),'down',3))
                    if mainball.hitValue < 1:
                        print("Game Over")
                        gameover = True
                mainball.stun(1)

            enemy.draw(screen)
            for bullet in bullets[:]:
                if bullet.collidecheck(enemy.x, enemy.y, enemy.radius):
                    bullets.remove(bullet)
                    enemy.hitvalue -= 1
                    if enemy.hitvalue < 1:
                        enemyBalls.remove(enemy)
                        enemyBalls.append(Ball(random.randint(50, WIDTH -50), random.randint(-50, 0), random.randint(5, 10),(150,0,255),4,"down",7))

            if enemy.y > HEIGHT:
                enemyBalls.remove(enemy)
                enemyBalls.append(Ball(random.randint(50, WIDTH -50), random.randint(-50, 0), random.randint(5,10),(150,150,250),"down",7))

        mainball.move(keys, WIDTH, HEIGHT, False)
        mainball.draw(screen)

    elif gameover:
        py.font.init()
        font = py.font.SysFont('Arial', 72)
        text = "GAME OVER!!!"
        text1 = font.render(text, True, RED)
        textwidth, textheight = font.size(text)

        screen.blit(text1, ((WIDTH - textwidth) // 2),(HEIGHT - textheight) // 2)


    py.display.update()
    clock.tick(FPS)

py.quit()


       