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

typeFrame = Frame(window)
typeFrame.pack(pady=5)
Label(typeFrame, text="Card Type:").pack()
cardType = StringVar(None, "Monster")
cardTypes = ["Monster", "Spell", "Trap"]
for c in cardTypes:
    Radiobutton(typeFrame, text=c, variable=cardType, value=c).pack(side=LEFT)

monsterFrame = Frame(window)
monsterFrame.pack(pady=5)

attrFrame = Frame(monsterFrame)
attrFrame.pack(padx=5, pady=5, side=LEFT)
Label(attrFrame, text="Attribute:").pack(side=LEFT)
attrs = ["NONE", "DARK", "DIVINE", "EARTH", "FIRE", "LIGHT", "WATER", "WIND"]
attr = StringVar(None, "NONE")
attrOptions = OptionMenu(attrFrame, attr, *attrs)
attrOptions.pack(side=LEFT)

levelFrame = Frame(monsterFrame)
levelFrame.pack(padx=5, pady=5, side=LEFT)
Label(levelFrame, text="Level:").pack(side=LEFT)
levels = [0,1,2,3,4,5,6,7,8,9,10,11,12]
level = IntVar(0)
levelOptions = OptionMenu(levelFrame, level, *levels)
levelOptions.pack(side=LEFT)

effectFrame = Frame(window)
effectFrame.pack(pady=5)
Label(effectFrame, text="Effect:").pack(side=LEFT)
effect = Text(effectFrame)
effect.pack(side=LEFT)

serialFrame = Frame(window)
serialFrame.pack(pady=5)
Label(serialFrame, text="Serial:").pack(side=LEFT)
serial = Entry(serialFrame)
serial.pack(side=LEFT)

submit = Button(bottomFrame, text="Submit", width=25, command=addEntry)
submit.pack(side=BOTTOM, pady=25)

window.mainloop()


