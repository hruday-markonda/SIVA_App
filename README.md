# SIVA - Virtual Assistant
### What is Siva?
SIVA is a voice based assistant project started in 2019 by me, Hruday Markonda.
The hopes for this project right now is to significantly improve the back end processing of voice inputs and add windows support.

### Developer Tools:
#### Calibration:
- Execute the bash script `devscript.sh` with `dependent` argument to install all required python dependencies, add to this list any new libraries being used.
- Execute the bash script `devscript.sh` with `compile` argument while in same folder as the file to generate executable which can be found in `/Source/dist/`.
- Execute the bash script `devscript.sh` with `clear` argument to remove all compilation files and directories including the application.
- Execute the bash script `devscript.sh` with `neat` argument to remove all compilation files and directories leaving only the application which is inside `/Source/dist/` folder.

#### Running Debug Mode:

After changing all paths from one file executable to relative paths, open `InitSIVA.py`, console log should pop up with interface debugging options by right clicking on interface and then going to inspect element. 

#### Files which contain debugger/onefile exec path variations:
- `SivaActions/SivaDateTime.py`
- `SivaActions/SivaGreetings.py`
- `SivaActions/SivaResponses.py`
- `SivaActions/SivaPopulator.py`
- `InitSIVA.py`
- `SivaBrain.py`

#### Usage
When pressing button to speak please wait around 1 second before speaking to ensure the program fully calibrates to your room’s ambience otherwise it won’t successfully pick up your audio. 