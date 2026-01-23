from gtts import gTTS
import playsound

import sys
version = f"{sys.version}"

def main(blurb):
  print(blurb)
  tts = gTTS(blurb)
  tts.save('tmp/Gtext.mp3')
  playsound.playsound('tmp/Gtext.mp3')

main(f"Your motherboard was a thermal paste guzzling microprocessor that couldn't calculate simple addition")

import playsound
import pyttsx3
engine = pyttsx3.init()
import sys
version = f"{sys.version}"

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