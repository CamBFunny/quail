import time, os
line = ['|', '\\', '-', '/']
m = 0
clear = lambda: os.system('clear')
running = 1
load = ' loading...'
length = len(load)
stuff = list(load)
message = ''
one = True
two = True
three = True
four = True
dt = 0
t_prime = 0

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
    load_bar = f"{a}{b}\n\n"
    for p in range(len(string)):
        if string[p] == '.':
            deci = p + 1
    thousandths = int(''.join(string[deci:deci + 2]))
    if 0 <= thousandths < 24 and one:
        clear()
        print(load_bar)
        one = False
        two = True
        m += 1
    elif 24 <= thousandths < 48 and two:
        clear()
        print(load_bar)
        two = False
        three = True
        m += 1
    elif 48 <= thousandths < 76 and three:
        clear()
        print(load_bar)
        three = False
        four = True
        m += 1
    elif 76 <= thousandths < 100 and four:
        clear()
        print(load_bar)
        four = False
        one = True
        m += 1
    else:
        time.sleep(0.05)