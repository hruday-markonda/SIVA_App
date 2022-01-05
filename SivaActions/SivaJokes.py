import random
import json
from SivaActions.SivaPopulator import Populate
import os

def JokeTeller():
    THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    my_file = THIS_FOLDER +'/SIVAintents.json'
    with open(my_file) as ListOfResponses:
        SpeechDictionary = json.load(ListOfResponses)
        for ProbableOutputs in SpeechDictionary['SivaSpeechDictionary']:
            if ProbableOutputs['ProbableInput'] == "Joke":
                Joke = "Here's a joke!: " + random.choice(ProbableOutputs['PotentialOutputs'])
                return Populate(str(Joke), "SIVATEXT", "non", "non","non")

if __name__ == '__main__':
    JokeTeller()