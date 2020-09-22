import couchdb
#import requests
#import json
from tkinter import *

server = couchdb.Server('http://admin:password@localhost:5984')
db = server['yugioh']

#for id in db:
#    doc = db[id]
#    print(doc['name'])

def addEntry():
    if name.get():
        print("Entry submitted.")
        print("Name: " + name.get())
        print("Serial: " + serial.get())
        print("Card Type: " + cardType.get())
        card = {"name": name.get(),
                "serial": serial.get(),
                "type": cardType.get()}
        if cardType.get() == "Monster":
            if specialType.get():
                print("Special Type: " + specialType.get())
                card["specialType"] = specialType.get()
            if attr.get():
                print("Attribute: " + attr.get())
                card["attribute"] = attr.get()
            if level.get():
                print("Level: " + str(level.get()))
                card["level"] = level.get()
            if rank.get():
                print("Rank: " + str(rank.get()))
                card["rank"] = rank.get()
            if linkCost.get():
                print("Link: " + str(linkCost.get()))
                card["linkCost"] = linkCost.get()
            

            for m in monsterTypeVars:
                if m.get() == 1:
                    print("Monster Type(s):")
                    card["monsterType"] = []
                    break
            count = 0
            for m in monsterTypeVars:
                if m.get() == 1:
                    print("-- " + monsterTypes[count])
                    card["monsterType"].append(monsterTypes[count])
                count += 1
            
            for z in zones:
                if z.get() == 1:
                    print("Link Zone(s):")
                    card["linkZones"] = []
                    break
            count = 0
            for z in zones:
                if z.get() == 1:
                    print("-- " + linkDirs[count])
                    card["linkZones"].append(linkDirs[count])
                count += 1
            
            print("ATK: " + str(atkVal.get()))
            card["atk"] = atkVal.get()
            if specialType.get() != "Link":
                print("DEF: " + str(defVal.get()))
                card["def"] = defVal.get()
                
            if summonCost.get("1.0","end").strip():
                print("Summon Cost(s): ")
                print(summonCost.get("1.0","end").strip())
                card["summonCost"] = summonCost.get("1.0","end").strip()
            if flavor.get("1.0","end").strip():
                print("Flavor: ")
                print(flavor.get("1.0","end").strip())
                card["flavor"] = flavor.get("1.0","end").strip()

        if cardType.get() == "Spell":
            if spellType.get():
                print("Spell Type: " + spellType.get())
                card["spellType"] = spellType.get()

        if cardType.get() == "Trap":
            if trapType.get():
                print("Trap Type: " + trapType.get())
                card["trapType"] = trapType.get()
        
        if effect.get("1.0","end").strip():
            print("Effect: ")
            print(effect.get("1.0","end").strip())
            card["effect"] = effect.get("1.0","end").strip()

        if setCode.get():
            print("Set: " + setCode.get())
            if edition.get(): print("Edition: " + edition.get())
            if rarity.get(): print("Rarity: " + rarity.get())
            if quantity.get(): print("Quantity: " + quantity.get())
            inventory = [{"setCode": setCode.get(),
                        "edition": edition.get(),
                        "rarity": rarity.get(),
                        "quantity": quantity.get()}]
            card["inventory"] = inventory
        
        print()
        db.save(card)
        #url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + name.get()
        #r = requests.get(url)
        #data = r.json()
        #print(data["data"][0]["name"])
        #print(card)
        #print()

def resetForm():
    name.delete(0,END)
    serial.delete(0,END)
    setCode.delete(0,END)
    edition.delete(0,END)
    rarity.delete(0,END)
    quantity.delete(0,END)
    resetTypeVals()
    resetLevelVals()
    resetStatVals()
    resetMonsterTypeVals()
    resetLinkZones()
    resetSpellTrap()
    effect.delete("1.0","end")
    flavor.delete("1.0","end")
    summonCost.delete("1.0","end")
    specialType.set("Effect")
    if cardType.get() == "Monster":
        specialSelect("Effect")

def resetTypeVals():
    attr.set("DARK")
    spellType.set("Normal")
    trapType.set("Normal")

def resetLevelVals():
    level.set("0")
    rank.set("0")
    linkCost.set("0")

def resetStatVals():
    atkVal.set("0")
    defVal.set("0")

def resetMonsterTypeVals():
    for m in monsterTypeVars: m.set(0)

