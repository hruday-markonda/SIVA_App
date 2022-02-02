from bs4 import BeautifulSoup as BeautifulSoup
from .SivaPopulator import Populate
from .SivaWeather import USER_AGENT, CurrentHTMLSession, LANGUAGE

#This function opens dictionary.com with the query and then gets its definition. If the definition doesnt exist
#then it populates an error message to display on front end
def Definer(WordToDefine):
    GoogleDefinitionHTML = CurrentHTMLSession.get("https://www.dictionary.com/browse/"+WordToDefine)
    soup = BeautifulSoup(GoogleDefinitionHTML.text, "html.parser")
    definition = soup.find("div", attrs={"class": "css-kg6o37 e1q3nk1v3", "value":"1"})
    if definition is not None:
        definition = definition.text
        return Populate(str(definition), "SIVATEXT", "non", "non","non")
    else:
        return Populate("The word you have asked for the meaning does not have a dictionary definition.", "SIVATEXT", "non", "non","non")

if __name__ == '__main__':
    Definer("Australian")