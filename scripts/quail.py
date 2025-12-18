import time

t = time.localtime(time.time())
localtime = time.asctime(t)
str = f"Current Time: {localtime}\n"
file_path = 'quail.txt'
with open(file_path, 'w') as file:  # w - write over file
    file.write(str)

max = int(input('Number: '))
while max > 20:
    max = int(max/10)
print(f"Pyramids: {max}")

for j in range(max):
    num = j + 2
    size = num*2 - 1
    for i in range(size-1):
        if i < num:
            string = ['//Python'] * (i+1) + ['//\n']
        elif num <= i < size-1:
            string = ['//Python'] * (num*2 - i - 1) + ['//\n']
        string = ''.join(string)
        with open(file_path, 'a') as file:  # a - add new line
            file.write(string)

string = '//Python//'
with open(file_path, 'a') as file:  # a - add new line
    file.write(string)

from ascii_quail import *

with open(file_path, 'a') as file:  # a - add new line
    file.write(ascql)

with open(file_path, 'r') as file:
    content = file.read() # Reads the entire file content into a single string
    print(content)