def resetLinkZones():
    for z in zones: z.set(0)

def resetSpellTrap():
    spellType.set("Normal")
    trapType.set("Normal")

def specialSelect(val):
    if val == "Normal":
        effectFrame.pack_forget()
        flavorFrame.pack(pady=5)
        effect.delete("1.0","end")
    else:
        flavorFrame.pack_forget()
        effectFrame.pack(pady=5)
        flavor.delete("1.0","end")

    if val == "Xyz" or val == "Link":
        levelFrame.pack_forget()
        resetLevelVals()
    else: levelFrame.pack(side=LEFT)
        
    if val == "Xyz": rankFrame.pack(side=LEFT)
    else: rankFrame.pack_forget()
    
    if val == "Link":
        linkFrame.pack(side=LEFT)
        linkZonesFrame.pack()
        defFrame.pack_forget()
        defVal.set("0")
    else:
        linkFrame.pack_forget()
        linkZonesFrame.pack_forget()
        defFrame.pack(side=LEFT)

    if val != "Normal" and val != "Effect" and val != "Ritual" and val != "Pendulum":
        summonCostFrame.pack(pady=5)
    else:
        summonCostFrame.pack_forget()
        summonCost.delete("1.0","end")
    
    #elif specialType.get() == "Pendulum":

def typeSelect():
    if currType.get() != cardType.get():
        resetTypeVals()
        resetMonsterTypeVals()
        resetStatVals()
        resetLinkZones()
        currType.set(cardType.get())

    if cardType.get() == "Monster":
        spellFrame.pack_forget()
        trapFrame.pack_forget()
        monsterFrame.pack(pady=5)
        monsterFrame2.pack(pady=5)
        specialType.set("Effect")
        specialSelect("Effect")
    elif cardType.get() == "Spell":
        monsterFrame.pack_forget()
        monsterFrame2.pack_forget()
        trapFrame.pack_forget()
        spellFrame.pack(pady=5)
    elif cardType.get() == "Trap":
        monsterFrame.pack_forget()
        monsterFrame2.pack_forget()
        spellFrame.pack_forget()
        trapFrame.pack(pady=5)
        
    effectFrame.pack(pady=5)

window = Tk()
window.minsize(600,900)

Label(window, text="Enter Yugioh card info").pack()

topFrame = Frame(window)
topFrame.pack(pady=5)

nameFrame = Frame(topFrame)
nameFrame.pack(pady=5)
Label(nameFrame, text="Name:").pack(side=LEFT)
name = Entry(nameFrame, width=50)
name.pack(side=LEFT)

reset = Button(nameFrame, text="Reset", width=6, command=resetForm)
reset.pack(padx=5, side=LEFT)

serialFrame = Frame(topFrame)
serialFrame.pack(padx=7, pady=5, side=LEFT)
Label(serialFrame, text="Serial:").pack(side=LEFT)
serial = Entry(serialFrame)
serial.pack(side=LEFT)

typeFrame = Frame(topFrame)
typeFrame.pack(pady=5, side=LEFT)
Label(typeFrame, text="Card Type:").pack(side=LEFT)
cardType = StringVar(None, "Monster")
currType = StringVar(None, "Monster")
cardTypes = ["Monster", "Spell", "Trap"]
for c in cardTypes:
    Radiobutton(typeFrame, text=c, variable=cardType, value=c, command=typeSelect).pack(side=LEFT)

dataFrame = Frame(window)
dataFrame.pack(padx=30)

typeInfoFrame = Frame(dataFrame)
typeInfoFrame.pack()

monsterFrame = Frame(typeInfoFrame)
monsterFrame.pack(pady=5)

specialTypeFrame = Frame(monsterFrame)
specialTypeFrame.pack(padx=5, pady=5)
Label(specialTypeFrame, text="Special Type:").pack(side=LEFT)
specialTypes = ["Effect", "Normal", "Fusion", "Link", "Pendulum", "Ritual", "Synchro", "Xyz"]
specialType = StringVar(None, "Effect")
currSpecial = StringVar(None, "Effect")
specialTypeOptions = OptionMenu(specialTypeFrame, specialType, *specialTypes, command=specialSelect)
specialTypeOptions.pack(side=LEFT)

