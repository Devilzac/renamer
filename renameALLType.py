import os
import shutil
from datetime import datetime

# Product_datasheet_Revision_Language_multilingual
now = datetime.now() # current date and time

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

folderPath = r'C:\Users\Kavan.Rodriguez\Desktop\RenameScripts\toDo'
allSamefile = bool(True)
allLanguagesAvailable = ["CA_", "DE_", "DU_",
                         "EN_", "ES_", "FR_", "IT_", "NO_", "PT_", "SV_","DA_","PL_","EU_"]

product = 'Supernova_'
multilingual = bool(True)
revision = ''
dataMulti = ''
 
dataType = {
    "DS": bool(False),
    "IG": bool(True),
    "UG": bool(False),
    "Manual": bool(False),
    "GuiaActivation": bool(False)
}
multi = {
    "CA_": "_multilingüe",
    "DE_": "_mehrsprachig",
    "DU_": "_meertalig",
    "EN_": "_multilingual",
    "ES_": "_multilingüe",
    "FR_": "_multilingue",
    "IT_": "_multilingue",
    "NO_": "_flerspråklig",
    "PT_": "_multilingue",
    "SV_": "_flerspråkig",
    "DA_": "_flersproget",
    "PL_": "_wielojęzyczny",
    "EU_": "_eleanitza"
}


if bool(dataType["DS"]):
    data = {
        "CA_": "Fitxa_tecnica", 
        "DE_": "Datenblatter",
        "DU_": "Gegevensbladen",
        "EN_": "Datasheet",
        "ES_": "Fichas_tecnicas",
        "FR_": "Fiches_techniques",
        "IT_": "Schede_tecniche",
        "NO_": "Dataark",
        "PT_": "Fichas_tecnicas",
        "SV_": "Datablad",
        "CS_": "Technicky_datovy_list",
        "DA_": "Datablad",
        "NL_": "Technisch_gegevensblad",
        "EL_": "Φύλλο_τεχνικών_δεδομένων",
        "ET_": "Tehniline_andmeleht",
        "FI_": "Tekninen_esite",
        "HE_": "גיליון_נתונים_טכניים",
        "HU_": "Muszaki_adatlap",
        "IS_": "Taeknilegt_gagnablad",
        "LV_": "Tehnisko_datu_lapa",
        "PL_": "Arkusz_danych_technicznych",
        "RO_": "Fisa_tehnica",
        "RU_": "Лист_технических_данных",
        "SI_": "Tehnični_podatkovni_list",
        "UK_": "Технічна_інформація",
        "SL_": "Tehnicni_podatkovni_list"
        
    }

if bool(dataType["IG"]):
    data = {"CA_": "Guies_d’instal·lació",
            "DE_": "Installationsanleitungen",
            "DU_": "Installatiegidsen",
            "NL_": "Installatiegidsen",
            "EN_": "Installation_Guide",
            "ES_": "Guías_de_instalación",
            "FR_": "Guides_d’installation",
            "IT_": "Guide_all’installazione",
            "NO_": "Installasjonsveiledninger",
            "PT_": "Guias_de_instalação",
            "SV_": "Installationsanvisningar",
            "DA_": "Installationsvejledninger",
            "PL_": "Instrukcje_instalacji",
            "EU_": "Instalatzeko_gida"
            }

if bool(dataType["UG"]):
    data = {"CA_": "Guies_d’usuari",
            "DE_": "Benutzerhandbücher",
            "DU_": "Gebruikershandleidingen",
            "EN_": "User_Guides",
            "ES_": "Guías_del_usuario",
            "FR_": "Guides_d’utilisation",
            "IT_": "Guide_dell’utente",
            "NO_": "Brukerhåndbøker",
            "PT_": "Manuais_do_utilizador",
            "SV_": "Användarhandböcker",
            "CS_": "Uživatelská_příručka",
            "DA_": "Brugervejledning",
            "EL_": "Οδηγίες_χρήσης",
            "ET_": "Kasutusjuhend",
            "FL_": "Käyttöopas",
            "HE_": "מדרי_למשתמש",
            "HU_": "Használati_útmutató",
            "IS_": "Notendaleiðbeiningar",
            "LV_": "Lietotāja_ceļvedis",
            "PL_": "Podręcznik_użytkownika",
            "RO_": "Ghidul_utilizatorului",
            "SK_": "Návod_na_používanie",
            "SW_": "Användarhandböcker",
            "UK_": "Посібник користувача"
            }


if bool(dataType["Manual"]):
    data = {"CA_": "Manual",
            "DE_": "Handbuch",
            "DU_": "handleiding",
            "EN_": "Manual",
            "ES_": "Manual",
            "FR_": "Manuel",
            "IT_": "Manuale",
            "NO_": "Håndbok",
            "PT_": "Manual",
            "SV_": "Manuell",
            "DA_": "Manuel"
            }

