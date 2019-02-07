from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
  print(audio)
  tts = gTTS(text=audio, lang='en')
  tts.save('audio.mp3')
  os.system('mpg123 audio.mp3')
#listen for commands

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshhold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
