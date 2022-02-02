import os,json,sys

THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__)))
my_file = THIS_FOLDER + '/PyJsVarDump.json'

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