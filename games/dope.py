import msvcrt as m
import time, random
def wait():
    m.getch()

def cook():
    cook_cycles = 0
    price = {}
    while True:
        if m.kbhit():
            m.getch()
            return price
            break
        price['weed'] = random.choice(range(50, 200))
        time.sleep(0.03)
        cook_cycles += 1

K_b = 98

print('Welcome to the Dope Game!')
print('Press any key to BEGIN randomizing.')
wait()
print('Press any key to END randomizing.')
price = cook()
running = True
message = True
while running:
    if message:
        print(f"Weed: ${price['weed']}")
        print('[B]uy, [S]ell')
        message = False
    if m.kbhit():
        choice = m.getch()
        choice = list(choice)[0]
        print(choice)
        if choice == K_b:
            game_state = "buy"
            running = False
print('// fin //')