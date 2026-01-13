from gtts import gTTS
import playsound

def main():
  tts = gTTS("Hello, world! Python is awesome!")
  tts.save('hello.mp3')

if __name__ == "__main__":
  main()

playsound.playsound('hello.mp3')