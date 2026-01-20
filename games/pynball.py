# Pynball
import pygame, random, math, numpy as np
from pygame import K_ESCAPE

pygame.init()
resolution = [800, 600]
screen = pygame.display.set_mode(resolution)
running = True
clock = pygame.time.Clock()
framerate = 120
frame_counter = 0
dt = 0
sample_size = 240
dt_array = np.array([0.04] * sample_size)

# A global dict value that will contain all the Pygame
# Surface objects returned by pygame.image.load().
IMAGESDICT = {'cosmic_p': pygame.image.load('lib/cosmic.jpg'),
              '{placeholder}': pygame.image.load('lib/cosmic.jpg')}
cosmic = IMAGESDICT['cosmic_p']
sz = cosmic.get_size()
scl = 200/sz[0]
cosmic = pygame.transform.scale(cosmic, (sz[0] * scl, sz[1] * scl))

dimensions = [80, 120]
scale = resolution[1] / dimensions[1]
size = [dimensions[0] * scale, dimensions[1] * scale]
border = 10
edges = [int((resolution[0] - size[0]) / 2 + border * 2), int((resolution[0] + size[0]) / 2 - border * 2)]
LeftClick = False
RightClick = False
escape = False
button_check = False

font_mono20 = pygame.font.SysFont("Mono", 20, bold=False, italic=False)
font_helv20 = pygame.font.SysFont("Helvetica", 20, bold=False, italic=False)

def draw_text(text, font, text_col, x, y):  # function for outputting text onto the screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

class Pinball():
    def __init__(self, pos, color, size, speed):
        self.pos = pos
        self.color = color
        self.size = size
        self.speed = speed
        
    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.size)
        
    def fall(self, interval):
        self.speed[1] = self.speed[1] + gravity * interval
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
        
launcher = [resolution[0]- 230, resolution[1] - 50]

ball = Pinball(launcher, (255, 255, 255), 7, [0, -40])
score = 0

gravity = 30
elasticity = 0.8
bumpers = [Bumper([575, 25], (150, 150, 150), 13),]

cluster = [480, 200]
bumpers.append(Bumper([cluster[0] + 40, cluster[1]], (150, 150, 150), 12))
bumpers.append(Bumper([cluster[0], cluster[1] + 20], (150, 150, 150), 12))
bumpers.append(Bumper([cluster[0] - 40, cluster[1]], (150, 150, 150), 12))

for p in range(random.choice(range(3, 5))):
    x = random.choice(range(edges[0]+20, edges[1]-40))
    y = random.choice(range(150, 400))
    bumpers.append(Bumper([x, y],(150, 150, 150), 12))

# debug
# ball.speed[1] = -5
# gravity = 0
# elasticity = 1

hitstop = 1
hitstop_limit = 0.03

while running:  # Game Loop
    for event in pygame.event.get():
        if pygame.key.get_pressed()[K_ESCAPE]:
            escape = True
            running = False
        if pygame.mouse.get_pressed()[0] and not button_check:
            LeftClick = True
        elif pygame.mouse.get_pressed()[1] and not button_check:
            RightClick = True

    if LeftClick and not button_check:
        LeftClick = False
        button_check = True
        ball.speed[1] *= 2

    if RightClick:
        RightClick = False
        button_check = True

    screen.fill([0, 0, 0])
    screen.blit(cosmic, [0, 0])
    
    pygame.draw.rect(screen, [50, 50, 50], [resolution[0]/2 - size[0]/2, 0, size[0], size[1]], border)
    buff = ball.size + border

    if hitstop > hitstop_limit:
        if abs(ball.speed[1]) >= 2 or ball.pos[1] <= resolution[1] - buff:
            ball.fall(dt)
        else:
            ball.speed[1] = 0
            ball.pos[1] = resolution[1] - buff
            
        if ball.pos[1] > resolution[1] - buff:
            ball.pos[1] = resolution[1] - buff
    
    
        # Walls
        if ball.pos[1] >= resolution[1] - buff and ball.speed[1] > 0:
            hitstop = 0
            ball.pos[1] = resolution[1] - buff
            ball.speed[1] = -elasticity * ball.speed[1]
        elif ball.pos[1] <= buff and ball.speed[1] < 0:
            hitstop = 0
            ball.pos[1] = buff
            ball.speed[1] = -elasticity * ball.speed[1]
    
        if ball.pos[0] <= edges[0] and ball.speed[0] < 0:
            hitstop = 0
            ball.speed[0] = -elasticity * ball.speed[0]
        elif ball.pos[0] >= edges[1] and ball.speed[0] > 0:
            hitstop = 0
            ball.speed[0] = -elasticity * ball.speed[0]

    magnitude = (ball.speed[0] ** 2 + ball.speed[1] ** 2) ** 0.5
    heading = math.atan(ball.speed[1] / (ball.speed[0] + .001))
    
    for b in range(len(bumpers)):
        bumpers[b].draw()
        distance = [bumpers[b].pos[0] - ball.pos[0], bumpers[b].pos[1] - ball.pos[1]]
        pythag = (abs(distance[0]) ** 2 + abs(distance[1]) ** 2) ** 0.5
        hitbox = ball.size + bumpers[b].size
        cushion = hitbox * 1.002

        if pythag <= hitbox and hitstop > hitstop_limit:
            while pythag < cushion:
                ball.pos[0] -= ball.speed[0]/100
                ball.pos[1] -= ball.speed[1]/100 
                distance = [bumpers[b].pos[0] - ball.pos[0], bumpers[b].pos[1] - ball.pos[1]]
                pythag = (abs(distance[0]) ** 2 + abs(distance[1]) ** 2) ** 0.5
            hitstop = 0
            score += 10
            theta = math.atan(distance[1] / (distance[0]+.001))
            if distance[0] <= 0:
                ball.speed[0] = magnitude * (elasticity * math.cos(theta))
                ball.speed[1] = magnitude * (elasticity * math.sin(theta))
            else: 
                ball.speed[0] = -magnitude * (elasticity * math.cos(theta))
                ball.speed[1] = - magnitude * (elasticity * math.sin(theta))

    ball.draw()
    draw_text(f"Score: {score}", font_mono20, (220, 230, 230), 20, 400)

    # Debug section
    # Framerate display
    rolling_frame = frame_counter % sample_size
    dt_array[rolling_frame] = dt
    dt_sum = np.sum(dt_array, dtype = np.float32)
    fps_counter = np.uint8(sample_size / dt_sum)
    draw_text(f"FPS: {fps_counter}", font_mono20, (200, 200, 200), resolution[0] - 100, resolution[1]-150)
    draw_text(f"{frame_counter:,}", font_mono20, (0, 0, 0), 850, resolution[1]-125)
        
    if event.type == pygame.KEYUP:
        button_check = False
        escape = False
    if event.type == pygame.MOUSEBUTTONUP:
        button_check = False
        LeftClick = False
        RightClick = False

    pygame.display.update()
    dt = clock.tick(framerate) / 1000  # Makes movement or time-related events work independent of framerate
    hitstop += dt
    frame_counter += 1
    clock.tick(framerate)  # Sets frames/sec

pygame.quit()
