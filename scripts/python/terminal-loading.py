import time, os

line = ['|', '\\', '-', '/']
m = 0
clear = lambda: os.system('cls')
running = 1
load = 'loading...'
length = len(load)
stuff = list(load)

while running:
    a = line[m%4]
    b = ''.join(stuff[:(m%length)])
    clear()
    print(f"{a} {b}")
    buffer = 0.245
    if m%4 == 2:
        time.sleep(1-(3*buffer))
    else:
        time.sleep(buffer)
    if m%20 == 3 and m>4:
        clear()
        print('poop')
        m = -1
        time.sleep(2)
    m += 1
