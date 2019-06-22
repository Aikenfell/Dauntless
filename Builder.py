from tkinter import *
import json
from itertools import product
import math

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
##    return(relative_path)
    

with open(resource_path("Cells.json")) as f:
    Base = json.load(f)

with open(resource_path("Equips.json")) as f:
    Gear = json.load(f)

perks = {}

#print(Base.keys())
perks.update({"None" : "Null"})

for item in Base:
    for cell in Base[item]:
        perks.update({cell : item})
#print(perks)

helmlist = ["Free"]
chestlist = ["Free"]
handlist = ["Free"]
leglist = ["Free"]
weaplist = ["Free"]
types = ["Free"]

for item in Gear:
    if Gear[item]["Equip Type"] == "Armor":            
            if Gear[item]["Region"] == "Head":
                helmlist.append(item)                
            if Gear[item]["Region"] == "Chest":
                chestlist.append(item)                
            if Gear[item]["Region"] == "Hands":
                handlist.append(item)                
            if Gear[item]["Region"] == "Legs":
                leglist.append(item)                
    elif Gear[item]["Equip Type"] == "Weapon":
        weaplist.append(item)                
        if Gear[item]["Region"] not in types:
            types.append(Gear[item]["Region"])

def checker(item,source):
    if item in source:
        return(True)
    else:
        return(False)
def ex(crit,weaps):
        pas = []
        for item in weaps:
            if Gear[item]["Region"] == crit:
                pas.append(item)
        return(pas)

def match(searching,locks):
    matches = []
    armor = []
    weapons = []
    head = []
    chest = []
    legs = []
    hands = []
    for query in searching:
        for item in Gear:
            if Gear[item]["Equip Type"] == "Armor" and checker(item,matches) == False:            
                
                if Gear[item]["Cell"] == query:
                    matches.append(item)
                    armor.append(1)
                    if Gear[item]["Region"] == "Head":
                        head.append(item)
                        matches.append(item)
                    elif Gear[item]["Region"] == "Chest":
                        chest.append(item)
                        matches.append(item)
                    elif Gear[item]["Region"] == "Hands":
                        hands.append(item)
                        matches.append(item)
                    elif Gear[item]["Region"] == "Legs":
                        legs.append(item)
                        matches.append(item)


                elif Gear[item]["Slot"] == perks[query] and checker(item,matches) == False:
                    matches.append(item)
                    armor.append(1)
                    if Gear[item]["Region"] == "Head":
                        head.append(item)
                        matches.append(item)
                    elif Gear[item]["Region"] == "Chest":
                        chest.append(item)
                        matches.append(item)
                    elif Gear[item]["Region"] == "Hands":
                        hands.append(item)
                        matches.append(item)
                    elif Gear[item]["Region"] == "Legs":
                        legs.append(item)
                        matches.append(item)

            elif Gear[item]["Equip Type"] == "Weapon":
                if Gear[item]["Cell"] == query:
                    weapons.append(item)
                    matches.append(item)
                elif Gear[item]["Slot 1"] == perks[query]:
                    weapons.append(item)
                    matches.append(item)
                elif Gear[item]["Slot 2"] == perks[query]:
                    weapons.append(item)
                    matches.append(item)
#    print(locks[0])
    if locks[0] != "Free":
        weapons = [locks[0]]
    if locks[1] != "Free":
        head = [locks[1]]
    if locks[2] != "Free":
        chest = [locks[2]]
    if locks[3] != "Free":
        hands = [locks[3]]
    if locks[4] != "Free":
        legs = [locks[4]]
    print(locks[5])
    if locks[5] != "Free" and locks[0] == "Free":
        print(ex(locks[5],weapons),"vawdverwvqewv qe")
        z = product(ex(locks[5],weapons),head,chest,legs,hands)

        
    else:
        z = product(weapons,head,chest,legs,hands)

    tt = []
    final = open("test.txt","a")
    
    for combo in z:
        tt.append(combo)
    print(len(tt))
    print(tt[0])
    return(tt)
#    final.write("\n".join(tt))

#    final.close()
#    for combo in z:
#        print(combo)

def find():
    clist = sorted(list(perks.keys()))
    rlist = ["+1","+2","+3","+4","+5","+6"]
    master = Tk()

    Label(master, text="Perk 1").grid(row=2, column=0)
    p1c = StringVar(master)
    p1c.set("None") # default value

    Label(master, text="Rank").grid(row=2, column=3)
    r1c = StringVar(master)
    r1c.set(rlist[5]) # default value

    p1 = OptionMenu(master, p1c, *clist)
    p1.grid(row=2, column=1)
    r1 = OptionMenu(master, r1c, *rlist)
    r1.grid(row=2, column=2)
