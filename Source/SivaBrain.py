import json,os,sys
from SivaActions import SivaJokes, SivaDefinitions, SivaGoogleSearch, SivaGreetings, SivaMusic, SivaWeather, SivaDateTime
from SivaActions.SivaResponses import Responses

#QueryFunctions and NonQueryFunctions are variable lists which list possible function requests which the user might ask
#which require some type of search request which in that case would be a query and ones which dont require a search
#request which would be a nonquery.

QueryFunctions = ["google","search","music","define","definition","meaning","mean","play","youtube","song","music","song"]
NonQueryFunctions = ["weather","joke","feeling","date","day","today","time","outside","temperature","sad","unhappy","laugh"]
my_file = os.path.join(sys._MEIPASS, 'SIVAintents.json')

#-----------------------------------------------------------------------------------------------------------------------
#This small piece of code simply opens the json file for use. This is seen frequently in many of my modules
with open(str(my_file)) as ListOfResponses:
    SpeechDictionary = json.load(ListOfResponses)

#-----------------------------------------------------------------------------------------------------------------------
#This function uses the EnglishStopWords text file in order to filter out non-essential words within the given
#input so that only the uncommon words or the desired elements of the phrase are left which is usually the intent and
#the entity.
def SivaStringProcessor(user_command):
    #-------------------------------------------------------------------------------------------------------------------
    EngFile = os.path.join(sys._MEIPASS, 'EnglishStopWords.txt')
    EnglishStopWords = open(str(EngFile), "r")
    ListOfStopWords = [line.strip() for line in EnglishStopWords]
    user_command = user_command.replace("'", "")
    user_command = user_command.lower()
    user_command = user_command.split()
    #-------------------------------------------------------------------------------------------------------------------
    FilteredCommand = user_command[:]
    for word in user_command:
        for stopword in ListOfStopWords:
            if word == stopword:
                FilteredCommand.remove(word)
    print(FilteredCommand)
    FunctionDeterminer(FilteredCommand)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
#This section deals with the final command which now has no stopwords.
def FunctionDeterminer(ProcessedCommand):
    #-------------------------------------------------------------------------------------------------------------------
    if ProcessedCommand == []:
        for ProbableOutputs in SpeechDictionary['SivaSpeechDictionary']:
            Responses("Error","non")
    #-------------------------------------------------------------------------------------------------------------------
    else:
        # for KeyWords in ProcessedCommand:
        for index, command in enumerate(ProcessedCommand):
            if len(ProcessedCommand) == 1 and command in QueryFunctions:
                return Responses("Search-NoQuery", "non")

            else:
                if command in QueryFunctions:
                    Function = command
                    Query = ""
                    # ------------------------------------------------------------------------------------------------------
                    if command != "mean" or "songs" and command in QueryFunctions:
                        commandIndex = ProcessedCommand.index(command) + 1
                        while commandIndex < len(ProcessedCommand):
                            Query = Query + " " + ProcessedCommand[commandIndex]
                            commandIndex = commandIndex + 1
                        return QueryFunctionIdentifier(Function, Query)
                    # --------------------------------------------------------------------------------------------------
                    elif command == "mean" or command == "songs":
                        commandIndex = ProcessedCommand.index(command) - 1
                        while commandIndex > -1:
                            Query = Query + " " + ProcessedCommand[commandIndex]
                            commandIndex = commandIndex - 1
                        return QueryFunctionIdentifier(Function, Query)
                # -------------------------------------------------------------------------------------------------------
                elif command in NonQueryFunctions:
                    Function = command
                    return NonQueryFunctionIdentifier(Function)
                # -------------------------------------------------------------------------------------------------------
                elif command in ["goodbye", "go", "leave", "bye", "later"]:
                    return Responses("Bye", "Exit")
                # -------------------------------------------------------------------------------------------------------
                elif command in ["good", "well", "fine", "great", "fantastic"]:
                    return Responses("GoodResponse", "non")
                # -------------------------------------------------------------------------------------------------------
                elif command in ["thank", "thanks"]:
                    return Responses("YourWelcome", "non")
                # ------------------------------------------------------------------------------------------------------
                elif command in "name":
                    return Responses("Name", "non")
                # ------------------------------------------------------------------------------------------------------
                elif command in ["greeting", "greetings", "hello", "see", "hi"]:
                    return SivaGreetings.Greetings()
                # ------------------------------------------------------------------------------------------------------
                elif command in ["help","do"]:
                    return Responses("Help", "non")
                # ------------------------------------------------------------------------------------------------------
                elif command in ["feeling", "how", "hows"]:
                    return Responses("Feeling", "non")
                # ------------------------------------------------------------------------------------------------------
                elif index == len(ProcessedCommand) - 1:
                    return Responses("Error", "non")

#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
def QueryFunctionIdentifier(GivenRequest, QueryValue):
    if GivenRequest in ["google", "search"]:
        SivaGoogleSearch.GoogleSearch(QueryValue)
    #-------------------------------------------------------------------------------------------------------------------
    elif GivenRequest in ["play", "music", "song"]:
        SivaMusic.MusicPlayer(QueryValue)
    #-------------------------------------------------------------------------------------------------------------------
    elif GivenRequest in ["define", "meaning", "mean", "definition"]:
        SivaDefinitions.Definer(QueryValue)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
def NonQueryFunctionIdentifier(GivenRequest):
    if GivenRequest in ["weather", "outside", "temperature"]:
        SivaWeather.Weather()
    #-------------------------------------------------------------------------------------------------------------------
    elif GivenRequest in ["greeting", "greetings", "hello"]:
        SivaGreetings.Greetings()
    #-------------------------------------------------------------------------------------------------------------------
    elif GivenRequest in ["joke", "sad", "unhappy", "laugh"]:
        SivaJokes.JokeTeller()
    #-------------------------------------------------------------------------------------------------------------------
    elif GivenRequest in ["date", "day", "today"]:
        SivaDateTime.Date()
    #-------------------------------------------------------------------------------------------------------------------
    elif GivenRequest in "time":
        SivaDateTime.Time()
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    SivaStringProcessor("Im good")