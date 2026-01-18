from gtts import gTTS
import playsound

import sys
version = f"{sys.version}"

def main(blurb):
  print(blurb)
  tts = gTTS(blurb)
  tts.save('Gtext.mp3')
  playsound.playsound('Gtext.mp3')

main(f"Your motherboard was a thermal paste guzzling microprocessor that couldn't calculate simple addition")

import playsound
import pyttsx3
engine = pyttsx3.init()
import sys
version = f"{sys.version}"

from quote import quote
import random

def say(text):
    # RATE
    rate = 130
    engine.setProperty('rate', rate)
    # VOLUME
    engine.setProperty('volume', 1)
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

say(f"No u.")

# # Saving Voice to a file
# engine.save_to_file('', 'test.mp3')
# engine.runAndWait()
# playsound.playsound('test.mp3')