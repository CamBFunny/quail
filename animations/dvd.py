# Makes python logo bounce around screen like DVD screensaver
import pygame
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
screen = pygame.display.set_mode([800, 600])
running = True
clock = pygame.time.Clock()
framerate = 30
dt = 0

python = pygame.image.load('lib/python_logo.png')
sz = python.get_size()
scl = 100/sz[1]
python = pygame.transform.scale(python, (sz[0] * scl, sz[1] * scl))
size = [python.get_size(), 0]

dvd = pygame.image.load('lib/dvd.png')
sz = dvd.get_size()
scl = 100/sz[1]
dvd = pygame.transform.scale(dvd, (sz[0] * scl, sz[1] * scl))
size[1] = dvd.get_size()

logo = [python, dvd]
index = 0

position = [0, 0]
rate = 150
rate_x = rate
rate_y = rate
LeftClick = False
button_check = False

while running:  # Game Loop
    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0] and not button_check:
            LeftClick = True
        if event.type == pygame.QUIT:
            running = False

    if LeftClick:
        LeftClick = False
        button_check = True
        index += 1
        if index >= 2:
            index = 0

    screen.fill((0, 0, 0))
    if position[0] + size[index][0] >= screen.get_width() and rate_x > 0:
        rate_x = -rate_x
    if position[0] <= 0 and rate_x < 0:
        rate_x = -rate_x
    if position[1] + size[index][1] >= screen.get_height() and rate_y > 0:
        rate_y = -rate_y
    if position[1] <= 0 and rate_y < 0:
        rate_y = -rate_y

    position[0] += dt * rate_x
    position[1] += dt * rate_y
    screen.blit(logo[index], position)  # Position the image at (0, 0)

    if event.type == pygame.MOUSEBUTTONUP:
        button_check = False

    pygame.display.update()
    dt = clock.tick(framerate) / 1000	# Makes movement or time-related events work independent of framerate
    clock.tick(framerate)         	# Sets frames/sec
pygame.quit()