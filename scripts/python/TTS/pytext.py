import playsound
import pyttsx3
engine = pyttsx3.init()
import sys
version = f"{sys.version}"

def say(text):
    # RATE
    rate = 170
    engine.setProperty('rate', rate)
    # VOLUME
    engine.setProperty('volume', 1)
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# say(input('Say something: '))

# # Saving Voice to a file
# engine.save_to_file('', 'tmp/test.mp3')
# engine.runAndWait()
# playsound.playsound('tmp/test.mp3')