import pygame, os, time
from pygame.locals import (KEYDOWN, QUIT, KEYUP, K_LCTRL, MOUSEWHEEL,
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, K_TAB, K_LSHIFT, K_SPACE, K_BACKSPACE,
    K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0, K_p,
                           K_q, K_w, K_e, K_r, K_t,
                           K_a, K_s, K_d, K_f, K_g, K_h, K_j, K_k,
                           K_z, K_x, K_c, K_v, K_b, K_m)

ip_address = f"192.168.0.235"
tv_ip = f"{ip_address}"
enter_mainframe = f"adb connect"

pygame.init()

resolution = [1000, 600]
screen = pygame.display.set_mode(resolution)

Images = {'remote': pygame.image.load('lib/remote.png'),
              'lock': pygame.image.load('lib/lock.png')}

def resize(self, height):
    sz = self.get_size()
    scl = height/sz[1]
    return pygame.transform.scale(self, (sz[0] * scl, sz[1] * scl))

img_remote = resize(Images['remote'], resolution[1])
img_lock = resize(Images['lock'], 80)

font_size = 21
font_mono = pygame.font.SysFont("ubuntumono", font_size, bold=False, italic=False)
font_atari = pygame.font.SysFont("atari800", 100, bold=False, italic=False)

setup_controls = ((K_SPACE, 'key_media_play_pause', "adb shell input keyevent 85"),
                  (K_BACKSPACE, 'key_back', "adb shell input keyevent 4"),
                  (K_r, "adb shell input keyevent 24", 'key_volume_up'),
                  (K_f, "adb shell input keyevent 25", 'key_volume_down'),
                  (K_h, "adb shell input keyevent 3", 'key_home'),
                  (K_e, "adb shell input keyevent 23", 'key_dpad_center'),
                  (K_2, "adb shell input keyevent 244", 'key_tv_input_hdmi_2'),
                  (K_k, "adb shell input keyevent 223", 'key_sleep'),
                  (K_j, "adb shell input keyevent 224", 'key_wakeup'),
                  (K_m, "adb shell input keyevent 164", 'key_volume_mute'),
                  (K_v, "adb shell input keyevent 87", 'key_media_next'),
                  (K_c, "adb shell input keyevent 88", 'key_media_previous'),
                  (K_UP, "adb shell input keyevent 19", 'up'),
                  (K_DOWN, "adb shell input keyevent 20", 'down'),
                  (K_LEFT, "adb shell input keyevent 21", 'left'),
                  (K_RIGHT, "adb shell input keyevent 22", 'right'),
                  (K_w, "adb shell input keyevent 19", 'up'),
                  (K_s, "adb shell input keyevent 20", 'down'),
                  (K_a, "adb shell input keyevent 21", 'left'),
                  (K_d, "adb shell input keyevent 22", 'right')
                  )

length = len(setup_controls)
controls = {}
for n in range(length):
    controls[setup_controls[n][0]] = setup_controls[n][1]

action = {}
for n in range(length):
    action[setup_controls[n][0]] = setup_controls[n][2]

running = True
clock = pygame.time.Clock()
framerate = 30
lock_controls = False
lock_switch = False
LeftClick = False
RightClick = False
tab_check = False
button_check = False
version = 'v0.1'
console_feedback = ['',]
console_feedback[0] = 'Welcome ~ PyFire Linux-TV Remote v0.1'

os.system(' '.join([enter_mainframe, tv_ip]))
os.system(f"echo Running PyFire {version}")
console_feedback.append(f"Connected to television {tv_ip}!")

def draw_text(text, font, text_col, x, y):  # function for outputting text onto the screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

class Button():  # Function for clickable buttons on screen
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False  # used for singles button clicks

    def draw(self):
        action = False
        # Mouse over event
        mousepos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousepos):  # Over button
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:  # Left click
                # self.clicked = True
                action = True

        # Draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

    def hover(self):
        action = False  # Mouse over event
        mousepos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousepos):  # Over button
            action = True

        return action

def remote_control(text): # Control the television
    os.system(controls[text])
    console_feedback.append(f"{action[text]} [{pygame.key.name(text)}]: {controls[text]}")

while running:  # Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_TAB and not tab_check:
                tab_check = True
                lock_controls = not lock_controls
            elif not lock_controls:
                try:
                    remote_control(event.key)
                except:
                    console_feedback.append(f"Key not recognized: {pygame.key.name(event.key)}")

        if pygame.mouse.get_pressed()[0] and not LeftClick:
            LeftClick = True

        if pygame.mouse.get_pressed()[2] and not RightClick:
            RightClick = True
            lock_switch = True


    screen.fill([0, 0, 0])
    screen.blit(img_remote, [resolution[0] - img_remote.get_width(), 0])
    if lock_controls:
        s = pygame.Surface(resolution)  # the size of your rect
        s.set_alpha(235)  # alpha level
        s.fill((0, 0, 0))  # this fills the entire surface
        screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates
        draw_text(f"Controls Locked", font_atari, (180, 180, 0), 125, 220)

    if Button(resolution[0]-138, resolution[1]-img_lock.get_height()/1.5,
              img_lock, 1).draw() and not button_check:
        button_check = True
        lock_switch = True

    if lock_switch:
        lock_switch = False
        lock_controls = not lock_controls

    length = len(console_feedback)
    for n in range(length):
        draw_text(f"{console_feedback[n]}", font_mono, (50, 235, 50),
                  10, resolution[1] - font_size *length*1.1 + font_size *n*1.1)

    if event.type == pygame.KEYUP:
        if event.key == K_TAB:
            tab_check = False

    if event.type == pygame.MOUSEBUTTONUP:
        button_check = False
        if event.button == 1:
            LeftClick = False
        if event.button == 3:
            RightClick = False

    pygame.display.update()
    clock.tick(framerate)  # Sets frames/sec

pygame.quit()
