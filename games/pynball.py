# Pynball
import pygame, random, math, numpy as np
from pygame.locals import (KEYDOWN, QUIT, KEYUP, K_LCTRL, MOUSEWHEEL,
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, K_TAB, K_LSHIFT, K_SPACE,
    K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0, K_p,
                           K_q, K_w, K_e, K_r, K_t,
                           K_a, K_s, K_d, K_f, K_g,
                           K_z, K_x, K_c, K_v, K_b)

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
# IMAGESDICT = {'cosmic_p': pygame.image.load('lib/cosmic.jpg'),
              # '{placeholder}': pygame.image.load('lib/cosmic.jpg')}
# cosmic = IMAGESDICT['cosmic_p']
# sz = cosmic.get_size()
# scl = 200/sz[0]
# cosmic = pygame.transform.scale(cosmic, (sz[0] * scl, sz[1] * scl))

dimensions = [80, 120]
scale = resolution[1] / dimensions[1]
size = [dimensions[0] * scale, dimensions[1] * scale]
border = 10
edges = [int((resolution[0] - size[0]) / 2 + border * 2), int((resolution[0] + size[0]) / 2 - border * 2)]
LeftClick = False
RightClick = False
escape = False
button_check = False
space_button = False
flip_left = False
flip_right = False

font_mono20 = pygame.font.SysFont("Mono", 20, bold=False, italic=False)
font_helv20 = pygame.font.SysFont("Helvetica", 20, bold=False, italic=False)

def draw_text(text, font, text_col, x, y):  # function for outputting text onto the screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def dprint(text):
    if debug:
        print(text)

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
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
    
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

ball = Pinball(launcher, (255, 255, 255), 7, [0, -30])
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
    # bumpers.append(Bumper([x, y],(150, 150, 150), 12))

flipper_left = Flipper((resolution[0] / 2 - 50, resolution[1] - 50), (230, 230, 30))
flipper_right = Flipper((resolution[0]/2 + 50, resolution[1] - 50), (230, 230, 30))
left_spin = 0
right_spin = 0

hitstop = 1
hitstop_limit = 0.017

debug = False
if debug:
    ball.speed[1] = -1
    ball.pos[0] = 380
    ball.pos[1] = 480
    hitstop_limit = 0.25


