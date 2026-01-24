import playsound
import pyttsx3
engine = pyttsx3.init()
import sys
version = f"{sys.version}"

from quote import quote
import random

def say(text):
    # RATE
    rate = 170
    engine.setProperty('rate', rate)
    # VOLUME
    engine.setProperty('volume', 0.8)
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

say(f"Hello, world! I am Python {version[:6]}.")

key_terms = ['life', 'death', 'humanity', 'age', 'wisdom', 'family', 'technology', 'love', 'time',
             'music', 'patience', 'purpose', 'meaning', 'ascii_art']
term = random.choice(key_terms)
saying = quote(term)
selection = saying[random.choice(range(len(saying)))]
while selection['author'] == "J.K. Rowling" or len(selection['quote']) > 200:
    term = random.choice(key_terms)
    saying = quote(random.choice(key_terms))
    selection = saying[random.choice(range(len(saying)))]

say(f"\"{selection['quote']}\" -{selection['author']}")

# # Saving Voice to a file
# engine.save_to_file('', 'test.mp3')
# engine.runAndWait()
# playsound.playsound('test.mp3')