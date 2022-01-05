import urllib.request, os, json, sys, re, requests
from bs4 import BeautifulSoup
from SivaActions.SivaPopulator import Populate

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
CurrentHTMLSession = requests.Session()
CurrentHTMLSession.headers['User-Agent'] = USER_AGENT
CurrentHTMLSession.headers['Accept-Language'] = LANGUAGE
CurrentHTMLSession.headers['Content-Language'] = LANGUAGE

THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
my_file = THIS_FOLDER + '/SIVAintents.json'

#Adapted from https://www.codeproject.com/articles/873060/python-search-youtube-for-video and
#https://stackoverflow.com/questions/62726516/empty-list-most-of-the-time-outputted-when-trying-to-find-first-link-when-gettin

def MusicPlayer(MusicRequest):
    #-------------------------------------------------------------------------------------------------------------------
    #The query is converted into a youtube search query which can be seen when you search something on youtube and then
    #if you check the url all the spaces between the words in your query are replaced with a plus and then searched
    MusicSearchLink = MusicRequest.replace(" ","+")
    MusicSearchLink = "https://www.youtube.com/results?search_query=" + MusicSearchLink
    #-------------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------------------------------------------
    #This part 'opens' the processed url for python to view the contents of the HTML
    HTMLContent = urllib.request.urlopen(MusicSearchLink)
    #-------------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------------------------------------------
    #SearchResults is an array which is populated by finding all instances of the youtube video ID which is lead by a
    #prefix of watch?v= and then a combination of 11 characters as denoted by .{11}
    SearchResults = re.findall(r'/watch\?v=(.{11})', HTMLContent.read().decode())
    #-------------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------------------------------------------
    #Once all the youtube search video ID's are found, an embedded version of the link is created using the first ID
    #found in the SearchResults array as the first ID would be the best matching youtube video to play
    besturl = str("http://www.youtube.com/embed/" + SearchResults[0] + "?autoplay=1&showinfo=0&controls=0")
    #-------------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------------------------------------------
    #This piece of code simply gets the title of the video from the title tag of the HTML of the video link
    youtubeurl = CurrentHTMLSession.get(str("https://www.youtube.com/watch?v=" + SearchResults[0]))
    soup = BeautifulSoup(youtubeurl.text, "html.parser")
    Title = soup.find("title").text
    Title = Title.replace("- YouTube","")
    #-------------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------------------------------------------
    #The link and a response from SIVA stating what you have searched is then populated into JSON to then send to front
    #end.
    Populate(besturl, "WEBLINK", "non", "non", "non")
    SivaMessage = "Now playing: " + Title
    return Populate(str(SivaMessage), "SIVATEXT", "non", "non", "non")
    #-------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    MusicPlayer("Thomas the Tank Engine theme")