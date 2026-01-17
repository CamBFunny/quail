from gtts import gTTS
import playsound

import sys
version = f"{sys.version}"

def main():
  tts = gTTS(f"Hello, world! Python is awesome! You are using Python version {version[:6]}")
  tts.save('hello.mp3')

if __name__ == "__main__":
  main()

playsound.playsound('hello.mp3')