import time, random
import pygame
import subprocess
import sys, os
# Import buttons
from pygame.locals import (KEYDOWN, QUIT, KEYUP, K_LCTRL,
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, K_TAB, K_LSHIFT, K_SPACE,
    K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0,
                           K_q, K_w, K_e, K_r, K_t,
                           K_a, K_s, K_d, K_f, K_g,
                           K_z, K_x, K_c, K_v, K_b, K_i)

# Load colors
Colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "yellow": (255, 255, 0),
    "orange": (255, 150, 0),
    "pink": (255, 0, 150),
    "purple": (150, 0, 255),
    "cyan": (0, 255, 255),
    "teal": (0, 150, 255),
    "lime": (150, 255, 0),
    "seafoam": (0, 255, 150),
    "magenta": (255, 0, 255),
    "gold": (255, 215, 0),
    "black": (0, 0, 0),
    "silver": (240, 240, 240),
    "grey": (150, 150, 150),
}

title = "Dope Empire"
pygame.init()  # Initialize PyGame
# Screen settings
res = [int(1280), int(800)] # resolution
mobile_res = [int(540), int(960)]
screen = pygame.display.set_mode(res)
screen_center = (res[0] / 2, res[1] / 2)

keys_pressed = set()
clock = pygame.time.Clock()

# pygame.mouse.set_visible(False)     # Hide mouse cursor
mouse_pos = pygame.mouse.get_pos()

Fonts = {}
font_sizes = range(10, 70, 1)
font_names = ['mono', 'helv', 'ubuntu']
font_id = {'mono': 'Mono', 'helv': 'Helvetica', 'ubuntu': 'ubuntumono'}
# Fonts
for i in font_sizes:
    for n in font_id:
        Fonts[f"{n}{i}b"] = pygame.font.SysFont(font_id[n], i, bold=True)
        Fonts[f"{n}{i}"] = pygame.font.SysFont(font_id[n], i, bold=False)

# // FUNCTIONS //
def draw_text(text, font, text_col, x, y):  # Function for outputting text onto the screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def gauge(value, x, y, width, color):
    rectangle = pygame.Rect(x, y, value, width)
    pygame.draw.rect(screen, color, rectangle)

# initialize variables
running = True
framerate = 30
true_timer = 0.0
pause = False
frame_counter = 0
game_state = "startup"
LeftHold = False
RightHold = False
MiddleClick = False
price = {}

while running:
    # CONTROLS
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Reading Keyboard Input
        if event.type == KEYDOWN:
            keys_pressed.add(event.key)
        if event.type == pygame.QUIT or K_ESCAPE in keys_pressed:
            running = False
            # Reading Mouse Input
        if event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                wheel_up = True
            if event.y == -1:
                wheel_down = True
        if pygame.mouse.get_pressed()[0] and not LeftHold:  # Left Click
            LeftClick = True
            LeftHold = True
            HoldStart = true_timer
        if pygame.mouse.get_pressed()[2] and not RightHold:  # Right Click
            RightClick = True
            RightHold = True
        if pygame.mouse.get_pressed()[1] and not MiddleClick:  # Middle Click
            MiddleClick = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                LeftClick = False
                LeftHold = False
                HoldTime = (true_timer - HoldStart) / framerate
                buttoncheck = False
            if event.button == 2:
                MiddleClick = False
            if event.button == 3:
                RightClick = False
                RightHold = False
        if event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed.remove(event.key)

    screen.fill((5, 5, 10))

    if game_state == "simulating":
        draw_text('Release key to END simulation.', Fonts['ubuntu20'], Colors['green'], 0, 1)
        sim_message = f"Simulating dope prices.{'.'*int((true_timer - t_0)*2)}"
        draw_text(sim_message, Fonts['ubuntu20'], Colors['green'], 0, 50)
        price['weed'] = random.choice(range(50, 200))
        time.sleep(0.05)
        if len(keys_pressed) == 0:
            game_state = "ready"
        message = False

    if game_state == "startup":
        draw_text('Welcome to the Dope Game!', Fonts['ubuntu20'], Colors['green'], 0, 1)
        if true_timer >= 2:
            draw_text('Hold any button to create simulation.', Fonts['ubuntu20'], Colors['green'], 0, 50)
        if len(keys_pressed) > 0:
            t_0 = true_timer
            game_state = "simulating"

    if game_state == "ready":
        draw_text('Name your empire:', Fonts['ubuntu20'], Colors['green'], 0, 1)
        if len(keys_pressed) > 0:
            game_state = "main"

    # Main gameplay loop
    if game_state == "main":
        draw_text('[B]uy, [S]ell', Fonts['ubuntu20'], Colors['green'], 0, 1)
        if K_b in keys_pressed:
            game_state = "buy"
        if K_s in keys_pressed:
            game_state = "sell"
        if K_i in keys_pressed:
            game_state = "invest"

    if game_state == "buy":
        message = f"Which product are you buying?"
        draw_text(message, Fonts['ubuntu20'], Colors['green'], 0, 1)

    pygame.display.update()
    dt = clock.tick(framerate) / 1000  # Makes movement or time-related events work independent of framerate
    true_timer += dt  # Total time game has been unpaused
    frame_counter += 1  # Total number of rendered frames

    # ~~~~~ End of game loop ~~~~~
pygame.quit()

print('// fin //')