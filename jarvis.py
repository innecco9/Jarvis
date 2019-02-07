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
    try:
        command = r.recognize_google(audio)
        print("you said" + command + '/n' )

    #Loop back to continue to listen for commands

    except sr.UnknownValueError:
        assistant(myCommand())

    return command

#If statements for executing commands
    def assistant(command):

        if 'open reddit python' in command:
            chrome_path = '/usr/bin/google-chrome'
            url = 'https://www.reddit.com/r/python'
            webbrowser.get(chrome_path).open(url)

        if 'what\'s up' in command:
            talkToMe('Chillin like a villain')

        if 'email' in command:
            talkToMe('Who is the recipient')
            recipient = myCommand()

            if 'john' in recipient:
                talkToMe('what should I say')
                content = myCommand()

                #init Gmail smtp
                mail = smtplib.SMTP('smtp.gmail.com', 587)

                #indentify to server
                mail.ehlo()

                #encrypt session
                mail.starttls()

                #login
                mail.login('username', 'password')

                #sending our email
                mail.sendmail('PERSON NAME', 'emailaddress@whatever.com', content)

                #close connection
                mail.close()

                talkToMe('Email sent')

    talkToMe('I am ready for your command')
    while True:
        assistant(myCommand())
