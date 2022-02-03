import os,json,sys

#One file executable json path
my_file = os.path.join(sys._MEIPASS, 'PyJsVarDump.json')

'''
#Debugging json path
THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname( __file__ )))
my_file = THIS_FOLDER + '/PyJsVarDump.json'
'''

#This populates the PyJsVarDump.json file by passing the name of the key to populate and the data it should go
def Populate(data, key, WEATHERIMAGE, TEMP, appstat):
    with open(my_file, 'r') as VarDump:
        JSONAPI = json.load(VarDump)
    JSONAPI[str(key)] = data
    if TEMP is not "non":
        JSONAPI["WEATHERIMAGE"] = WEATHERIMAGE
        JSONAPI["TEMP"] = TEMP
    elif appstat is not "non":
        JSONAPI["APPSTAT"] = appstat
    with open(my_file, 'w') as VarDump:
        json.dump(JSONAPI, VarDump)

if __name__ == '__main__':
    Populate("non","SIVATEXT","non","non","non")