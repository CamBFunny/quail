import subprocess
import time

# Create and start the processes
programs = ["animations/bloody yin yang.py", "animations/solar system.py", "animations/dvd.py"]

process = [0,] * len(programs)
for n in range(len(programs)):
    process[n] = subprocess.Popen(['python3', programs[n]])

time.sleep(1)
spacer = f"~~~~~"
for k in range(7):
    print(spacer)

from scripts.python.pyspeech import *

say(f"Thank you for visiting Cameron's quail repository.")
say(f"I hope you enjoy my somewhat useless programs.")

# Wait for the processes to finish
for m in range(len(programs)):
    process[m].wait()

# opening file_1.py and reading it with read() and executing if with exec()
# path =
# with open(path) as file:
#     exec(file.read())
