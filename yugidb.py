import couchdb
from tkinter import *

#server = couchdb.Server('http://admin:password@localhost:5984')
#db = server['yugioh']

#for id in db:
#    doc = db[id]
#    print(doc['name'])


def addEntry():
    if name.get():
        print("Entry submitted.")
        print("Name: " + name.get())
        print("Card Type: " + cardType.get())
        print("Serial: " + serial.get())
        if effect.get("1.0","end").strip():
            print("Effect: ")
            print(effect.get("1.0","end").strip())
        if attr.get(): print("Attribute: " + attr.get())
        if level.get(): print("Level: " + level.get())
        print()

def resetTypeVals():
    attr.set("DARK")
    level.set("0")
    spellType.set("Normal")
    trapType.set("Normal")

def specialSelect():
    if currSpecial.get() != specialType.get():
        level.set("")
        currSpecial.set(specialType.get())

    if specialType.get() == "Normal":
        effectFrame.pack_forget()
        flavorFrame.pack(pady=5)
    #elif specialType.get() == "Xyz":
    #elif specialType.get() == "Synchro":
    #elif specialType.get() == "Fusion":
    #elif specialType.get() == "Link":
    #elif specialType.get() == "Pendulum":

def typeSelect():
    if currType.get() != cardType.get():
        resetTypeVals()
        currType.set(cardType.get())

    if cardType.get() == "Monster":
        spellFrame.pack_forget()
        trapFrame.pack_forget()
        monsterFrame.pack(pady=5)
        specialSelect()
    elif cardType.get() == "Spell":
        monsterFrame.pack_forget()
        trapFrame.pack_forget()
        spellFrame.pack(pady=5)
    elif cardType.get() == "Trap":
        monsterFrame.pack_forget()
        spellFrame.pack_forget()
        trapFrame.pack(pady=5)
        
    effectFrame.pack(pady=5)

window = Tk()
window.minsize(500,550)

frame = Frame(window)
frame.pack()

bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)

Label(frame, text="Enter Yugioh card info").pack()

nameFrame = Frame(window)
nameFrame.pack(pady=5)
Label(nameFrame, text="Name:").pack(side=LEFT)
name = Entry(nameFrame)
name.pack(side=LEFT)

serialFrame = Frame(window)
serialFrame.pack(pady=5)
Label(serialFrame, text="Serial:").pack(side=LEFT)
serial = Entry(serialFrame)
serial.pack(side=LEFT)

typeFrame = Frame(window)
typeFrame.pack(pady=5)
Label(typeFrame, text="Card Type:").pack()
cardType = StringVar(None, "Monster")
currType = StringVar(None, "Monster")
cardTypes = ["Monster", "Spell", "Trap"]
for c in cardTypes:
    Radiobutton(typeFrame, text=c, variable=cardType, value=c, command=typeSelect).pack(side=LEFT)

typeInfoFrame = Frame(window)
typeInfoFrame.pack()


monsterFrame = Frame(typeInfoFrame)
monsterFrame.pack(pady=5)

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

specialTypeFrame = Frame(monsterFrame)
specialTypeFrame.pack(padx=5, pady=5, side=LEFT)
Label(levelFrame, text="Level:").pack(side=LEFT)
specialTypes = ["Effect", "Normal", "Fusion", "Link", "Pendulum", "Ritual", "Synchro", "Xyz"]
specialType = StringVar(None, "Effect")
currSpecial = StringVar(None, "Effect")
specialTypeOptions = OptionMenu(specialTypeFrame, specialType, *specialTypes)
specialTypeOptions.pack(side=LEFT)

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

effectFrame = Frame(window)
Label(effectFrame, text="Effect:").pack(side=LEFT)
effect = Text(effectFrame)
effect.pack(side=LEFT)

flavorFrame = Frame(window)
Label(flavorFrame, text="Flavor:").pack(side=LEFT)
flavor = Text(flavorFrame)
flavor.pack(side=LEFT)

typeSelect()

submit = Button(bottomFrame, text="Submit", width=25, command=addEntry)
submit.pack(side=BOTTOM, pady=25)

window.mainloop()


