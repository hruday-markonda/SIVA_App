#!/bin/bash

if [ $1 = dependent ]
then
    pip3 install pyinstaller
    pip3 install SpeechRecognition
    pip3 install beautifulsoup4
    pip3 install inflect
    pip3 install pywebview
    pip3 install PyAudio
    pip3 install Flask
    pip3 install urllib3
    pip3 install setuptools
    pip3 install Werkzeug

elif [ $1 = compile ]
then
    cd ./Source
    pyinstaller -w -F --hidden-import=pkg_resources.py2_warn --add-data "templates:templates" --add-data "static:static" --add-data "SIVAintents.json:." --add-data "SivaActions/PyJsVarDump.json:." --add-data "EnglishStopWords.txt:." --name SIVA --icon icon.icns InitSIVA.py

else
echo 'Invalid Argument'
fi