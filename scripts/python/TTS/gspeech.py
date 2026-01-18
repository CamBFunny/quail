from gtts import gTTS
import playsound

def main(blurb):
  print(blurb)
  tts = gTTS(blurb)
  tts.save('Gtext.mp3')
  playsound.playsound('Gtext.mp3')

# if __name__ == "__main__":
#   main(f"Hello, world! Python is awesome! You are using Python version {version[:6]}")

main(input('Say something: '))