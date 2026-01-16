# Yin-Yang battling over the screen
import pygame, random
pygame.init()
resolution = [800, 600]
screen = pygame.display.set_mode(resolution)
running = True
clock = pygame.time.Clock()
framerate = 60
dt = 0

size = 40
rate = 350
LeftClick = False
button_check = False

position = [0, random.choice(range(resolution[1]))]
rate_x = rate
rate_y = rate

location = [resolution[0]-size, random.choice(range(resolution[1]))]
speed_x = -rate
speed_y = -rate


grid_size = [resolution[0] // size, resolution[1] // size]
box = [[0] * grid_size[1]] * grid_size[0]
half = grid_size[0] // 2

for n in range(half):
    box[n + half] = [1] * grid_size[1]

while running:  # Game Loop
    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0] and not button_check:
            LeftClick = True

    if LeftClick:
        LeftClick = False
        button_check = True

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (resolution[0]/2, 0, resolution[0], resolution[1]))

    for n in range(grid_size[0]):
        for m in range(grid_size[1]):
            boundary = [n*size, m*size]
            if box[n][m] == 0:
                color = (0, 0, 0)
                if abs(boundary[0] - location[0]) < size and abs(boundary[1] - location[1]) < size and speed_x < 0:
                    box[n][m] = 1
                    speed_x = -speed_x 
            elif box[n][m] == 1:
                color = (255, 255, 255)
                if abs(boundary[0] - position[0]) < size and abs(boundary[1] - position[1]) < size and rate_x > 0:
                    box[n][m] = 0
                    rate_x = -rate_x 
            pygame.draw.rect(screen, color, (n*size, m*size, size, size))

    if position[0] + size >= screen.get_width() and rate_x > 0:
        rate_x = -rate_x
    if position[0] <= 0 and rate_x < 0:
        rate_x = -rate_x
    if position[1] + size >= screen.get_height() and rate_y > 0:
        rate_y = -rate_y
    if position[1] <= 0 and rate_y < 0:
        rate_y = -rate_y
        

    if location[0] + size >= screen.get_width() and speed_x > 0:
        speed_x = -speed_x
    if location[0] <= 0 and speed_x < 0:
        speed_x = -speed_x
    if location[1] + size >= screen.get_height() and speed_y > 0:
        speed_y = -speed_y
    if location[1] <= 0 and speed_y < 0:
        speed_y = -speed_y

    position[0] += dt * rate_x
    position[1] += dt * rate_y
    pygame.draw.rect(screen, (255, 255, 255), (position[0], position[1], size, size))
    
    location[0] += dt * speed_x
    location[1] += dt * speed_y
    pygame.draw.rect(screen, (0, 0, 0), (location[0], location[1], size, size))

    if event.type == pygame.MOUSEBUTTONUP:
        button_check = False

    mod = 1.0002
    rate_x *= mod
    rate_y *= mod

    pygame.display.update()
    dt = clock.tick(framerate) / 1000	# Makes movement or time-related events work independent of framerate
    clock.tick(framerate)         	# Sets frames/sec

pygame.quit()
