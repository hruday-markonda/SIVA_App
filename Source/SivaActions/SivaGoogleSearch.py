from .SivaPopulator import Populate

#This adds the query to a google search prefix to generate the google link
def GoogleSearch(SearchRequest):
    SearchQuery = "https://www.google.com/search?igu=1&ei=&q=" + SearchRequest.strip()
    DisplayMessage = "Showing results for " + SearchRequest + "."
    Populate(str(SearchQuery), "WEBLINK", "non", "non","non")
    return Populate(str(DisplayMessage),"SIVATEXT", "non", "non","non")

if __name__ == '__main__':
    GoogleSearch("Dogs")