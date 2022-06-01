import os
import shutil
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

folderPath = r'C:\Users\shane\Desktop\RenameScripts\toDo'
allSamefile = bool(False)
allLanguagesAvailable = ["EN_US_", "ES_MX_", "FR_CA_"]

product = 'Onyx'
multilingual = bool(False)
revision = ''
dataMulti = ''

dataType = {
    "DS": bool(True),
    "IG": bool(False),
    "UG": bool(False),
    "Manual": bool(False),
    "GuiaActivation": bool(False)
}
multi = {
    "FR_CA_": "_multilingue",
    "EN_US_": "_multilingual",
    "ES_MX_": "_multilingüe"
}


if bool(dataType["DS"]):
    data = {
        "FR_CA_": "Fiche technique",
        "EN_US_": "Technical_Datasheet",
        "ES_MX_": "Hoja_técnica"
        
    }

if allSamefile == False:
    if bool(dataType["GuiaActivation"]) == False:
        for filename in os.listdir(folderPath):
            if filename[0:3] == "FR_CA_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'FR_CA_' +
                            data["FR_CA_"] + "_" + product + multi["FR_CA_"] + revision + '.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'FR_CA_' +
                            data["FR_CA_"] + "_" + product + revision + '.pdf')

            if filename[0:3] == "EN_US_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'EN_US_' +
                            data["EN_US_"] + "_" + product + multi["EN_US_"] + revision + '.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'EN_US_' +
                            data["EN_US_"] + "_" + product + revision + '.pdf')

            if filename[0:3] == "ES_MX_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'ES_MX_' +
                            data["ES_MX_"] + "_" + product + multi["ES_MX_"] + revision + '.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'ES_MX_' +
                            data["ES_MX_"] + "_" + product + revision + '.pdf')
