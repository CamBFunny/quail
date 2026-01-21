import time, os

line = ['|', '\\', '-', '/']
m = 0
clear = lambda: os.system('cls')
running = 1
load = 'loading...'
length = len(load)
stuff = list(load)
message = ''

while running:
    a = line[m%4]
    index = 1 + m%length
    b = ''.join(stuff[:(index)])
    clear()
    print(f"{a} {b}")
    buffer = 0.245
    if m%4 == 2:
        time.sleep(1-(3*buffer))
    else:
        time.sleep(buffer)
    if m%20 == 3 and m>4:
        clear()
        message += 'poop '
        print(message)
        m = -1
        time.sleep(2)
    m += 1
