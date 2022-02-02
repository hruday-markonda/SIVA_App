SIVA is a voice based assistant project started in 2019 however only recently uploaded to GitHub for public contribution.
The hopes for this project right now is to significantly improve the back end processing of voice inputs and windows support.

Run following command while inside the Source directory to create mac executable:

`pyinstaller -w -F --hidden-import=pkg_resources.py2_warn --add-data "templates:templates" --add-data "static:static" --add-data "SIVAintents.json:." --add-data "SivaActions/PyJsVarDump.json:." --add-data "EnglishStopWords.txt:." --name SIVA --icon icon.icns InitSIVA.py`
