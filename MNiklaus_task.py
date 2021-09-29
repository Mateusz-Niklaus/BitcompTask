from xml.dom import minidom
import json

quitVar = True

def parcel_aaa():
    DOMTree = minidom.parse(userInput)
    cNodes = DOMTree.childNodes
    for i in cNodes[0].getElementsByTagName("Flurstueck"):
        print ("Numer działki: " + i.getElementsByTagName("flstkennz")[0].childNodes[0].toxml())
        print ("Wielkość działki: " + i.getElementsByTagName("flaeche")[0].childNodes[0].toxml())
        print ("Numer landu: " + i.getElementsByTagName("landschl")[0].childNodes[0].toxml())
        print ("Numer okręgu: " + i.getElementsByTagName("kreisschl")[0].childNodes[0].toxml())
        print ("Numer powiatu: " + i.getElementsByTagName("gmdschl")[0].childNodes[0].toxml())
        print ("Numer gemarkung: " + i.getElementsByTagName("gemaschl")[0].childNodes[0].toxml())
def parcel_nas():
    DOMTree = minidom.parse(userInput)
    cNodes = DOMTree.childNodes
    for i in cNodes[0].getElementsByTagName("AX_Flurstueck"):
        print ("Numer działki: " + i.getElementsByTagName("flurstueckskennzeichen")[0].childNodes[0].toxml())
        print ("Wielkość działki: " + i.getElementsByTagName("amtlicheFlaeche")[0].childNodes[0].toxml())
        print ("Numer landu: " + i.getElementsByTagName("land")[0].childNodes[0].toxml())
        print ("Numer okręgu: " + i.getElementsByTagName("kreis")[0].childNodes[0].toxml())
        print ("Numer powiatu: " + i.getElementsByTagName("gemeinde")[0].childNodes[0].toxml())
        print ("Numer gemarkung: " + i.getElementsByTagName("gemarkungsnummer")[0].childNodes[0].toxml())
def parcel_xyz():
    json_text = str()
    with open(userInput, 'r') as file:
        data = json.load(file)
    print ("Numer działki: " + data['cadastreNo'])
    print ("Wielkość działki: " + data['cadastreNo'])
    print ("Numer landu: " + data['landKey'])
    print ("Numer okręgu: " + data['kreisKey'])
    print ("Numer powiatu: " + data['gemeindeKey'])
    print ("Numer gemarkung: " + data['gemarkungKey'])

while quitVar:
    userInput = input("Wybierz plik który chcesz wczytać, wpisz: parcel_aaa.xml, parcel_nas.xml lub parcel_xyz.json: ")

    if (userInput == "parcel_aaa.xml"):
        parcel_aaa()
    elif (userInput == "parcel_nas.xml"):
        parcel_nas()
    elif (userInput == "parcel_xyz.json"):
        parcel_xyz()
    elif (userInput == "quit"):
        quitVar = False
    else:
        print("Podano złą nazwę pliku.")
    
