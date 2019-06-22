import json
import csv

ldict = {}
for item in range(0,15):
    ldict.update({item : ["",{}]})

def mergea(val):
    d3 = {"Cell" : "" , "Slot" : "", "Unique" : "", "Ingame Name" : "", "Description" : "", "Equip Type" : "Armor"}
#    d4 = dict1
    d3.update(val)
#    d3.update(d4)
#    print(d3)
    return(d3) 

def mergew(val):
    d3 = {"Cell" : "" , "Slot 1" : "", "Slot 2" : "", "Unique" : "", "Ingame Name" : "", "Description" : "", "Equip Type" : "Weapon"}
#    d4 = dict1
    d3.update(val)
#    d3.update(d4)
    return(d3) 

with open("Behemoths.json") as f:
    Behemoths = json.load(f)

def initdata():
    equips = {}
    for item in Behemoths.keys():
        armor = {"Cell" : "" , "Slot" : "", "Ingame Name" : "", "Description" : "", "Equip Type" : "Armor"}
        weapon = {"Cell" : "" , "Slot 1" : "", "Slot 2" : "", "Unique" : "", "Ingame Name" : "", "Description" : "", "Equip Type" : "Weapon"}
        equips.update({item+" Head" : mergea({"Region" : "Head","Source Behemoth" : item,"Levels" : ldict})})
        equips.update({item+" Chest" : mergea({"Region" : "Chest","Source Behemoth" : item,"Levels" : ldict})})
        equips.update({item+" Legs" : mergea({"Region" : "Legs","Source Behemoth" : item,"Levels" : ldict})})
        equips.update({item+" Hands" : mergea({"Region" : "Hands","Source Behemoth" : item,"Levels" : ldict})})
        equips.update({item+" Sword" : mergew({"Region" : "Sword","Source Behemoth" : item,"Source Behemoth" : item,"Levels" : ldict})})
        equips.update({item+" Hammer" : mergew({"Region" : "Hammer","Source Behemoth" : item,"Levels" : ldict})})
        equips.update({item+" Chainblades" : mergew({"Region" : "Chainblades","Source Behemoth" : item,"Levels" : ldict})})
        equips.update({item+" Axe" : mergew({"Region" : "Axe","Source Behemoth" : item,"Levels" : ldict})})
        equips.update({item+" War Pike" : mergew({"Region" : "War Pike","Source Behemoth" : item,"Levels" : ldict})})
    equips.update({"Charrogg Exotic Helm" : mergea({"Region" : "Head","Source Behemoth" : "Charrogg","Levels" : ldict})})
    equips.update({"Charrogg Exotic Weapon" : mergew({"Region" : "Hammer","Source Behemoth" : "Charrogg","Levels" : ldict})})
    equips.update({"Shrowd Exotic Helm" : mergea({"Region" : "Head","Source Behemoth" : "Shrowd","Levels" : ldict})})
    equips.update({"Shrowd Exotic Weapon" : mergew({"Region" : "Sword","Source Behemoth" : "Shrowd","Levels" : ldict})})
    equips.update({"Rezakiri Exotic Helm" : mergea({"Region" : "Head","Source Behemoth" : "Rezakiri","Levels" : ldict})})
    equips.update({"Rezakiri Exotic Weapon" : mergew({"Region" : "War Pike","Source Behemoth" : "Rezakiri","Levels" : ldict})})
    equips.update({"Repeaters" : mergew({"Region" : "Repeaters","Levels" : ldict})})
##    for item in equips:
##        print(item)
##    print(equips["Rezakiri Exotic Weapon"])
    print("Pre Save")
    with open("EquipsV2"+".json", "w") as filez:
        json.dump(equips, filez, indent=4)
    filez.close()
    print("Saved")

