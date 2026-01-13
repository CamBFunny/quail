import playsound
import pyttsx3
engine = pyttsx3.init()
import sys
version = f"{sys.version}"

def say(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# RATE
rate = 190
engine.setProperty('rate', rate)

# VOLUME
engine.setProperty('volume', 1)

say(f"Hello, Cameron! I am Python {version[:6]}!")
say('My current speaking rate is ' + str(rate))
engine.stop()

# Saving Voice to a file
# On Linux, make sure that 'espeak-ng' is installed
engine.save_to_file('This file was saved', 'test.mp3')
engine.runAndWait()
playsound.playsound('test.mp3')