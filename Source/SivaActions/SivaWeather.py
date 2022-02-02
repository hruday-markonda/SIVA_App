from bs4 import BeautifulSoup as BeautifulSoup
import requests
from .SivaPopulator import Populate

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
CurrentHTMLSession = requests.Session()
CurrentHTMLSession.headers['User-Agent'] = USER_AGENT
CurrentHTMLSession.headers['Accept-Language'] = LANGUAGE
CurrentHTMLSession.headers['Content-Language'] = LANGUAGE

#Basically what this function does is it opens google weather link, searches for the wob_tm and wob_dc ids in the html
#which hold information for temperature and weather description respectively.
def Weather():
    GoogleWeatherHTMLLink = CurrentHTMLSession.get("https://www.google.com/search?q=Weather")
    soup = BeautifulSoup(GoogleWeatherHTMLLink.text, "html.parser")
    temp = soup.find("span", attrs={"id": "wob_tm"}).text + "°C"
    weather = soup.find("span", attrs={"id": "wob_dc"}).text
    output = "The current temperature is " + temp + " and it is " + weather.lower() + " outside."
    return Populate(str(output),"SIVATEXT",str(weather), str(temp),"non")

if __name__ == '__main__':
    Weather()
