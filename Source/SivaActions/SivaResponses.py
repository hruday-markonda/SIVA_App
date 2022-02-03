import os, sys, json, random
from .SivaPopulator import Populate

#One file executable json path
my_file = os.path.join(sys._MEIPASS, 'SIVAintents.json')

'''
#Debugging json path
THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
my_file = THIS_FOLDER + '/SIVAintents.json'
'''

with open(str(my_file)) as ListOfResponses:
    SpeechDictionary = json.load(ListOfResponses)

#-----------------------------------------------------------------------------------------------------------------------
#This script and definition was created as a way to simplify placing SIVA's static responses based on the possible
#responses my intents.json file.
def Responses(ResponseType, APPSTAT):
    #-------------------------------------------------------------------------------------------------------------------
    for ProbableOutputs in SpeechDictionary['SivaSpeechDictionary']:
        if ProbableOutputs['ProbableInput'] == str(ResponseType):
            SivaResponse = random.choice(ProbableOutputs['PotentialOutputs'])
            return Populate(str(SivaResponse),"SIVATEXT","non","non",APPSTAT)

if __name__ == "__main__":
    Responses("Hello","non")