attrFrame = Frame(monsterFrame)
attrFrame.pack(padx=5, pady=5, side=LEFT)
Label(attrFrame, text="Attribute:").pack(side=LEFT)
attrs = ["DARK", "DIVINE", "EARTH", "FIRE", "LIGHT", "WATER", "WIND"]
attr = StringVar(None, "DARK")
attrOptions = OptionMenu(attrFrame, attr, *attrs)
attrOptions.pack(side=LEFT)

levelFrame = Frame(monsterFrame)
levelFrame.pack(padx=5, pady=5, side=LEFT)
Label(levelFrame, text="Level:").pack(side=LEFT)
levels = [0,1,2,3,4,5,6,7,8,9,10,11,12]
level = IntVar(0)
levelOptions = OptionMenu(levelFrame, level, *levels)
levelOptions.pack(side=LEFT)

#used for xyz
rankFrame = Frame(monsterFrame)
rankFrame.pack(padx=5, pady=5, side=LEFT)
Label(rankFrame, text="Rank:").pack(side=LEFT)
ranks = [0,1,2,3,4,5,6,7,8,9,10,11,12]
rank = IntVar(0)
rankOptions = OptionMenu(rankFrame, rank, *ranks)
rankOptions.pack(side=LEFT)

#used for links
linkFrame = Frame(monsterFrame)
linkFrame.pack(padx=5, pady=5, side=LEFT)
Label(linkFrame, text="Link:").pack(side=LEFT)
linkCosts = [0,1,2,3,4,5,6,7,8,9,10,11,12]
linkCost = IntVar(0)
linkOptions = OptionMenu(linkFrame, linkCost, *linkCosts)
linkOptions.pack(side=LEFT)

linkZonesFrame = Frame(typeInfoFrame)
linkZonesFrame.pack(pady=5)
Label(linkZonesFrame, text="Link Zone(s):").pack()

linkDirs = ["NW", "N", "NE", "W", "E", "SW", "S", "SE"]
intVars = []
for i in linkDirs:
    intVars.append(IntVar())

nw, n, ne, w, e, sw, s, se = intVars
zones = [nw, n, ne, w, e, sw, s, se]

dir1Frame = Frame(linkZonesFrame)
dir1Frame.pack()
Checkbutton(dir1Frame, text=linkDirs[0],variable=zones[0], onvalue=1, offvalue=0).pack(side=LEFT)
Checkbutton(dir1Frame, text=linkDirs[1],variable=zones[1], onvalue=1, offvalue=0).pack(side=LEFT)
Checkbutton(dir1Frame, text=linkDirs[2],variable=zones[2], onvalue=1, offvalue=0).pack(side=LEFT)
dir2Frame = Frame(linkZonesFrame)
Checkbutton(dir2Frame, text=linkDirs[3],variable=zones[3], onvalue=1, offvalue=0).pack(side=LEFT)
Checkbutton(dir2Frame, text=linkDirs[4],variable=zones[4], onvalue=1, offvalue=0).pack(side=LEFT)
dir2Frame.pack()
dir3Frame = Frame(linkZonesFrame)
Checkbutton(dir3Frame, text=linkDirs[5],variable=zones[5], onvalue=1, offvalue=0).pack(side=LEFT)
Checkbutton(dir3Frame, text=linkDirs[6],variable=zones[6], onvalue=1, offvalue=0).pack(side=LEFT)
Checkbutton(dir3Frame, text=linkDirs[7],variable=zones[7], onvalue=1, offvalue=0).pack(side=LEFT)
dir3Frame.pack()

monsterFrame2 = Frame(typeInfoFrame)
monsterFrame2.pack(pady=5)

monsterTypeFrame = Frame(monsterFrame2)
monsterTypeFrame.pack(padx=5, pady=5)
Label(monsterTypeFrame, text="Monster Type(s):").pack()
monsterTypes = ["Aqua", "Beast", "Beast-Warrior",
                "Cyberse", "Dinosaur", "Divine-Beast",
                "Dragon", "Fairy", "Fiend", "Fish",
                "Insect", "Machine", "Plant", "Psychic",
                "Pyro", "Reptile", "Rock", "Sea Serpent",
                "Spellcaster", "Thunder", "Warrior",
                "Winged Beast", "Wyrm", "Zombie", "Tuner",
                "Link", "Synchro", "Xyz", "Fusion", "Ritual",
                "Pendulum", "Effect"]

intVars = []
for i in monsterTypes:
    intVars.append(IntVar())

