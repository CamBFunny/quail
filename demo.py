import subprocess
import time

# Create and start the processes
proc1 = subprocess.Popen(['python3', "animations/bloody yin yang.py"])
proc2 = subprocess.Popen(['python3', "animations/solar system.py"])
proc3 = subprocess.Popen(['python3', "animations/dvd.py"])

time.sleep(1)
from scripts.python.pyspeech import *

say(f"Thank you for visiting Cameron's quail repository.")
say(f"I hope you enjoy my somewhat useless programs.")

# Wait for the processes to finish
proc1.wait()
proc2.wait()
proc3.wait()

# opening file_1.py and reading it with read() and executing if with exec()
# path =
# with open(path) as file:
#     exec(file.read())
