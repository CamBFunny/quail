# Pynball
import pygame, random
from pygame import K_ESCAPE

pygame.init()
resolution = [800, 600]
screen = pygame.display.set_mode(resolution)
running = True
clock = pygame.time.Clock()
framerate = 60
dt = 0

dimensions = [80, 120]
scale = resolution[1] / dimensions[1]
size = [dimensions[0] * scale, dimensions[1] * scale]

LeftClick = False
RightClick = False
escape = False
button_check = False
cosmic = pygame.image.load('lib/cosmic.jpg')
sz = cosmic.get_size()
scl = 200/sz[0]
cosmic = pygame.transform.scale(cosmic, (sz[0] * scl, sz[1] * scl))

while running:  # Game Loop
    for event in pygame.event.get():
        if pygame.key.get_pressed()[K_ESCAPE]:
            escape = True
            running = False
        if pygame.mouse.get_pressed()[0] and not button_check:
            LeftClick = True
        elif pygame.mouse.get_pressed()[1] and not button_check:
            RightClick = True

    if LeftClick:
        LeftClick = False
        button_check = True

    if RightClick:
        RightClick = False
        button_check = True

    screen.fill([0, 0, 0])
    pygame.draw.rect(screen, [50, 50, 50], [resolution[0]/2 - size[0]/2, 0, size[0], size[1]], 10)

    screen.blit(cosmic, [0, 0])

    if event.type == pygame.KEYUP:
        button_check = False
        escape = False
    if event.type == pygame.MOUSEBUTTONUP:
        button_check = False
        LeftClick = False
        RightClick = False

    pygame.display.update()
    dt = clock.tick(framerate) / 1000  # Makes movement or time-related events work independent of framerate
    clock.tick(framerate)  # Sets frames/sec

pygame.quit()
