# Yin-Yang battling over the screen
import pygame, random
pygame.init()
resolution = [800, 600]
screen = pygame.display.set_mode(resolution)
running = True
clock = pygame.time.Clock()
framerate = 60
dt = 0

size = 25
rate = 500
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

blood = 0
state = 0 

for n in range(grid_size[0]):
  if n < half:
    map = 0
  else:
    map = 1
  box[n] = [map] * grid_size[1]

while running:  # Game Loop
    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0] and not button_check:
            LeftClick = True

    if LeftClick:
        LeftClick = False
        button_check = True
        
    if state == 0:
      yin = (255, 255 - blood, 255 - blood)
      yang = (0, 0, 0)
    elif state == 1:
      yin = (255, 0, 0)
      yang = (0 + blood, 0 + blood, 0 + blood)
    elif state == 2:
      yin = (255 - blood, 0, 0)
      yang = (255, 255, 255)
    elif state == 3:
      yin = (0, 0, 0)
      yang = (255, 255 - blood, 255 - blood)
    elif state == 4:
      yin = (0 + blood, 0 + blood, 0 + blood)
      yang = (255, 0, 0)
    elif state == 5:
      yin = (255, 255, 255)
      yang = (255 - blood, 0, 0)
      
    for n in range(grid_size[0]):
        for m in range(grid_size[1]):
            boundary = [n*size, m*size]
            if box[n][m] == 0:
                color = yang
                if abs(boundary[0] - location[0]) < size and abs(boundary[1] - location[1]) < size and speed_x < 0:
                    box[n][m] = 1
                    speed_x = -speed_x  
            elif box[n][m] == 1:
                color = yin
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
    pygame.draw.rect(screen, yin, (position[0], position[1], size, size))
    
    location[0] += dt * speed_x
    location[1] += dt * speed_y
    pygame.draw.rect(screen, yang, (location[0], location[1], size, size))

    if event.type == pygame.MOUSEBUTTONUP:
        button_check = False

    if state < 3:
      mod = 1.0005
    else:
      mod = .9995
    rate_x *= mod
    rate_y *= mod
    speed_x *= mod
    speed_y *= mod
    
    blood += 20*dt
    if blood >= 255:
      blood = 0
      state += 1
      if state > 5:
        state = 0  
        rate_x = rate * rate_x / abs(rate_x)
        rate_y = rate * rate_y / abs(rate_y) 
        speed_x = rate * speed_x / abs(speed_x)
        speed_y = rate * speed_y / abs(speed_y)

    pygame.display.update()
    dt = clock.tick(framerate) / 1000	# Makes movement or time-related events work independent of framerate
    clock.tick(framerate)         	# Sets frames/sec

pygame.quit()
