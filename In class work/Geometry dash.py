import pygame as py

py.init()

size = WIDTH, HEIGHT = 560, 320
screen = py.display.set_mode((size))

py.display.set_caption("Jump!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRENY = (34, 84, 54)
RED = (255,0, 0)

FPS = 60
clock = py.time.Clock()

cube_controls = {
    'jump':py.K_SPACE,
}

cube = cube_controls(WIDTH/2, HEIGHT-50,25,RED,5,'left',5,cube_controls)

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False

py.display.update()
clock.tick(FPS)

py.quit()

