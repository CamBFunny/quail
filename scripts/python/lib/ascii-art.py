import os

path = '/ascii_art'
files = os.listdir(path)
counter = 0
for l in range(len(files)):
    if files[l - counter] == 'README.md':
        files.remove(files[l - counter])
        counter += 1
    else:
        try:
            with open(f"{path}/{files[l-counter]}", 'r') as f:
                content = f.read()
                print(content)
                print('###############')
                print(files[l-counter])
                print('###############')
        except:
            print(f"\n!!! {files[l-counter]} !!!\n")