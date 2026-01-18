import playsound
import pyttsx3
engine = pyttsx3.init()
import sys
version = f"{sys.version}"

from quote import quote
import random

def say(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# RATE
rate = 182
engine.setProperty('rate', rate)

# VOLUME
engine.setProperty('volume', 1)

say(f"Hello, world! I am Python {version[:6]}.")

key_terms = ['life', 'death', 'humanity', 'age', 'wisdom', 'family', 'technology', 'love', 'time']
saying = quote(random.choice(key_terms))
selection = saying[random.choice(range(len(saying)))]
say(f"\"{selection['quote']}\" -{selection['author']}")

# # Saving Voice to a file
# engine.save_to_file('', 'test.mp3')
# engine.runAndWait()
# playsound.playsound('test.mp3')