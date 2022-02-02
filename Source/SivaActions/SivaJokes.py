import random, json, os, sys
from .SivaPopulator import Populate

#This just gets a joke and adds the prefix to the joke
def JokeTeller():
    my_file = os.path.join(sys._MEIPASS, 'SIVAintents.json')
    with open(my_file) as ListOfResponses:
        SpeechDictionary = json.load(ListOfResponses)
        for ProbableOutputs in SpeechDictionary['SivaSpeechDictionary']:
            if ProbableOutputs['ProbableInput'] == "Joke":
                Joke = "Here's a joke!: " + random.choice(ProbableOutputs['PotentialOutputs'])
                return Populate(str(Joke), "SIVATEXT", "non", "non","non")

if __name__ == '__main__':
    JokeTeller()