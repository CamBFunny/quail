import pygame, os, time
from pygame.locals import (KEYDOWN, QUIT, KEYUP, K_LCTRL, MOUSEWHEEL,
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, K_TAB, K_LSHIFT, K_SPACE, K_BACKSPACE,
    K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0, K_p,
                           K_q, K_w, K_e, K_r, K_t,
                           K_a, K_s, K_d, K_f, K_g, K_h, K_j, K_k,
                           K_z, K_x, K_c, K_v, K_b, K_m)

tv_ip = f"192.168.0.235"
enter_mainframe = f"adb connect"

pygame.init()

font_size = 21
font_mono = pygame.font.SysFont("ubuntumono", font_size, bold=False, italic=False)

controls = {
        "key_unknown": "adb shell input keyevent 0",
        "key_soft_left": "adb shell input keyevent 1",
        "key_soft_right": "adb shell input keyevent 2",
        K_h: "adb shell input keyevent 3", # key_home
        K_BACKSPACE: "adb shell input keyevent 4", # key_back
        K_UP: "adb shell input keyevent 19",
        K_DOWN: "adb shell input keyevent 20",
        K_LEFT: "adb shell input keyevent 21",
        K_RIGHT: "adb shell input keyevent 22",
        K_e: "adb shell input keyevent 23", # key_dpad_center
        K_r: "adb shell input keyevent 24", # key_volume_up
        K_f: "adb shell input keyevent 25", # key_volume_down
        "key_menu": "adb shell input keyevent 82",
        K_SPACE: "adb shell input keyevent 85",   # key_media_play_pause
        K_d: "adb shell input keyevent 87", # key_media_next
        K_a: "adb shell input keyevent 88", # key_media_previous
        "key_media_rewind": "adb shell input keyevent 89",
        "key_media_fast_forward": "adb shell input keyevent 90",
        K_m: "adb shell input keyevent 164", # key_volume_mute
        K_c: "adb shell input keyevent 175", # key_captions
        "key_settings": "adb shell input keyevent 176",
        "key_tv_input": "adb shell input keyevent 178",
        K_k: "adb shell input keyevent 223", # key_sleep
        K_j: "adb shell input keyevent 224", # key_wakeup
        "key_tv_input_hdmi_1": "adb shell input keyevent 243",
        K_2: "adb shell input keyevent 244", # key_tv_input_hdmi_2
        "key_tv_input_hdmi_3": "adb shell input keyevent 245",
        "key_tv_input_hdmi_4": "adb shell input keyevent 246",
        "key_media_skip_forward": "adb shell input keyevent 272",
        "key_media_skip_backward": "adb shell input keyevent 273",
        "key_media_step_forward": "adb shell input keyevent 274",
        "key_media_step_backward": "adb shell input keyevent 275",
    }

action = dict(controls)
action[K_SPACE] = 'key_media_play_pause'
action[K_BACKSPACE] = 'key_back'
action[K_r] = 'key_volume_up'
action[K_f] = 'key_volume_down'
action[K_h] = 'key_home'
action[K_e] = 'key_dpad_center'
action[K_2] = 'key_tv_input_hdmi_2'
action[K_k] = 'key_sleep'
action[K_j] = 'key_wakeup'
action[K_m] = 'key_volume_mute'
action[K_d] = 'key_media_next'
action[K_a] = 'key_media_previous'
action[K_c] = 'key_captions'

running = True
trigger = False
clock = pygame.time.Clock()
framerate = 20
console_feedback = ['',]
console_feedback[0] = 'Welcome ~ Linux-TV Remote v0.1'

os.system(' '.join([enter_mainframe, tv_ip]))
os.system('clear')
console_feedback.append(f"Connected to television {tv_ip}!")

length = len(action)
for n in range(length):
    try:
        os.system(f"echo {list(action.values())[n]}-{pygame.key.name(list(action)[n])}")
    except:
        os.system(f"echo {list(action.values())[n]}-{list(action)[n]}")

resolution = [800, 600]
screen = pygame.display.set_mode(resolution)

def draw_text(text, font, text_col, x, y):  # function for outputting text onto the screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def remote_control(text): # Control the television
    os.system(controls[text])
    console_feedback.append(f"{action[text]} [{pygame.key.name(text)}]: {controls[text]}")

while running:  # Game Loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            try:
                remote_control(event.key)
                trigger = True
            except:
                console_feedback.append(f"Key not recognized: {pygame.key.name(event.key)}")

        if pygame.mouse.get_pressed()[0]:
            LeftClick = True
        elif pygame.mouse.get_pressed()[1]:
            RightClick = True

    screen.fill([0, 0, 0])
    # screen.blit(background, [0, 0])

    length = len(console_feedback)
    for n in range(length):
        draw_text(f"{console_feedback[n]}", font_mono, (50, 235, 50),
                  10, resolution[1] - font_size *length*1.1 + font_size *n*1.1)

    pygame.display.update()
    clock.tick(framerate)  # Sets frames/sec

    if trigger:
        time.sleep(0.2)
        trigger = False

pygame.quit()
