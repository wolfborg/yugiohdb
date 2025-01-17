import couchdb
import requests
import json
from tkinter import *

server = couchdb.Server('http://admin:password@localhost:5984')
db = server['yugioh']

#for id in db:
#    doc = db[id]
#    print(doc['name'])

def checkDatabase(data):
    print()
    print("Found in database.")
    print("Num of entries: " + str(len(data["inventory"])))
    
    num = 0
    doc_id = data["_id"]
    for inv in data["inventory"]:
        setCheck = inv["set_code"] == setCode.get()
        editionCheck = inv["edition"] == edition.get()
        rarityCheck = inv["rarity"] == rarity.get()
        if setCheck and editionCheck and rarityCheck:
            #update quantity
            quantityChange = inv["quantity"] + int(quantity.get())
            data["inventory"][num]["quantity"] = quantityChange
            db[doc_id] = data
            print("Quantity updated: " + str(quantityChange))
            print()
            return
        else:
            if num < len(data["inventory"])-1:
                num += 1
                continue
            #add new entry to inventory
            inventory = {"set_code": setCode.get(),
                        "edition": edition.get(),
                        "rarity": rarity.get(),
                        "quantity": int(quantity.get())}
            data["inventory"].append(inventory)
            db[doc_id] = data
            print("Inventory updated: " + str(data["inventory"][-1]))
            print()
            return
    return

def addEntry():
    if serial.get():
        print("Entry submitted.")
        print("Name: " + name.get())
        print("Serial: " + serial.get())

        found = False
        mango = {"selector": {"id": serial.get()}}
        for i in db.find(mango):
            checkDatabase(i)
            return        
        
        url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?id=" + serial.get()
        data = requests.get(url).json()
        if "data" in data:
            card = data["data"][0]
            card["id"] = serial.get()
            
            if "card_prices" in card:
                card.pop("card_prices")
            if "id" in card["card_images"][0]:
                card["card_images"][0].pop("id")

            if "card_sets" in card:
                card.pop("card_sets")
            if setCode.get(): print("Set: " + setCode.get())
            if edition.get(): print("Edition: " + edition.get())
            if rarity.get(): print("Rarity: " + rarity.get())
            if quantity.get(): print("Quantity: " + quantity.get())
            inventory = [{"set_code": setCode.get(),
                        "edition": edition.get(),
                        "rarity": rarity.get(),
                        "quantity": int(quantity.get())}]
            card["inventory"] = inventory
            db.save(card)
            print("Added to database.")
        else:
            print("Card not found: " + serial.get())
        print()

def resetForm():
    serial.delete(0,END)
    setOptions["menu"].delete(0,END)
    setCode.set("")
    name.set("")
    quantity.delete(0,END)

def searchCard():
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?id=" + serial.get()
    data = requests.get(url).json()
    if "data" in data:
        card = data["data"][0]
        name.set(card["name"])
        setOptions["menu"].delete(0,END)
        setCode.set("")

        if "card_sets" in card:
            sets = card.pop("card_sets")
            codes = []
            for s in sets:
                code = s["set_code"]
                if code not in codes:
                    codes.append(code)
            setCode.set(codes[0])
            for c in codes:
                setOptions["menu"].add_command(label=c, command=lambda x=c: setCode.set(x))
    else:
        print("Card not found: " + serial.get())

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
name = StringVar(None, "")
Label(inventoryFrame, textvariable=name).pack()

setFrame = Frame(inventoryFrame)
setFrame.pack(padx=7, pady=5, side=LEFT)
Label(setFrame, text="Set:").pack(side=LEFT)
setCodes = [""]
setCode = StringVar(None, "")
setOptions = OptionMenu(setFrame, setCode, *setCodes)
setOptions.pack(side=LEFT)


editionFrame = Frame(inventoryFrame)
editionFrame.pack(padx=7, pady=5, side=LEFT)
Label(editionFrame, text="Edition:").pack(side=LEFT)
editions = ["Unlimited", "1st", "Limited"]
edition = StringVar(None, "1st")
editionOptions = OptionMenu(editionFrame, edition, *editions)
editionOptions.pack(side=LEFT)

rarityFrame = Frame(inventoryFrame)
rarityFrame.pack(padx=7, pady=5, side=LEFT)
Label(rarityFrame, text="Rarity:").pack(side=LEFT)
rarities = ["C", "R", "SR", "UR", "ScR"]
rarity = StringVar(None, "C")
rarityOptions = OptionMenu(rarityFrame, rarity, *rarities)
rarityOptions.pack(side=LEFT)

quantityFrame = Frame(inventoryFrame)
quantityFrame.pack(padx=7, pady=5, side=LEFT)
Label(quantityFrame, text="Qty:").pack(side=LEFT)
quantity = Entry(quantityFrame, width=6)
quantity.pack(side=LEFT)

bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)

submit = Button(bottomFrame, text="Submit", width=15, command=addEntry)
submit.pack(padx=50, pady=15, side=LEFT)

search = Button(bottomFrame, text="Search", width=15, command=searchCard)
search.pack(padx=50, pady=5, side=LEFT)

window.mainloop()


