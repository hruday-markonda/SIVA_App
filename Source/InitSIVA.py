import json,os,sys,threading,webview,SivaNLI
from flask import Flask, Response, render_template, jsonify
from SivaActions.SivaGreetings import Greetings
#-----------------------------------------------------------------------------------------------------------------------
#These are variables which are needed in order for a onefile executable to work properly. sys._MEIPASS refers to a
#cached directory which is created by the application when opened which temporarily houses data files such as JSON and
#text files and also script files such as my python scripts which are easier to access through relative paths.

#Comment this block out and uncomment next block if you wish to debug the application

template_folder = os.path.join(sys._MEIPASS, 'templates')
static_folder = os.path.join(sys._MEIPASS, 'static')
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
my_file = os.path.join(sys._MEIPASS, 'PyJsVarDump.json')
#-----------------------------------------------------------------------------------------------------------------------

'''
#-----------------------------------------------------------------------------------------------------------------------
app = Flask(__name__)
THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
my_file = THIS_FOLDER + '/SivaActions/PyJsVarDump.json'
#-----------------------------------------------------------------------------------------------------------------------
'''

#-----------------------------------------------------------------------------------------------------------------------
#This is what is run when the user clicks the microphone button. It is prompted by the AJAX front end to run through the
#function url or route /startAI/, then once it is done processing it 'POST's the processed JSON back so front end can be
#updated
@app.route('/startAI/',methods=['POST'])
def StartAIbutton():
    SivaNLI.SivaSTTS()
    with open(my_file) as Json:
        JSON = json.load(Json)
    print(JSON)
    return jsonify(JSON)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
#This is the function which is run when the program is opened. Similar to the StartAI function, it runs then edits the
#JSON API and then 'POST's it back as a JSON HTTP Protocol.
@app.route('/Greetings/',methods=['POST'])
def StartUpGreeting():
    Greetings()
    print(my_file)
    with open(my_file) as Json:
        JSON = json.load(Json)
    print(JSON)
    return jsonify(JSON)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
#This function is prompted by a tiny get request using AJAX after the major part which is the processed JSON API is
#recieved by the front end. This returns a HTTP Protocol with status 200 to indicate to the front end AJAX that the
#action has been successfully performed.
@app.route('/SaySpeech/')
def SaySpeech():
    with open(my_file) as Json:
        JSON = json.load(Json)
    SivaNLI.SIVAResponse(str(JSON["SIVATEXT"]))
    return Response(status=200)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
#This resets the JSON API. It does it by opening the JSON file then setting all the JSON Key values to 'non' which acts
#as an indicator for an empty JSON
@app.route('/resetJSON/')
def resetJson():
    with open(my_file, 'r') as Json:
        JSONAPI = json.load(Json)
    JSONAPI["WEBLINK"] = JSONAPI["SIVATEXT"] = JSONAPI["USERTEXT"] = JSONAPI["WEATHERIMAGE"] = JSONAPI["TEMP"] = JSONAPI["APPSTAT"] = "non"
    with open(my_file, 'w') as Json:
        json.dump(JSONAPI, Json)
    return Response(status=200)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
@app.route('/closeApp/')
def closeApp():
    #JSON API file is reset upon exiting to ensure it is fresh for next session.
    resetJson()
    #os._exit(0) ensures all processes relating SIVA are quit such as closing the localserver with host name SIVAhost
    #rather than just the interface closing. This ensures there is no background processes going on after quitting which
    #would count as a violation of privacy as the app is still technically running.
    os._exit(0)
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
@app.route('/')
def renderGUI():
    return render_template('/sivaGUI.html', name="SIVA")
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
def start_server():
    #Host is set to localhost rather than the standard IP address 127.0.0.1 because some videos when using the music
    #will not play because the video is trying to be hosted on an IP address and not a host link
    app.run(host='localhost')
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
#This if statement is an exclusive feature of python. Basically what it does is if the current script is designed as the
#'entering' or primary script then a specific set of instructions are performed as opposed to just running whatever code
#has been written. In this case the entry script when opening the program is this script so it opens the interface up
#with a set height and other conditions and parameters such as connecting to the localhost server.
if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    webview.create_window("SIVA","http://localhost:5000/", resizable=False, height=670, width=340)
    webview.start(debug=False)
    sys.exit()
#-----------------------------------------------------------------------------------------------------------------------