######################################################################Slot 1

    Label(master, text="Perk 2").grid(row=3, column=0)
    p2c = StringVar(master)
    p2c.set("None") # default value

    Label(master, text="Rank").grid(row=3, column=3)
    r2c = StringVar(master)
    r2c.set(rlist[5]) # default value

    p2 = OptionMenu(master, p2c, *clist)
    p2.grid(row=3, column=1)
    r2 = OptionMenu(master, r2c, *rlist)
    r2.grid(row=3, column=2)
######################################################################Slot 2

    Label(master, text="Perk 3").grid(row=4, column=0)
    p3c = StringVar(master)
    p3c.set("None") # default value

    Label(master, text="Rank").grid(row=4, column=3)
    r3c = StringVar(master)
    r3c.set(rlist[5]) # default value

    p3 = OptionMenu(master, p3c, *clist)
    p3.grid(row=4, column=1)
    r3 = OptionMenu(master, r3c, *rlist)
    r3.grid(row=4, column=2)
######################################################################Slot 3

    Label(master, text="Perk 4").grid(row=5, column=0)
    p4c = StringVar(master)
    p4c.set("None") # default value

    Label(master, text="Rank").grid(row=5, column=3)
    r4c = StringVar(master)
    r4c.set(rlist[5]) # default value

    p4 = OptionMenu(master, p4c, *clist)
    p4.grid(row=5, column=1)
    r4 = OptionMenu(master, r4c, *rlist)
    r4.grid(row=5, column=2)
######################################################################Slot 4

    Label(master, text="Perk 5").grid(row=6, column=0)
    p5c = StringVar(master)
    p5c.set("None") # default value

    Label(master, text="Rank").grid(row=6, column=3)
    r5c = StringVar(master)
    r5c.set(rlist[5]) # default value

    p5 = OptionMenu(master, p5c, *clist)
    p5.grid(row=6, column=1)
    r5 = OptionMenu(master, r5c, *rlist)
    r5.grid(row=6, column=2)
######################################################################Slot 5

    Label(master, text="Perk 6").grid(row=7, column=0)
    p6c = StringVar(master)
    p6c.set("None") # default value

    Label(master, text="Rank").grid(row=7, column=3)
    r6c = StringVar(master)
    r6c.set(rlist[5]) # default value

    p6 = OptionMenu(master, p6c, *clist)
    p6.grid(row=7, column=1)
    r6 = OptionMenu(master, r6c, *rlist)
    r6.grid(row=7, column=2)
######################################################################Slot 6

    Label(master, text="Perk 7").grid(row=8, column=0)
    p7c = StringVar(master)
    p7c.set("None") # default value

    Label(master, text="Rank").grid(row=8, column=3)
    r7c = StringVar(master)
    r7c.set(rlist[5]) # default value

    p7 = OptionMenu(master, p7c, *clist)
    p7.grid(row=8, column=1)
    r7 = OptionMenu(master, r7c, *rlist)
    r7.grid(row=8, column=2)
######################################################################Slot 7

    Label(master, text="Perk 8").grid(row=9, column=0)
    p8c = StringVar(master)
    p8c.set("None") # default value

    Label(master, text="Rank").grid(row=9, column=3)
    r8c = StringVar(master)
    r8c.set(rlist[5]) # default value

    p8 = OptionMenu(master, p8c, *clist)
    p8.grid(row=9, column=1)
    r8 = OptionMenu(master, r8c, *rlist)
    r8.grid(row=9, column=2)
######################################################################Slot 8

    Label(master, text="Perk 9").grid(row=10, column=0)
    p9c = StringVar(master)
    p9c.set("None") # default value

    Label(master, text="Rank").grid(row=10, column=3)
    r9c = StringVar(master)
    r9c.set(rlist[5]) # default value

    p9 = OptionMenu(master, p9c, *clist)
    p9.grid(row=10, column=1)
    r9 = OptionMenu(master, r9c, *rlist)
    r9.grid(row=10, column=2)
######################################################################Slot 9

    Label(master, text="Perk 10").grid(row=11, column=0)
    p10c = StringVar(master)
    p10c.set("None") # default value

    Label(master, text="Rank").grid(row=11, column=3)
    r10c = StringVar(master)
    r10c.set(rlist[5]) # default value

    p10 = OptionMenu(master, p10c, *clist)
    p10.grid(row=11, column=1)
    r10 = OptionMenu(master, r10c, *rlist)
    r10.grid(row=11, column=2)
