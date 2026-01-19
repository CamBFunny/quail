# Pynball
import pygame, random, math
from pygame import K_ESCAPE

pygame.init()
resolution = [800, 600]
screen = pygame.display.set_mode(resolution)
running = True
clock = pygame.time.Clock()
framerate = 60
dt = 0

# cosmic = pygame.image.load('lib/cosmic.jpg')
# sz = cosmic.get_size()
# scl = 200/sz[0]
# cosmic = pygame.transform.scale(cosmic, (sz[0] * scl, sz[1] * scl)) 

dimensions = [80, 120]
scale = resolution[1] / dimensions[1]
size = [dimensions[0] * scale, dimensions[1] * scale]

LeftClick = False
RightClick = False
escape = False
button_check = False 

gravity = 30

class Pinball():
    def __init__(self, pos, color, size, speed):
        self.pos = pos
        self.color = color
        self.size = size
        self.speed = speed
        
    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.size)
        
    def fall(self, interval):
        self.speed = [self.speed[0], self.speed[1] + gravity * interval]
        self.pos = [self.pos[0] + self.speed[0], self.pos[1] + self.speed[1]]
        
class Flipper():
    def __init__(self, pos, color, size):
        self.pos = pos
        self.color = color
        self.size = size
    
class Slingshot():
    def __init__(self, pos, color, size):
        self.pos = pos
        self.color = color
        self.size = size
    
class Bumper():
    def __init__(self, pos, color, size):
        self.pos = pos
        self.color = color
        self.size = size
        
    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.size)
        
launcher = [resolution[0]- 225, resolution[1] - 50]

ball = Pinball(launcher, (255, 255, 255), 7, [0, -30])

bump1 = Bumper([585, 300], (150, 150, 150), 12)

# Debug
# ball.speed[1] = -3
# gravity = 0

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
    # screen.blit(cosmic, [0, 0])
    
    border = 10
    pygame.draw.rect(screen, [50, 50, 50], [resolution[0]/2 - size[0]/2, 0, size[0], size[1]], border)
    bump1.draw()
    buff = ball.size + border
    
    if abs(ball.speed[1]) >= 1.5 or ball.pos[1] <= resolution[1] - buff: 
        ball.fall(dt)
    else:
        ball.speed[1] = 0
        ball.pos[1] = resolution[1] - buff
        
    if ball.pos[1] > resolution[1] - buff:
        ball.pos[1] = resolution[1] - buff
    
    if ball.pos[1] >= resolution[1] - buff and ball.speed[1] > 0: 
        ball.speed[1] = -0.8 * ball.speed[1]
        
    distance = [bump1.pos[0] - ball.pos[0], bump1.pos[1] - ball.pos[1]]  
    pythag = (abs(distance[0]) ** 2 + abs(distance[1]) ** 2) ** 0.5
    hitbox = ball.size + bump1.size
    if pythag <= hitbox:  
        theta = math.atan(distance[1] / distance[0]) 
        #if distance[0] == 0:
            #if distance[1] > 0:
               # theta = math.pi / 2
            #elif distance[1] < 0:
               # theta = math.pi * 1.5
       # else: 
        ball.speed[0] = -ball.speed * (0.8 * math.sin(theta))
        # ball.speed[1] = -ball.speed[1] * (0.8 * math.sin(theta))  
        
    ball.draw()

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
