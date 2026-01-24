import subprocess, time, random, os

# Create and start the processes
path = '/home/cameron/PycharmProjects/quail/'
programs = ["animations/bloody yin yang.py", "animations/solar system.py", "animations/dvd.py"]

process = [0,] * len(programs)
for n in range(len(programs)):
    process[n] = subprocess.Popen(['python3', f"{path}{programs[n]}"])

time.sleep(1)

path = '/home/cameron/PycharmProjects/quail/ascii_art'
files = os.listdir(path)
counter = 0
for l in range(len(files)):
    if files[l - counter] == 'README.md':
        files.remove(files[l - counter])
        counter += 1
choice = random.choice(range(len(files)))
with open(f"{path}/{files[choice]}", 'r') as f:
    content = f.read()
    print(content)

from scripts.python.TTS.pyquote import *

say(f"Thank you for visiting Cameron's quail repository.")
say(f"I hope you enjoy my somewhat useless programs.")

# Wait for the processes to finish
for m in range(len(programs)):
    process[m].wait()

# opening file_1.py and reading it with read() and executing if with exec()
# path =
# with open(path) as file:
#     exec(file.read())