######################################################################Slot 10

    Label(master, text="Perk 11").grid(row=12, column=0)
    p11c = StringVar(master)
    p11c.set("None") # default value

    Label(master, text="Rank").grid(row=12, column=3)
    r11c = StringVar(master)
    r11c.set(rlist[5]) # default value

    p11 = OptionMenu(master, p11c, *clist)
    p11.grid(row=12, column=1)
    r11 = OptionMenu(master, r11c, *rlist)
    r11.grid(row=12, column=2)
######################################################################Slot 11

    Label(master, text="Perk 12").grid(row=13, column=0)
    p12c = StringVar(master)
    p12c.set("None") # default value

    Label(master, text="Rank").grid(row=13, column=3)
    r12c = StringVar(master)
    r12c.set(rlist[5]) # default value

    p12 = OptionMenu(master, p12c, *clist)
    p12.grid(row=13, column=1)
    r12 = OptionMenu(master, r12c, *rlist)
    r12.grid(row=13, column=2)
######################################################################Slot 11

    Label(master, text="Locked Weapon").grid(row=15, column=0)
    l1c = StringVar(master)
    l1c.set("Free") # default value

    l1 = OptionMenu(master, l1c, *weaplist)
    l1.grid(row=15, column=1)

######################################################################Weapon Slot

    Label(master, text="Locked Helmet").grid(row=16, column=0)
    l2c = StringVar(master)
    l2c.set("Free") # default value

    l2 = OptionMenu(master, l2c, *helmlist)
    l2.grid(row=16, column=1)

######################################################################Weapon Slot

    Label(master, text="Locked Chestpiece").grid(row=17, column=0)
    l3c = StringVar(master)
    l3c.set("Free") # default value

    l3 = OptionMenu(master, l3c, *chestlist)
    l3.grid(row=17, column=1)

######################################################################Weapon Slot

    Label(master, text="Locked Gloves").grid(row=18, column=0)
    l4c = StringVar(master)
    l4c.set("Free") # default value

    l4 = OptionMenu(master, l4c, *handlist)
    l4.grid(row=18, column=1)

######################################################################Weapon Slot

    Label(master, text="Locked Legs").grid(row=19, column=0)
    l5c = StringVar(master)
    l5c.set("Free") # default value

    l5 = OptionMenu(master, l5c, *leglist)
    l5.grid(row=19, column=1)

######################################################################Weapon Slot
    Label(master, text="General Weapon Lock").grid(row=15, column=4)
    l6c = StringVar(master)
    l6c.set("Free") # default value

    l6 = OptionMenu(master, l6c, *types)
    l6.grid(row=15, column=3)

######################################################################General Range Lock
    Label(master, text="Rejected Perk 1").grid(row=16, column=4)
    e1c = StringVar(master)
    e1c.set("None") # default value

    e1 = OptionMenu(master, e1c, *clist)
    e1.grid(row=16, column=3)

########################################################################Perk Exclusion 1
    Label(master, text="Rejected Perk 2").grid(row=17, column=4)
    e2c = StringVar(master)
    e2c.set("None") # default value

    e2 = OptionMenu(master, e2c, *clist)
    e2.grid(row=17, column=3)

########################################################################Perk Exclusion 2
    Label(master, text="Rejected Perk 3").grid(row=18, column=4)
    e3c = StringVar(master)
    e3c.set("None") # default value

    e3 = OptionMenu(master, e3c, *clist)
    e3.grid(row=18, column=3)

########################################################################Perk Exclusion 3



    Button(master, text='Build',command=lambda: [build([[p1c.get(),r1c.get()],[p2c.get(),r2c.get()],[p3c.get(),r3c.get()],[p4c.get(),r4c.get()],[p5c.get(),r5c.get()],[p6c.get(),r6c.get()],[p7c.get(),r7c.get()],[p8c.get(),r8c.get()],[p9c.get(),r9c.get()],[p10c.get(),r10c.get()],[p11c.get(),r11c.get()],[p12c.get(),r12c.get()]],[l1c.get(),l2c.get(),l3c.get(),l4c.get(),l5c.get(),l6c.get()],[e1c.get(),e2c.get(),e3c.get(),])]).grid(row=25, column=1, sticky=W, pady=4)

    Button(master, text='Quit Program',command=lambda: [master.quit()]).grid(row=25, column=0, sticky=W, pady=4)
#[[],[]]
    mainloop()
    master.destroy()

def build(Sets,Locks,rej):
    Criteria = {}