while running:  # Game Loop
    for event in pygame.event.get():
        if pygame.key.get_pressed()[K_ESCAPE]:
            escape = True
            running = False
        if pygame.mouse.get_pressed()[0]:
            LeftClick = True
        elif pygame.mouse.get_pressed()[1]:
            RightClick = True

    if LeftClick and not button_check:
        LeftClick = False
        button_check = True
        if debug:
          ball.speed[1] += 10

    if RightClick:
        RightClick = False
        button_check = True

    screen.fill([0, 0, 0])
    # screen.blit(cosmic, [0, 0])

    pygame.draw.rect(screen, [50, 50, 50], [resolution[0]/2 - size[0]/2, 0, size[0], size[1]], border)
    buff = ball.size + border

    if pygame.key.get_pressed()[K_SPACE]:
        flip_left = True
        flip_right = True

    if pygame.key.get_pressed()[K_LEFT]:
        flip_left = True

    flip_speed = 40
    limit = 25 * 3.14/180
    if flip_left:
        if left_spin > -limit:
            left_spin -= flip_speed * dt
        elif left_spin < -limit:
            left_spin = -limit
    else:
        if left_spin < limit:
            left_spin += flip_speed * dt
        elif left_spin > limit:
            left_spin = limit

    length = ball.size * 7
    flipx = flipper_left.pos[0] + length * math.cos(left_spin)
    flipy = flipper_left.pos[1] + length * math.sin(left_spin)

    pygame.draw.circle(screen, flipper_left.color, flipper_left.pos, 9)
    pygame.draw.line(screen, flipper_left.color, flipper_left.pos, (flipx, flipy), 6)
    top_angle = left_spin + 90 * 360 / 3.14
    offset = length / 8
    hit_left= [flipper_left.pos[0] + offset * math.cos(top_angle), flipper_left.pos[1] + offset * math.sin(top_angle)]
    bot_angle = left_spin - 90 * 360 / 3.14
    bot_left = [flipper_left.pos[0] + offset * math.cos(bot_angle), flipper_left.pos[1] + offset * math.sin(bot_angle)]
    pygame.draw.line(screen, flipper_left.color, (hit_left[0], hit_left[1]), (flipx, flipy), 6)
    pygame.draw.line(screen, flipper_left.color, (bot_left[0], bot_left[1]), (flipx, flipy), 6)

    # Right flipper
    if flip_right:
        if right_spin < limit:
            right_spin += flip_speed * dt
        elif right_spin > limit:
            right_spin = limit
    else:
        if right_spin > -limit:
            right_spin -= flip_speed * dt
        elif right_spin < -limit:
            right_spin = -limit

    right_flipx = flipper_right.pos[0] - length * math.cos(right_spin)
    right_flipy = flipper_right.pos[1] - length * math.sin(right_spin)

    pygame.draw.circle(screen, flipper_right.color, flipper_right.pos, 9)
    pygame.draw.line(screen, flipper_right.color, flipper_right.pos, (right_flipx, right_flipy), 6)
    angle = right_spin + 90 * 360 / 3.14
    offset = length / 8
    zoid = [flipper_right.pos[0] + offset * math.cos(angle), flipper_right.pos[1] + offset * math.sin(angle)]
    angle = right_spin - 90 * 360 / 3.14
    floyd = [flipper_right.pos[0] + offset * math.cos(angle), flipper_right.pos[1] + offset * math.sin(angle)]
    pygame.draw.line(screen, flipper_right.color, (zoid[0], zoid[1]), (right_flipx, right_flipy), 6)
    pygame.draw.line(screen, flipper_right.color, (floyd[0], floyd[1]), (right_flipx, right_flipy), 6)

    # Ball physics
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

    # Ball magnitude and direction
    magnitude = (ball.speed[0] ** 2 + ball.speed[1] ** 2) ** 0.5
    heading = math.atan(ball.speed[1] / (ball.speed[0] + .001))

    # Bumpers
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

    # Flippers
    # if ball.pos[1] > resolution[1]*0.7:
    #     for i in range(100):
    #         stretch = length * (i+1)/100
    #         point = [hit_left[0] + stretch * math.cos(left_spin), hit_left[1] + stretch * math.sin(left_spin)-5]
    #         distance = [point[0] - ball.pos[0], point[1] - ball.pos[1]]
    #         pythag = (abs(distance[0]) ** 2 + abs(distance[1]) ** 2) ** 0.5
    #         hitbox = ball.size + 8
    #         cushion = hitbox * 1.002
    #         if pythag <= hitbox and hitstop > hitstop_limit:
    #             hitstop = 0
    #             while pythag < cushion:
    #                 ball.pos[0] -= ball.speed[0] / 100
    #                 ball.pos[1] -= ball.speed[1] / 100
    #                 distance = [point[0] - ball.pos[0], point[1] - ball.pos[1]]
    #                 pythag = (abs(distance[0]) ** 2 + abs(distance[1]) ** 2) ** 0.5
    #             if flip_left and left_spin < limit:
    #                 ball.speed[1] = magnitude * stretch / 5 * math.sin(theta - left_spin) * elasticity
    #                 ball.speed[1] -= 20
    #             break

    ball.draw()
    draw_text(f"Score: {score}", font_mono20, (220, 230, 230), 20, 400)

    # Debug section
    if debug:
      # Framerate display
      rolling_frame = frame_counter % sample_size
      dt_array[rolling_frame] = dt
      dt_sum = np.sum(dt_array, dtype = np.float32)
      fps_counter = np.uint8(sample_size / dt_sum)
      draw_text(f"FPS: {fps_counter}", font_mono20, (200, 200, 200), resolution[0] - 100, resolution[1]-150)
        
    if event.type == pygame.KEYUP:
        if event.key == K_SPACE:
            flip_left = False
            flip_right = False
        if event.key == K_LEFT:
            flip_left = False
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
