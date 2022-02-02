import speech_recognition as sr
import os
import SivaBrain
from SivaActions import SivaPopulator
import platform

def SIVAResponse(audio):
    #speaks audio passed as argument
    response = audio + "\n"

    if 'siva' in audio:
        audio = audio.replace("siva", " seeva")

    elif 'SIVA' in audio:
        audio = audio.replace("SIVA", " seeva")

    elif '°C' in audio:
        audio = audio.replace("°C", " degrees celsius")

    #This piece of code is made to ensure that when the text is being said using bash it wont read included parentheses
    #or other special characters as bash commands which can prevent bash from saying the string out
    BadCharacters = "([\`*_{}[]()>#+-$])|/"
    for character in audio:
        for BadChar in BadCharacters:
            audio = audio.replace(BadChar,"")

    for line in audio.splitlines():
        os.system("say " + audio)


def SivaSTTS():
    #Listens for command
    print("Listening: ")
    r = sr.Recognizer()
    command = ""
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        UserCommand = command.capitalize() + "." + '\n'
        SivaPopulator.Populate(str(UserCommand), "USERTEXT", "non", "non","non")
        SivaBrain.SivaStringProcessor(command)

    except sr.UnknownValueError:
        SivaPopulator.Populate("non", "USERTEXT", "non", "non","non")
        SivaBrain.SivaStringProcessor(command)

if __name__ == '__main__':
    SIVAResponse("Now playing: Dragon Ball Super: Opening 2 - Limit Break X Survivor | English Dub (Adult Swim)")