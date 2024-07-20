""" Python 3.12.4 """

import subprocess
import os
import sys
import ctypes

#google drive public file downloader
import gdown

DUCK_GAME = "steam://rungameid/1568590"
SETTING_URL = "https://drive.google.com/uc?export=download&id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH"

def downloadSettings():
    output = 'temp_settings.reg'
    gdown.download(SETTING_URL, output, quiet=False)

def importSettings():
    try:
        subprocess.run(['regedit', '/s', 'temp_settings.reg'], check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(e)

def startGame():
    subprocess.run(['start', DUCK_GAME], shell=True)

def isAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def runAsAdmin():
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:])
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    except:
        print("Не удалось запустить скрипт с правами администратора.")

if not isAdmin():
    runAsAdmin()
else:
    downloadSettings()
    importSettings()
    startGame()
