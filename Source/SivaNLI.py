import speech_recognition as sr
import os, SivaBrain
from SivaActions import SivaPopulator

def SIVAResponse(audio):
    #The audio variable is passed as an argument into this function so that SIVA can 'speak'
    response = audio + "\n"

    #A couple of if statements are passed to deal with exceptions. This includes things like replacing SIVA/siva with
    #seeva instead so that the correct pronounciation could be said and replace the °C with degrees celsius in order to
    #ensure it says degrees celcius rather than 'C'.
    if 'siva' in audio:
        audio = audio.replace("siva", " seeva")

    elif 'SIVA' in audio:
        audio = audio.replace("SIVA", " seeva")

    elif '°C' in audio:
        audio = audio.replace("°C", " degrees celsius")

    # This piece of code is made to ensure that when the text is being said using bash it wont read included parentheses
    # or other special characters as bash commands which can prevent bash from saying the string out
    BadCharacters = "([\`*_{}[]()>#+-$])|/"
    for character in audio:
        for BadChar in BadCharacters:
            audio = audio.replace(BadChar, "")

    #It says the audio by splitting the string into seperate lines and then saying each line
    for line in audio.splitlines():
        os.system("say " + audio)


def SivaSTTS():
    #Listens for any recognisable words and sets that into a variable called command
    r = sr.Recognizer()
    command = ""
    #This detects and sets the default microphone as the 'source' to listen from
    with sr.Microphone() as source:
        #Pause threshold is if there is no recognisable words for 0.5s then it stops listening and writing to the
        #command variable and it moves on with the code
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        #Once the pause threshold has been achieved whatever has been recognised will be populated into the command
        #variable and then populated as the usertext so that it can be displayed on the interface
        command = r.recognize_google(audio)
        UserCommand = command.capitalize() + "." + '\n'
        SivaPopulator.Populate(str(UserCommand), "USERTEXT", "non", "non","non")
        SivaBrain.SivaStringProcessor(command)

    except sr.UnknownValueError:
        #If nothing has been recognised it just populates the usertext as 'non' which is the keyword I use for an empty
        #key and then processes as normal
        SivaPopulator.Populate("non", "USERTEXT", "non", "non","non")
        SivaBrain.SivaStringProcessor(command)

if __name__ == '__main__':
    SIVAResponse("My name is SIVA")