aqua, beast, beastWarrior, cyberse, dinosaur, divineBeast, dragon, fairy, fiend, fish, insect, machine, plant, psychic, pyro, reptile, rock, seaSerpent, spellcaster, thunder, warrior, wingedBeast, wyrm, zombie, tuner, link, synchro, xyz, fusion, ritual, pendulum, effectType = intVars

monsterTypeVars = [aqua, beast, beastWarrior, cyberse,
                   dinosaur, divineBeast, dragon, fairy,
                   fiend, fish, insect, machine, plant,
                   psychic, pyro, reptile, rock, seaSerpent,
                   spellcaster, thunder, warrior, wingedBeast,
                   wyrm, zombie, tuner, link, synchro, xyz,
                   fusion, ritual, pendulum, effectType]

count = 0
rowFrame = Frame(monsterTypeFrame)
rowFrame.pack(padx=5, pady=5)
sepCount = 1
seperate = 6
for m in monsterTypes:
    if sepCount % (seperate+1) == 0:
        rowFrame = Frame(monsterTypeFrame)
        rowFrame.pack(padx=5)
        sepCount = 1
        seperate = 7
    Checkbutton(
        rowFrame, text=m,
        variable=monsterTypeVars[count],
        onvalue=1, offvalue=0).pack(side=LEFT)
    count += 1
    sepCount += 1

statsFrame = Frame(monsterTypeFrame)
statsFrame.pack(padx=5, pady=5)

atkFrame = Frame(statsFrame)
atkFrame.pack(padx=5, pady=5, side=LEFT)
Label(atkFrame, text="ATK:").pack(side=LEFT)
atkVal = IntVar()
atkStat = Entry(atkFrame, textvariable=atkVal)
atkStat.pack(side=LEFT)

defFrame = Frame(statsFrame)
defFrame.pack(padx=5, pady=5, side=LEFT)
Label(defFrame, text="DEF:").pack(side=LEFT)
defVal = IntVar()
defStat = Entry(defFrame, textvariable=defVal)
defStat.pack(side=LEFT)

spellFrame = Frame(typeInfoFrame)
spellTypeFrame = Frame(spellFrame)
spellTypeFrame.pack(padx=5, pady=5, side=LEFT)
Label(spellTypeFrame, text="Spell Type:").pack(side=LEFT)
spellTypes = ["Normal", "Continuous", "Equip", "Quick-Play", "Field", "Ritual"]
spellType = StringVar(None, "Normal")
spellTypeOptions = OptionMenu(spellTypeFrame, spellType, *spellTypes)
spellTypeOptions.pack(side=LEFT)


trapFrame = Frame(typeInfoFrame)
trapTypeFrame = Frame(trapFrame)
trapTypeFrame.pack(padx=5, pady=5, side=LEFT)
Label(trapTypeFrame, text="Trap Type:").pack(side=LEFT)
trapTypes = ["Normal", "Continuous", "Counter"]
trapType = StringVar(None, "Normal")
trapTypeOptions = OptionMenu(trapTypeFrame, trapType, *trapTypes)
trapTypeOptions.pack(side=LEFT)


summonCostFrame = Frame(typeInfoFrame)
summonCostFrame.pack(pady=5)
Label(summonCostFrame, text="Summon Cost(s):").pack()
summonCost = Text(summonCostFrame, width=55, height=3)
summonCost.pack()

effectFrame = Frame(dataFrame)
Label(effectFrame, text="Effect:").pack()
effect = Text(effectFrame, width=55, height=10)
effect.pack()

flavorFrame = Frame(dataFrame)
Label(flavorFrame, text="Flavor:").pack()
flavor = Text(flavorFrame, width=55, height=10)
flavor.pack()

typeSelect()


inventoryFrame = Frame(window)
inventoryFrame.pack(pady=5)
Label(inventoryFrame, text="Inventory:").pack()

setFrame = Frame(inventoryFrame)
setFrame.pack(padx=7, pady=5, side=LEFT)
Label(setFrame, text="Set:").pack(side=LEFT)
setCode = Entry(setFrame)
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
quantity = Entry(quantityFrame, width=10)
quantity.pack(side=LEFT)

#button to add new row


bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
submit = Button(bottomFrame, text="Submit", width=25, command=addEntry)
submit.pack(padx=50, pady=25)

window.mainloop()


