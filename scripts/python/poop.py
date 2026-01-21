import time, os

line = ['|', '\\', '-', '/']
m = 0
clear = lambda: os.system('cls')
running = 1
load = ' loading...'
length = len(load)
stuff = list(load)
message = ''
one = True
two = True
three = True
four = True
wait = False
dt = 0
t_prime = 0
accumulator = 0

while running:
    t = time.localtime(time.time())
    local_time = time.asctime(t)
    a = line[m%4]
    index = 1 + m%length
    b = ''.join(stuff[:(index)])
    timer = time.perf_counter()
    dt = timer - t_prime
    t_prime = timer
    string = str(timer) + '00'
    thousandths = int(''.join(string[5:7]))
    if 0 <= thousandths < 24 and one:
        clear()
        print(f"{a} {b}")
        one = False
        two = True
        m += 1
    elif 24 <= thousandths < 48 and two:
        clear()
        print(f"{a} {b}")
        two = False
        three = True
        m += 1
    elif 48 <= thousandths < 76 and three:
        clear()
        print(f"{a} {b}")
        three = False
        four = True
        m += 1
    elif 76 <= thousandths < 100 and four:
        clear()
        print(f"{a} {b}")
        four = False
        one = True
        m += 1
    if m%20 == 3 and m>4:
        wait = True
        one = False
        two = False
        three = False
        four = False
        clear()
        message += 'poop '
        print(message)
        holder = thousandths
        m = 0
    elif wait:
        accumulator += dt
        if accumulator >= 1.8:
            one = True
            wait = False
            accumulator = 0
