import random, json, time, os, sys
from .SivaPopulator import Populate

my_file = os.path.join(sys._MEIPASS, 'SIVAintents.json')
with open(str(my_file)) as ListOfResponses:
    SpeechDictionary = json.load(ListOfResponses)

#This function run upon opening the app and it gets a greeting. If the greeting has a TimeOfDay indicator
#inside then it replaces it with morning, afternoon, or evening based on the hour of the day
def Greetings():
    for ProbableOutputs in SpeechDictionary['SivaSpeechDictionary']:
        if ProbableOutputs['ProbableInput'] == "Hello":
            HelloMessage = random.choice(ProbableOutputs['PotentialOutputs'])
            if "_TimeOfDay_" not in HelloMessage:
                return Populate(str(HelloMessage), "SIVATEXT", "non", "non","non")
            else:
                day_time = int(time.strftime("%-H", time.localtime()))
                if 0 <= day_time < 12:
                    HelloMessage = HelloMessage.replace("_TimeOfDay_",'morning. How are you?')
                    return Populate(str(HelloMessage), "SIVATEXT", "non", "non","non")
                elif 12 <= day_time < 18:
                    HelloMessage = HelloMessage.replace("_TimeOfDay_",'afternoon. How are you?')
                    return Populate(str(HelloMessage), "SIVATEXT", "non", "non","non")
                elif day_time >= 18:
                    HelloMessage = HelloMessage.replace("_TimeOfDay_",'evening. How are you?')
                    return Populate(str(HelloMessage), "SIVATEXT", "non", "non","non")

if __name__ == '__main__':
    Greetings()