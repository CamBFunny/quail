import os

path = '/home/cameron/PycharmProjects/quail/ascii_art'
files = os.listdir(path)
counter = 0
for l in range(len(files)):
    if files[l - counter] == 'README.md':
        files.remove(files[l - counter])
        counter += 1
print(files)