if bool(dataType["GuiaActivation"]):
    data = {"CA_": "GUIA_D'ACTIVACIÓ",
            "DE_": "AKTIVIERUNGSANLEITUNG",
            "DU_": "ACTIVERINGSGIDS",
            "EN_": "ACTIVATION_GUIDE",
            "ES_": "GUÍA_DE_ACTIVACIÓN",
            "FR_": "GUIDE_D’ACTIVATION",
            "IT_": "GUIDA_ALL'ATTIVAZIONE",
            "NO_": "AKTIVERINGSVEILEDNING",
            "PT_": "GUIA_DE_ATIVAÇÃO",
            "SV_": "AKTIVERINGSGUIDE"
            }



if allSamefile == False:
    if bool(dataType["GuiaActivation"]) == False:
        for filename in os.listdir(folderPath):
            if filename[0:3] == "CA_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'CA_' +
                            product + data["CA_"] + "_" + multi["CA_"] + revision + 'Catala.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'CA_' +
                            product + data["CA_"] + "_" + revision + 'Catala.pdf')

            if filename[0:3] == "DE_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'DE_' +
                            product + data["DE_"] + "_" + multi["DE_"] + revision + 'Deutsch.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'DE_' +
                            product + data["DE_"] + "_" + revision + 'Deutsch.pdf')

            if filename[0:3] == "DU_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'DU_' +
                            product + data["DU_"] + "_" + multi["DU_"] + revision + 'Nederlands.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'DU_' +
                            product + data["DU_"] + "_" + revision + 'Nederlands.pdf')

            if filename[0:3] == "EN_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'EN_' +
                            product + data["EN_"] + "_" + multi["EN_"] + revision + 'English.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'EN_' +
                            product + data["EN_"] + "_" + revision + 'English.pdf')

            if filename[0:3] == "ES_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'ES_' +
                            product + data["ES_"] + "_" + multi["ES_"] + revision + 'Espanol.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'ES_' +
                            product + data["ES_"] + "_" + revision + 'Espanol.pdf')

            if filename[0:3] == "FR_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'FR_' +
                            product + data["FR_"] + "_" + multi["FR_"] + revision + 'Francais.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'FR_' +
                            product + data["FR_"] + "_" + revision + 'Francais.pdf')

            if filename[0:3] == "IT_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'IT_' +
                            product + data["IT_"] + "_" + multi["IT_"] + revision + 'Italiano.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'IT_' +
                            product + data["IT_"] + "_" + revision + 'Italiano.pdf')

            if filename[0:3] == "NO_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'NO_' +
                            product + data["NO_"] + "_" + multi["NO_"] + revision + 'Norsk_bokmal.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'NO_' +
                            product + data["NO_"] + "_" + revision + 'Norsk_bokmal.pdf')

            if filename[0:3] == "PT_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'PT_' +
                            product + data["PT_"] + "_" + multi["PT_"] + revision + 'Portugues.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'PT_' +
                            product + data["PT_"] + "_" + revision + 'Portugues.pdf')

            if filename[0:3] == "SV_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'SV_' +
                            product + data["SV_"] + "_" + multi["SV_"] + revision + 'Svenska.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'SV_' +
                            product + data["SV_"] + "_" + revision + 'Svenska.pdf')
                            

            if filename[0:3] == "CS_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'CS_' +
                            product + data["CS_"] + "_" + multi["CS_"] + revision + 'Czech.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'CS_' +
                            product + data["CS_"] + "_" + revision + 'Czech.pdf')
                            

            if filename[0:3] == "DA_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'DA_' +
                            product + data["DA_"] + "_" + multi["DA_"] + revision + 'Danish.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'DA_' +
                            product + data["DA_"] + "_" + revision + 'Danish.pdf')
      
            if filename[0:3] == "NL_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'NL_' +
                            product + data["NL_"] + "_" + multi["NL_"] + revision + 'Dutch.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'NL_' +
                            product + data["NL_"] + "_" + revision + 'Dutch.pdf')
                                             

            if filename[0:3] == "EL_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'EL_' +
                            product + data["EL_"] + "_" + multi["EL_"] + revision + 'Ελληνικά.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'EL_' +
                            product + data["EL_"] + "_" + revision + 'Ελληνικά.pdf')
                            

            if filename[0:3] == "ET_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'ET_' +
                            product + data["ET_"] + "_" + multi["ET_"] + revision + 'Eestlane.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'ET_' +
                            product + data["ET_"] + "_" + revision + 'Eestlane.pdf')
           
            if filename[0:3] == "FI_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'FI_' +
                            product + data["FI_"] + "_" + multi["FI_"] + revision + 'Suomen_kieli.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'FI_' +
                            product + data["FI_"] + "_" + revision + 'Suomen_kieli.pdf')
                                     

            if filename[0:3] == "FL":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'FL' +
                           product +  data["FL"] + "_" + multi["FL"] + revision + '.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'FL' +
                           product +  data["FL"] + "_" + revision + '.pdf')
                            

            if filename[0:3] == "HE_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'HE_' +
                            product + data["HE_"] + "_" + multi["HE_"] + revision + 'עִברִית.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'HE_' +
                            product + data["HE_"] + "_" + revision + 'עִברִית.pdf')
                            

            if filename[0:3] == "HU_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'HU_' +
                            product + data["HU_"] + "_" + multi["HU_"] + revision + 'Magyar.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'HU_' +
                            product + data["HU_"] + "_" + revision + 'Magyar.pdf')
                            

            if filename[0:3] == "IS_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'IS_' +
                            product + data["IS_"] + "_" + multi["IS_"] + revision + 'Islenska.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'IS_' +
                            product + data["IS_"] + "_" + revision + 'Islenska.pdf')
                            

            if filename[0:3] == "LV_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'LV_' +
                            product + data["LV_"] + "_" + multi["LV_"] + revision + 'Latvietis.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'LV_' +
                            product + data["LV_"] + "_" + revision + 'Latvietis.pdf')

            if filename[0:3] == "PL_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'PL_' +
                            product + data["PL_"] + "_" + multi["PL_"] + revision + 'Polski.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'PL_' +
                            product + data["PL_"] + "_" + revision + 'Polski.pdf')

            if filename[0:3] == "RO_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'RO_' +
                            product + data["RO_"] + "_" + multi["RO_"] + revision + 'Romania.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'RO_' +
                            product + data["RO_"] + "_" + revision + 'Romania.pdf')


            if filename[0:3] == "RU_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'RU_' +
                            product + data["RU_"] + "_" + multi["RU_"] + revision + 'Русский.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'RU_' +
                            product + data["RU_"] + "_" + revision + 'Русский.pdf')

            if filename[0:3] == "SK_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'SK_' +
                            product + data["SK_"] + "_" + multi["SK_"] + revision + '.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'SK_' +
                            product + data["SK_"] + "_" + revision + '.pdf')

            if filename[0:3] == "SI_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'SI_' +
                            product + data["SI_"] + "_" + multi["SI_"] + revision + '.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'SI_' +
                            product + data["SI_"] + "_" + revision + '.pdf')

            if filename[0:3] == "SL_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'SL_' +
                            product + data["SL_"] + "_" + multi["SL_"] + revision + 'Slovenscina.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'SL_' +
                            product + data["SL_"] + "_" + revision + 'Slovenscina.pdf')

            if filename[0:3] == "SW_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'SW_' +
                            product + data["SW_"] + "_" + multi["SW_"] + revision + 'Svenska.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'SW_' +
                            product + data["SW_"] + "_" + revision + 'Svenska.pdf')

            if filename[0:3] == "UK_":
                if bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'UK_' +
                            product + data["UK_"] + "_" + multi["UK_"] + revision + 'Український.pdf')
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'UK_' +
                            product + data["UK_"] + "_" + revision + 'Український.pdf')


