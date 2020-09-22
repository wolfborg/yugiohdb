import couchdb
import requests
import json
from tkinter import *

server = couchdb.Server('http://admin:password@localhost:5984')
db = server['yugioh']

#for id in db:
#    doc = db[id]
#    print(doc['name'])

def addEntry():
    if serial.get():
        print("Entry submitted.")
        #db.save(card)
        url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?id=" + serial.get()
        r = requests.get(url)
        data = r.json()
        try:
            print(data["data"][0]["name"])
        except:
            print("Card not found: " + serial.get())
        #print(card)
        #print()

def resetForm():
    serial.delete(0,END)
    setCode.delete(0,END)
    edition.delete(0,END)
    rarity.delete(0,END)
    quantity.delete(0,END)

window = Tk()
window.minsize(600,200)

Label(window, text="Enter Yugioh card info").pack()

topFrame = Frame(window)
topFrame.pack(pady=5)

serialFrame = Frame(topFrame)
serialFrame.pack(pady=5)
Label(serialFrame, text="Serial:").pack(side=LEFT)
serial = Entry(serialFrame, width=30)
serial.pack(side=LEFT)

reset = Button(serialFrame, text="Reset", width=6, command=resetForm)
reset.pack(padx=5, side=LEFT)


inventoryFrame = Frame(window)
inventoryFrame.pack(pady=5)
Label(inventoryFrame, text="Inventory:").pack()

setFrame = Frame(inventoryFrame)
setFrame.pack(padx=7, pady=5, side=LEFT)
Label(setFrame, text="Set:").pack(side=LEFT)
setCode = Entry(setFrame, width=15)
setCode.pack(side=LEFT)

editionFrame = Frame(inventoryFrame)
editionFrame.pack(padx=7, pady=5, side=LEFT)
Label(editionFrame, text="Edition:").pack(side=LEFT)
edition = Entry(editionFrame, width=10)
edition.pack(side=LEFT)

rarityFrame = Frame(inventoryFrame)
rarityFrame.pack(padx=7, pady=5, side=LEFT)
Label(rarityFrame, text="Rarity:").pack(side=LEFT)
rarity = Entry(rarityFrame, width=4)
rarity.pack(side=LEFT)

quantityFrame = Frame(inventoryFrame)
quantityFrame.pack(padx=7, pady=5, side=LEFT)
Label(quantityFrame, text="Qty:").pack(side=LEFT)
quantity = Entry(quantityFrame, width=6)
quantity.pack(side=LEFT)

bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
submit = Button(bottomFrame, text="Submit", width=25, command=addEntry)
submit.pack(padx=50, pady=25)

window.mainloop()


