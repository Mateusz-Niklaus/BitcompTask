from tkinter import *
import tkinter as tk
from xml.dom import minidom
import json

def parcel_aaa():
    label = Label(master, text= "                                                                 ")
    label.grid(row=4, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=5, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=6, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=7, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=8, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=9, column=4)
    DOMTree = minidom.parse(e2.get() + '.xml')
    cNodes = DOMTree.childNodes
    listAaa = []
    for i in cNodes[0].getElementsByTagName("Flurstueck"):
        listAaa.append(i.getElementsByTagName("flstkennz")[0].childNodes[0].toxml())
        listAaa.append(i.getElementsByTagName("flaeche")[0].childNodes[0].toxml())
        listAaa.append(i.getElementsByTagName("landschl")[0].childNodes[0].toxml())
        listAaa.append(i.getElementsByTagName("kreisschl")[0].childNodes[0].toxml())
        listAaa.append(i.getElementsByTagName("gmdschl")[0].childNodes[0].toxml())
        listAaa.append(i.getElementsByTagName("gemaschl")[0].childNodes[0].toxml())
    
    label = Label(text= "Numer działki: " + listAaa[0])
    label.grid(row=4, column=4)
    label = Label(text = "Wielkość działki: " + listAaa[1])
    label.grid(row=5, column=4)
    label = Label(text= "Numer landu: " + listAaa[2])
    label.grid(row=6, column=4)
    label = Label(text= "Numer okręgu: " + listAaa[3])
    label.grid(row=7, column=4)
    label = Label(text= "Numer powiatu: " + listAaa[4])
    label.grid(row=8, column=4)
    label = Label(text= "Numer gemarkung: " + listAaa[5])
    label.grid(row=9, column=4)

def parcel_nas():
    label = Label(master, text= "                                                                 ")
    label.grid(row=4, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=5, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=6, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=7, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=8, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=9, column=4)
    DOMTree = minidom.parse(e2.get() + '.xml')
    cNodes = DOMTree.childNodes
    listNas = []
    for i in cNodes[0].getElementsByTagName("AX_Flurstueck"):
        listNas.append(i.getElementsByTagName("flurstueckskennzeichen")[0].childNodes[0].toxml())
        listNas.append(i.getElementsByTagName("amtlicheFlaeche")[0].childNodes[0].toxml())
        listNas.append(i.getElementsByTagName("land")[0].childNodes[0].toxml())
        listNas.append(i.getElementsByTagName("kreis")[0].childNodes[0].toxml())
        listNas.append(i.getElementsByTagName("gemeinde")[0].childNodes[0].toxml())
        listNas.append(i.getElementsByTagName("gemarkungsnummer")[0].childNodes[0].toxml())

    label = Label(text= "Numer działki: " + listNas[0])
    label.grid(row=4, column=4)
    label = Label(text = "Wielkość działki: " + listNas[1])
    label.grid(row=5, column=4)
    label = Label(text= "Numer landu: " + listNas[2])
    label.grid(row=6, column=4)
    label = Label(text= "Numer okręgu: " + listNas[3])
    label.grid(row=7, column=4)
    label = Label(text= "Numer powiatu: " + listNas[4])
    label.grid(row=8, column=4)
    label = Label(text= "Numer gemarkung: " + listNas[5])
    label.grid(row=9, column=4)

def parcel_xyz():
    label = Label(master, text= "                                                                 ")
    label.grid(row=4, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=5, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=6, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=7, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=8, column=4)
    label = Label(master, text= "                                                                 ")
    label.grid(row=9, column=4)
    with open(e2.get() + '.json', 'r') as file:
        data = json.load(file)
    label = Label(master, text= "Numer działki: " + data['cadastreNo'])
    label.grid(row=4, column=4)
    label = Label(master, text= "Wielkość działki: " + str(data['area']))
    label.grid(row=5, column=4)
    label = Label(master, text= "Numer landu: " + data['landKey'])
    label.grid(row=6, column=4)
    label = Label(master, text= "Numer okręgu: " + data['kreisKey'])
    label.grid(row=7, column=4)
    label = Label(master, text= "Numer powiatu: " + data['gemeindeKey'])
    label.grid(row=8, column=4)
    label = Label(master, text= "Numer gemarkung: " + data['gemarkungKey'])
    label.grid(row=9, column=4)

def error():
    label = Label(master, text= "Niepoprawny format lub nazwa pliku.")
    label.grid(row=4, column=4)

master = tk.Tk()
master.title('My title')
master.geometry("500x300")
tk.Label(master,text="Format pliku").grid(row=0)
tk.Label(master,text="Nazwa pliku").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def chose():
    if (e1.get() == "aaa"):
        parcel_aaa()
    elif (e1.get() == "nas"):
        parcel_nas()
    elif (e1.get() == "xyz"):
        parcel_xyz()
    else:
        error()

tk.Button(master,text='Wypisz',command=chose).grid(row=3, column=1,sticky=tk.W, pady=10, padx=10)

tk.mainloop()