if allSamefile == True:
    for filename in os.listdir(folderPath):
        for item in allLanguagesAvailable:    
            if bool(multilingual):
                shutil.copy(folderPath + '\\' + filename, folderPath +
                        '\\' + item + product +"_"+ data[item] +"_"+ revision + multi[item] +  '.pdf')
            if not bool(multilingual):
                shutil.copy(folderPath + '\\' + filename, folderPath + '\\' + item +"_"+ data[item] + product + revision + '.pdf')
    



if allSamefile == False:
    if bool(dataType["GuiaActivation"]) == True:
        for filename in os.listdir(folderPath):
            if filename[0:3] == "CA_":
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'CA_' + data["CA_"] + "_" +product + '.pdf')
            if filename[0:3] == "DE_":
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'DE_' + data["DE_"] + "_" +product + '.pdf')
            if filename[0:3] == "DU_":
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'DU_' + data["DU_"] + "_" +product + '.pdf')
            if filename[0:3] == "EN_":
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'EN_' + data["EN_"] + "_" +product + '.pdf')
            if filename[0:3] == "ES_":
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'ES_' + data["ES_"] + "_" +product + '.pdf')
            if filename[0:3] == "FR_":
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'FR_' + data["FR_"] + "_" +product + '.pdf')
            if filename[0:3] == "IT_":
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'IT_' + data["IT_"] + "_" +product + '.pdf')
            if filename[0:3] == "NO_":
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'NO_' + data["NO_"] + "_" +product + '.pdf')
            if filename[0:3] == "PT_":
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'PT_' + data["PT_"] + "_" +product + '.pdf')
            if filename[0:3] == "SV_":
                if not bool(multilingual):
                    os.rename(folderPath + '\\' + filename, folderPath + '\\' + 'SV_' + data["SV_"] + "_" +product + '.pdf')