import json, os, inflect, sys
from datetime import datetime
from . import SivaPopulator

my_file = os.path.join(sys._MEIPASS, 'SIVAintents.json')
with open(my_file) as ListOfResponses:
    SpeechDictionary = json.load(ListOfResponses)

#The date function uses a module called inflect in order to convert the raw date given by the system into months i.e.
#raw month would be like 1 and inflect would convert that to january.
def Date():
    p = inflect.engine()
    for ProbableOutputs in SpeechDictionary['SivaSpeechDictionary']:
        if ProbableOutputs['ProbableInput'] == "Date":
            Current = datetime.now()
            DateResponse = ProbableOutputs['PotentialOutputs']
            Year = Current.strftime("%Y")
            Weekday = Current.strftime("%A")
            Month = Current.strftime("%B")
            DayOfMonth = Current.strftime("%d").capitalize()
            FinalDate = str(Weekday + ", " + "the " + p.ordinal(DayOfMonth) + " of " + Month + ". The year is " + Year)
            DateResponse = DateResponse.replace("__DAY__", FinalDate)
            return SivaPopulator.Populate(str(DateResponse), "SIVATEXT", "non", "non","non")

#The time function gets the raw time and then converts it into 24 hour based time
def Time():
    for ProbableOutputs in SpeechDictionary['SivaSpeechDictionary']:
        if ProbableOutputs['ProbableInput'] == "Time":
            Current = datetime.now()
            DisplayMessage = ProbableOutputs['PotentialOutputs']
            Time = str(Current.strftime("%I:%M%p"))
            DisplayMessage = DisplayMessage.replace("__CLOCK__", Time) + "."
            return SivaPopulator.Populate(str(DisplayMessage), "SIVATEXT", "non", "non","non")


if __name__ == '__main__':
    Date()
    Time()
