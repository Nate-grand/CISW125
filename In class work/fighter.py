









py.init()

size = WIDTH, Height = 980, 720
screen = py.display.set_mode((size))

py.display.set_caption("fire")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRENY = (34, 84, 54)

FPS = 60
clock = py.time.Clock()


mainballcontrols = {
    'left':py.K_left,
    'right':py.K_right,
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
        if keys[py.K_space]:
            current_time = time.time()
            if current_time - last_bullet_time > bullet_cooldown:
                bullets.append(Bullet(WHITE, 'up', mainball.x, mainball.y,mainball.radius, mainball.speed))
                last_bullet_time = current_time

            for bullet in bullets[:]:
                if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > Height:
                    bullet.remove(bullet)


        for bullet in bullets[:]:
            bullet.move()
            bullet.drawBullet(screen)


        