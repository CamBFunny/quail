import playsound
import pyttsx3
engine = pyttsx3.init()
import sys
version = f"{sys.version}"
import pycurl #curl library
import certifi #HTTP over TLS/SSL library
from io import BytesIO #Buffered I/O implementation using an in-memory bytes buffer.
from quote import quote
import random

def say(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# RATE
rate = 180
engine.setProperty('rate', rate)

# VOLUME
engine.setProperty('volume', 1)

say(f"Hello, world! I am Python {version[:6]}.")

header = ['Accept: application/json']

buffer = BytesIO()
c = pycurl.Curl() #curl
c.setopt(c.HTTPHEADER, header) #header
c.setopt(c.URL, 'https://ipinfo.io/json') #URL
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where()) # SSL certificates
c.perform()
c.close()
body = buffer.getvalue()
location = body.decode('iso-8859-1')

say(f"Greetings from {location[93:104]}, {location[120:127]}.")

key_terms = ['life', 'death', 'humanity', 'age', 'wisdom', 'family', 'technology', 'love']
saying = quote(random.choice(key_terms))
selection = saying[random.choice(range(len(saying)))]
say(f"\"{selection['quote']}\" -{selection['author']}")

# # Saving Voice to a file
# engine.save_to_file('', 'test.mp3')
# engine.runAndWait()
# playsound.playsound('test.mp3')