def toexcel():
    with open("Equips.json") as f:
        Gear = json.load(f)
    with open('Weapon Data.csv', 'w', newline="\n") as csvfile:
        fieldnames = ["Name", "Innate Cell", "Slot 1", "Slot 2","ID","Element","Unique","Description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in Gear:
            if Gear[item]["Equip Type"] == "Weapon":
                writer.writerow({'ID': item, "Innate Cell": Gear[item]["Cell"], "Name": Gear[item]["Ingame Name"], "Slot 1" : Gear[item]["Slot 1"], "Slot 2": Gear[item]["Slot 2"], "Description": Gear[item]["Description"], "Unique": Gear[item]["Unique"], 'Element': Gear[item]["Element"]})


    with open('Armor Data.csv', 'w', newline="\n") as csvfile:
        fieldnames = ["Name", "Innate Cell", "Slot 1","ID","Strength","Weakness","Unique","Description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in Gear:
            if Gear[item]["Equip Type"] == "Armor":
                writer.writerow({'ID': item, "Innate Cell": Gear[item]["Cell"], "Name": Gear[item]["Ingame Name"], "Slot 1": Gear[item]["Slot"], "Strength": Gear[item]["Resists"], "Description": Gear[item]["Description"], "Unique": Gear[item]["Unique"], 'Weakness': Gear[item]["Weak"]})

def fromexcel():
    with open("Equips.json") as f:
        Gear = json.load(f)
    with open('Weapon Data.csv', newline="\n") as csvfile:
        wfile = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in wfile:
            if row[4] not in ["ID","Repeaters","Rezakiri Exotic","Shroud Exotic","Charrogg Exotic"]:
                Gear[row[4]].update({"Ingame Name": row[0]})
                Gear[row[4]].update({"Unique": row[6]})
                Gear[row[4]].update({"Slot 1": row[2]})
                Gear[row[4]].update({"Slot 2": row[3]})
                Gear[row[4]].update({"Cell": row[1]})
                
        with open("Equips"+".json", "w") as filez:
            json.dump(Gear, filez, indent=4)

    with open('Armor Data.csv', newline="\n") as csvfile:
        afile = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in afile:
            if row[3] not in ["ID","Rezakiri Exotic","Shroud Exotic","Charrogg Exotic"]:
                Gear[row[3]].update({"Ingame Name": row[0]})
                Gear[row[3]].update({"Unique": row[6]})
                Gear[row[3]].update({"Slot": row[2]})
                Gear[row[3]].update({"Cell": row[1]})
                
        with open("Equips"+".json", "w") as filez:
            json.dump(Gear, filez, indent=4)




def laser():
    f =  open("Weapon Data.csv","r")
    conv = f.read().split(",")
    f.close()
    perks = ["None","Assassins Vigour","Bloodless","Fireproof","Fortress","Guardian","Iceborne","Insulated","Nine Lives","Shellshock Resist","Sturdy","Tough","Warmth","Agility","Conditioning","Endurance","Evasion","Fleet Footed","Nimble","Swift","Aetherhunter","Deconstruction","Knockout King","Overpower","Pacifier","Rage","Ragehunter","Sharpened","Acidic","Adrenaline","Barbed","Bladestorm","Cunning","Evasive Fury","Merciless","Molten","Predator","Savagery","Weighted Strikes","Wild Frenzy","Aetherborne","Aetheric Attunement","Aetheric Frenzy","Conduit","Energized","Lucent","Medic","Stunning Vigour","Vampiric"]
    cells = ["None", "Defence", "Mobility", "Power", "Technique", "Utility"]
    for item in conv:
        if item in perks:
            conv[conv.index(item)] = str(perks.index(item))
        if item in cells:
            conv[conv.index(item)] = str(cells.index(item))
    final = open("laser.csv","w")
    final.write(",".join(conv))
    final.close()

    f =  open("Armor Data.csv","r")
    conv = f.read().split(",")
    f.close()
    print(conv)
    perk = ["None","Assassins Vigour","Bloodless","Fireproof","Fortress","Guardian","Iceborne","Insulated","Nine Lives","Shellshock Resist","Sturdy","Tough","Warmth","Agility","Conditioning","Endurance","Evasion","Fleet Footed","Nimble","Swift","Aetherhunter","Deconstruction","Knockout King","Overpower","Pacifier","Rage","Ragehunter","Sharpened","Acidic","Adrenaline","Barbed","Bladestorm","Cunning","Evasive Fury","Merciless","Molten","Predator","Savagery","Weighted Strikes","Wild Frenzy","Aetherborne","Aetheric Attunement","Aetheric Frenzy","Conduit","Energized","Lucent","Medic","Stunning Vigour","Vampiric"]
    cell = ["None", "Defence", "Mobility", "Power", "Technique", "Utility"]
    for item in conv:
        if item in perks:
            conv[conv.index(item)] = str(perk.index(item))
        if item in cells:
            conv[conv.index(item)] = str(cell.index(item))
    final = open("laser2.csv","w")
    final.write(",".join(conv))
    final.close()

def perks(item):
    perk = ["None","Assassins Vigour","Bloodless","Fireproof","Fortress","Guardian","Iceborne","Insulated","Nine Lives","Shellshock Resist","Sturdy","Tough","Warmth","Agility","Conditioning","Endurance","Evasion","Fleet Footed","Nimble","Swift","Aetherhunter","Deconstruction","Knockout King","Overpower","Pacifier","Rage","Ragehunter","Sharpened","Acidic","Adrenaline","Barbed","Bladestorm","Cunning","Evasive Fury","Merciless","Molten","Predator","Savagery","Weighted Strikes","Wild Frenzy","Aetherborne","Aetheric Attunement","Aetheric Frenzy","Conduit","Energized","Lucent","Medic","Stunning Vigour","Vampiric"]
    item = str(perk.index(item))
    return(item)

def cells(item):
    cell = ["None", "Defence", "Mobility", "Power", "Technique", "Utility"]
    item = str(cell.index(item))
    return(item)
def split():
    with open("Equips.json") as f:
        Gear = json.load(f)

    with open("Behemoths.json") as b:
        Behemoths = json.load(b)

    with open('Weapons.csv', 'w', newline="\n") as csvfile:
        fieldnames = ["Swords", "Hammers", "Chainblades", "Axes","War Pikes"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in Behemoths:
            writer.writerow({'Swords': perks(Gear[item+" "+"Sword"]["Cell"]), 'Hammers': perks(Gear[item+" "+"Hammer"]["Cell"]), 'Chainblades': perks(Gear[item+" "+"Chainblades"]["Cell"]), 'Axes': perks(Gear[item+" "+"Axe"]["Cell"]), 'War Pikes': perks(Gear[item+" "+"War Pike"]["Cell"])})
        for item in Behemoths:
            writer.writerow({'Swords': cells(Gear[item+" "+"Sword"]["Slot 1"]), 'Hammers': cells(Gear[item+" "+"Hammer"]["Slot 1"]), 'Chainblades': cells(Gear[item+" "+"Chainblades"]["Slot 1"]), 'Axes': cells(Gear[item+" "+"Axe"]["Slot 1"]), 'War Pikes': cells(Gear[item+" "+"War Pike"]["Slot 1"])})
        for item in Behemoths:
            writer.writerow({'Swords': cells(Gear[item+" "+"Sword"]["Slot 2"]), 'Hammers': cells(Gear[item+" "+"Hammer"]["Slot 2"]), 'Chainblades': cells(Gear[item+" "+"Chainblades"]["Slot 2"]), 'Axes': cells(Gear[item+" "+"Axe"]["Slot 2"]), 'War Pikes': cells(Gear[item+" "+"War Pike"]["Slot 2"])})
        for item in Behemoths:
            writer.writerow({'Swords': Gear[item+" "+"Sword"]["Ingame Name"], 'Hammers': Gear[item+" "+"Hammer"]["Ingame Name"], 'Chainblades': Gear[item+" "+"Chainblades"]["Ingame Name"], 'Axes': Gear[item+" "+"Axe"]["Ingame Name"], 'War Pikes': Gear[item+" "+"War Pike"]["Ingame Name"]})


    with open('Armors.csv', 'w', newline="\n") as csvfile:
        fieldnames = ["Heads", "Chest", "Gloves", "Legs"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in Behemoths:
                writer.writerow({'Heads': Gear[item+" "+"Head"]["Ingame Name"], 'Chest': Gear[item+" "+"Chest"]["Ingame Name"], 'Gloves': Gear[item+" "+"Hands"]["Ingame Name"], 'Legs': Gear[item+" "+"Legs"]["Ingame Name"]})

#fromexcel()
#split()
initdata()