#    Locks = [Lock1,Lock2,Lock3,Lock4,Lock5]
#    Sets = [Set1,Set2,Set3,Set4,Set5,Set6,Set7,Set8,Set9,Set10,Set11,Set12]
    for item in Sets:
        if item[0] != "None":
            if item[0] not in Criteria: 
                    if item[1] == "None":
                        Criteria.update({item[0] : 1 })
                    else:
#                        print(item[1][1])
                        Criteria.update({item[0] : int(item[1][1])})

#                    print(Criteria)

            else:
                    if item[1] == "None":                       
                        Criteria[item[0]] += 1
                    else:
                        Criteria[item[0]] += int(item[1][1])
    for item in Criteria:
        Criteria[item] = int(math.ceil(float(Criteria[item]/3)))
    pack = []
    for item in Criteria:
        pack.append(item) 
##This Is Going To Form All Possible Matches Based On Perks Asked For
    con = match(pack,Locks)
    values = Criteria
    print(values)
##This Is Going To Check Through All Of Them
    mat = []
    for item in con:
        test1 = extract(item)
        test2 = values
        val = perfect(test1,test2,item,rej)
#        print(test2)
        if val == False:
            fin = list(item)
            fin.append(extract(item))
            mat.append(str(fin))
#            print(item)
    print(len(mat))
    window = Tk()
    mat = list(set(mat))
    Label(window, text="Please Enter The Name Of The File You Want The Results To Be In").grid(row=1, column=0)
    User_input = Entry(window)
    User_input.grid()
    Button(window, text='Get Builds',command=lambda: [window.quit()]).grid(row=15, column=0, sticky=W, pady=4)

    window.mainloop()
    nam = User_input.get()
    window.destroy()
    fn = nam+".txt"
    final = open(fn,"w")

    final.write(str("\n\n".join(mat)))
    final.close()
    print("Done")

def perfect(setii,crit,arm,rej):
#    print(rej)
    crit = dict(crit)
    orig = dict(crit)
    seti = setii
    cri = crit
#    print(seti,"set perks")
#    print(cri,"criteria perks")

    for item in seti:
#        print(item)
        if item in cri:
            cri[item] = cri[item] - seti[item]
#            print(cri)
    fail = False
#    print()
    for item in cri:
        if cri[item] != 0:
#            print(item)
            fail = True
    if fail == True:
        cri = celcheck(setii,cri)
#        print(cri)

    fail = False
    for item in cri:
        if cri[item] != 0:
    #            print(item)
            fail = True
    for item in rej:
        if item in setii and item != "None":
            fail = True
    
    return(fail)

def celcheck(setii,crit):
    for item in crit:
        if item !=0:
            if perks[item] in setii:
                if (setii[perks[item]] - crit[item]) >= 0:
                    setii[perks[item]] = setii[perks[item]] - crit[item]
                    crit[item] = 0
    return(crit)


def extract(Set):
    com = {"Utility" : 1}
#    Weap,Helm,Chest,Legs,Hands
    for item in Set:
        if Gear[item]["Equip Type"] == "Armor":            
            if Gear[item]["Cell"] not in com:
                com.update({Gear[item]["Cell"] : 1})
            else:
                com[Gear[item]["Cell"]] += 1

            if Gear[item]["Slot"] not in com:
                com.update({Gear[item]["Slot"] : 1})
            else:
                com[Gear[item]["Slot"]] += 1

            
        elif Gear[item]["Equip Type"] == "Weapon":            

            if Gear[item]["Cell"] not in com:
                com.update({Gear[item]["Cell"] : 1})
            else:
                com[Gear[item]["Cell"]] += 1

            if Gear[item]["Slot 1"] not in com:
                com.update({Gear[item]["Slot 1"] : 1})
            else:
                com[Gear[item]["Slot 1"]] += 1


            if Gear[item]["Slot 2"] not in com:
                com.update({Gear[item]["Slot 2"] : 1})
            else:
                com[Gear[item]["Slot 2"]] += 1

    return(com)

#def rank(mat,cri)
#    for item in 







#x = extract(['Charrogg Exotic Weapon', 'Rezakiri Head', 'Drask Chest', 'Boreus Legs', 'Boreus Hands'])
#print(x)
find()
#perfect(extract(['Charrogg Exotic Weapon', 'Rezakiri Head', 'Drask Chest', 'Boreus Legs', 'Boreus Hands']),{'Aetheric Attunement': 2},('Charrogg Exotic Weapon', 'Hellion Head', 'Charrogg Chest', 'Charrogg Legs', 'Charrogg Hands'),[])
