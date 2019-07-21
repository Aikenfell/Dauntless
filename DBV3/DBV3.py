import json
import csv
import demjson
import yaml

ldict = {}
for item in range(0,16):
    ldict.update({item : {"Power" : 0,"Mats" : {}}})

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
    with open("GearV3"+".json", "w") as filez:
        json.dump(equips, filez, indent=4)
    filez.close()
    print("Saved")

#def recruit()


def toexcel():
    with open("EquipsV2.json") as f:
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
    with open("EquipsV2.json") as f:
        Gear = json.load(f)
    with open('Weapon Data.csv', newline="\n") as csvfile:
        wfile = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in wfile:
            if row[4] not in ["ID"]:
                Gear[row[4]].update({"Ingame Name": row[0]})
                Gear[row[4]].update({"Unique": row[6]})
                Gear[row[4]].update({"Slot 1": row[2]})
                Gear[row[4]].update({"Slot 2": row[3]})
                Gear[row[4]].update({"Cell": row[1]})
                
        with open("EquipsV2"+".json", "w") as filez:
            json.dump(Gear, filez, indent=4)

    with open('Armor Data.csv', newline="\n") as csvfile:
        afile = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in afile:
            if row[3] not in ["ID"]:
                Gear[row[3]].update({"Ingame Name": row[0]})
                Gear[row[3]].update({"Unique": row[6]})
                Gear[row[3]].update({"Slot": row[2]})
                Gear[row[3]].update({"Cell": row[1]})
                
        with open("EquipsV2"+".json", "w") as filez:
            json.dump(Gear, filez, indent=4)


def elements():
    with open("GearV3.json") as f:
        Gear = json.load(f)
    with open("Behemoths.json") as f:
        Base = json.load(f)

    for item in Gear:
#        print(item)

        if item != "Repeaters":
            if Gear[item]["Equip Type"] == "Armor":
                Gear[item].update({"Resists" : Base[Gear[item]["Source Behemoth"]]["Strong"],"Weakness" : Base[Gear[item]["Source Behemoth"]]["Weak"]})
            elif Gear[item]["Equip Type"] == "Weapon":
                Gear[item].update({"Element" : Base[Gear[item]["Source Behemoth"]]["Strong"]})
    with open("EquipsV2"+".json", "w") as filez:
        json.dump(Gear, filez, indent=4)

def hecate():
    with open("GearV3.json") as f:
        Gear = json.load(f)
    with open("CellsV2.json") as f:
        Cell = json.load(f)
    with open("DBB.json") as f:
        Base = json.load(f)
    with open("DBIDS.json") as f:
        IDS = json.load(f)
    dbids = {}
    cellids = {}
    for item in IDS["Armours"]:
        dbids.update({IDS["Armours"][item] : item})

    for item in IDS["Weapons"]:
        dbids.update({IDS["Weapons"][item] : item})
    for item in IDS["Cells"]:
        cellids.update({IDS["Cells"][item] : item})

    for item in Gear:
        if item != "Repeaters":            
            try:           
                Gear[item]["Description"] = Base["armours"][Gear[item]["Ingame Name"]]["description"]
            except:
                Gear[item]["Description"] = Base["weapons"][Gear[item]["Ingame Name"]]["description"]

            try:
                Gear[item]["Unique"] = Base["armours"][Gear[item]["Ingame Name"]]["unique_effects"][len(Base["armours"][Gear[item]["Ingame Name"]]["unique_effects"])-1]["description"]
            except:
                pass
            try:
                Gear[item]["Unique"] = Base["weapons"][Gear[item]["Ingame Name"]]["unique_effects"][len(Base["armours"][Gear[item]["Ingame Name"]]["unique_effects"])-1]["description"]
            except:
                pass

    
            Gear[item].update({"DB ID" : dbids[Gear[item]["Ingame Name"]]})

    for item in Cell:
        st = "+3 "+item+" Cell"
        Cell[item].update({"DB ID" : cellids[st]})



    with open("CellsV3"+".json", "w") as filez:
        json.dump(Cell, filez, indent=4)
    
    with open("GearV3"+".json", "w") as filez:
        json.dump(Gear, filez, indent=4)
    
def mats():
    with open("GearV3.json") as f:
        Gear = json.load(f)

    for item in Gear:
#        print(Gear[item][e])
        if Gear[item]["Equip Type"] == "Weapon":
            if item != "Repeaters":
                if Gear[item]["Element"] in ["Blaze","Frost","Shock","Terra","Neutral"]:
                    Gear[item]["Levels"]["0"]["Mats"] = {"Rams" : 150}
                    Gear[item]["Levels"]["1"]["Mats"] = {"Rams" : 40 , Gear[item]["Element"]+" Orbs" : 7}
                    Gear[item]["Levels"]["2"]["Mats"] = {"Rams" : 60 , Gear[item]["Element"]+" Orbs" : 7}
                    Gear[item]["Levels"]["3"]["Mats"] = {"Rams" : 100 , Gear[item]["Element"]+" Orbs" : 8}
                    Gear[item]["Levels"]["4"]["Mats"] = {"Rams" : 140 , Gear[item]["Element"]+" Orbs" : 8}
                    Gear[item]["Levels"]["5"]["Mats"] = {"Rams" : 160 , Gear[item]["Element"]+" Orbs" : 9}
                    Gear[item]["Levels"]["6"]["Mats"] = {"Rams" : 220 , Gear[item]["Element"]+" Orbs" : 9 , "Dull Arcstone" : 12}
                    Gear[item]["Levels"]["7"]["Mats"] = {"Rams" : 240 , Gear[item]["Element"]+" Orbs" : 10 , "Dull Arcstone" : 15}
                    Gear[item]["Levels"]["8"]["Mats"] = {"Rams" : 290 , Gear[item]["Element"]+" Orbs" : 10 , "Dull Arcstone" : 18 , "Shining Arcstone" : 20}
                    Gear[item]["Levels"]["9"]["Mats"] = {"Rams" : 350 , Gear[item]["Element"]+" Orbs" : 11 , "Dull Arcstone" : 21 , "Shining Arcstone" : 40}
                    Gear[item]["Levels"]["10"]["Mats"] = {"Rams" : 400 , Gear[item]["Element"]+" Orbs" : 11 , "Dull Arcstone" : 24 , "Shining Arcstone" : 60}
                    Gear[item]["Levels"]["11"]["Mats"] = {"Rams" : 600 , "Peerless Arcstone" : 20}
                    Gear[item]["Levels"]["12"]["Mats"] = {"Rams" : 600 , "Peerless Arcstone" : 25}
                    Gear[item]["Levels"]["13"]["Mats"] = {"Rams" : 600 , "Peerless Arcstone" : 30}
                    Gear[item]["Levels"]["14"]["Mats"] = {"Rams" : 600 , "Peerless Arcstone" : 35}
                    Gear[item]["Levels"]["15"]["Mats"] = {"Rams" : 600 , "Peerless Arcstone" : 40}
                else:
                    Gear[item]["Levels"]["0"]["Mats"] = {"Rams" : 150}
                    Gear[item]["Levels"]["1"]["Mats"] = {"Rams" : 40 , "Dull Arcstone" : 6}
                    Gear[item]["Levels"]["2"]["Mats"] = {"Rams" : 60 , "Dull Arcstone" : 8}
                    Gear[item]["Levels"]["3"]["Mats"] = {"Rams" : 100 , "Dull Arcstone" : 9}
                    Gear[item]["Levels"]["4"]["Mats"] = {"Rams" : 140 , "Dull Arcstone" : 10}
                    Gear[item]["Levels"]["5"]["Mats"] = {"Rams" : 160 , "Dull Arcstone" : 11}
                    Gear[item]["Levels"]["6"]["Mats"] = {"Rams" : 220 , "Dull Arcstone" : 13}
                    Gear[item]["Levels"]["7"]["Mats"] = {"Rams" : 240 , "Dull Arcstone" : 14}
                    Gear[item]["Levels"]["8"]["Mats"] = {"Rams" : 290 , "Dull Arcstone" : 15 , "Shining Arcstone" : 25}
                    Gear[item]["Levels"]["9"]["Mats"] = {"Rams" : 350 , "Dull Arcstone" : 18 , "Shining Arcstone" : 50}
                    Gear[item]["Levels"]["10"]["Mats"] = {"Rams" : 400 , "Dull Arcstone" : 23 , "Shining Arcstone" : 75}
                    Gear[item]["Levels"]["11"]["Mats"] = {"Rams" : 600 , "Peerless Arcstone" : 20}
                    Gear[item]["Levels"]["12"]["Mats"] = {"Rams" : 600 , "Peerless Arcstone" : 25}
                    Gear[item]["Levels"]["13"]["Mats"] = {"Rams" : 600 , "Peerless Arcstone" : 30}
                    Gear[item]["Levels"]["14"]["Mats"] = {"Rams" : 600 , "Peerless Arcstone" : 35}
                    Gear[item]["Levels"]["15"]["Mats"] = {"Rams" : 600 , "Peerless Arcstone" : 40}
                Gear[item]["Levels"]["0"]["Power"] = 100
                Gear[item]["Levels"]["1"]["Power"] = 140
                Gear[item]["Levels"]["2"]["Power"] = 180
                Gear[item]["Levels"]["3"]["Power"] = 220
                Gear[item]["Levels"]["4"]["Power"] = 260
                Gear[item]["Levels"]["5"]["Power"] = 300
                Gear[item]["Levels"]["6"]["Power"] = 340
                Gear[item]["Levels"]["7"]["Power"] = 380
                Gear[item]["Levels"]["8"]["Power"] = 420
                Gear[item]["Levels"]["9"]["Power"] = 460
                Gear[item]["Levels"]["10"]["Power"] = 500
                Gear[item]["Levels"]["11"]["Power"] = 510
                Gear[item]["Levels"]["12"]["Power"] = 520
                Gear[item]["Levels"]["13"]["Power"] = 530
                Gear[item]["Levels"]["14"]["Power"] = 540
                Gear[item]["Levels"]["15"]["Power"] = 550

        if Gear[item]["Equip Type"] == "Armor":
            if Gear[item]["Resists"] in ["Blaze","Frost","Shock","Terra","Neutral"]:
                Gear[item]["Levels"]["0"]["Mats"] = {"Rams" : 40}
                Gear[item]["Levels"]["1"]["Mats"] = {"Rams" : 10 , Gear[item]["Resists"]+" Orbs" : 1}
                Gear[item]["Levels"]["2"]["Mats"] = {"Rams" : 15 , Gear[item]["Resists"]+" Orbs" : 1}
                Gear[item]["Levels"]["3"]["Mats"] = {"Rams" : 25 , Gear[item]["Resists"]+" Orbs" : 2}
                Gear[item]["Levels"]["4"]["Mats"] = {"Rams" : 35 , Gear[item]["Resists"]+" Orbs" : 2}
                Gear[item]["Levels"]["5"]["Mats"] = {"Rams" : 40 , Gear[item]["Resists"]+" Orbs" : 2}
                Gear[item]["Levels"]["6"]["Mats"] = {"Rams" : 55 , Gear[item]["Resists"]+" Orbs" : 3 , "Dull Arcstone" : 3}
                Gear[item]["Levels"]["7"]["Mats"] = {"Rams" : 60 , Gear[item]["Resists"]+" Orbs" : 4 , "Dull Arcstone" : 4}
                Gear[item]["Levels"]["8"]["Mats"] = {"Rams" : 75 , Gear[item]["Resists"]+" Orbs" : 5 , "Dull Arcstone" : 5 , "Shining Arcstone" : 5}
                Gear[item]["Levels"]["9"]["Mats"] = {"Rams" : 90 , Gear[item]["Resists"]+" Orbs" : 6 , "Dull Arcstone" : 6 , "Shining Arcstone" : 10}
                Gear[item]["Levels"]["10"]["Mats"] = {"Rams" : 100 , Gear[item]["Resists"]+" Orbs" : 7 , "Dull Arcstone" : 7 , "Shining Arcstone" : 15}
                Gear[item]["Levels"]["11"]["Mats"] = {"Rams" : 150 , "Peerless Arcstone" : 5}
                Gear[item]["Levels"]["12"]["Mats"] = {"Rams" : 150 , "Peerless Arcstone" : 6}
                Gear[item]["Levels"]["13"]["Mats"] = {"Rams" : 150 , "Peerless Arcstone" : 7}
                Gear[item]["Levels"]["14"]["Mats"] = {"Rams" : 150 , "Peerless Arcstone" : 8}
                Gear[item]["Levels"]["15"]["Mats"] = {"Rams" : 150 , "Peerless Arcstone" : 9}
            else:
                Gear[item]["Levels"]["0"]["Mats"] = {"Rams" : 40}
                Gear[item]["Levels"]["1"]["Mats"] = {"Rams" : 10 , "Dull Arcstone" : 2}
                Gear[item]["Levels"]["2"]["Mats"] = {"Rams" : 15 , "Dull Arcstone" : 2}
                Gear[item]["Levels"]["3"]["Mats"] = {"Rams" : 25 , "Dull Arcstone" : 2}
                Gear[item]["Levels"]["4"]["Mats"] = {"Rams" : 35 , "Dull Arcstone" : 2}
                Gear[item]["Levels"]["5"]["Mats"] = {"Rams" : 40 , "Dull Arcstone" : 3}
                Gear[item]["Levels"]["6"]["Mats"] = {"Rams" : 55 , "Dull Arcstone" : 3}
                Gear[item]["Levels"]["7"]["Mats"] = {"Rams" : 60 , "Dull Arcstone" : 3}
                Gear[item]["Levels"]["8"]["Mats"] = {"Rams" : 75 , "Dull Arcstone" : 4 , "Shining Arcstone" : 7}
                Gear[item]["Levels"]["9"]["Mats"] = {"Rams" : 90 , "Dull Arcstone" : 4 , "Shining Arcstone" : 13}
                Gear[item]["Levels"]["10"]["Mats"] = {"Rams" : 100 , "Dull Arcstone" : 5 , "Shining Arcstone" : 20}
                Gear[item]["Levels"]["11"]["Mats"] = {"Rams" : 150 , "Peerless Arcstone" : 5}
                Gear[item]["Levels"]["12"]["Mats"] = {"Rams" : 150 , "Peerless Arcstone" : 6}
                Gear[item]["Levels"]["13"]["Mats"] = {"Rams" : 150 , "Peerless Arcstone" : 7}
                Gear[item]["Levels"]["14"]["Mats"] = {"Rams" : 150 , "Peerless Arcstone" : 8}
                Gear[item]["Levels"]["15"]["Mats"] = {"Rams" : 150 , "Peerless Arcstone" : 9}
            Gear[item]["Levels"]["0"]["Power"] = 25
            Gear[item]["Levels"]["1"]["Power"] = 35
            Gear[item]["Levels"]["2"]["Power"] = 45
            Gear[item]["Levels"]["3"]["Power"] = 55
            Gear[item]["Levels"]["4"]["Power"] = 65
            Gear[item]["Levels"]["5"]["Power"] = 75
            Gear[item]["Levels"]["6"]["Power"] = 85
            Gear[item]["Levels"]["7"]["Power"] = 95
            Gear[item]["Levels"]["8"]["Power"] = 105
            Gear[item]["Levels"]["9"]["Power"] = 115
            Gear[item]["Levels"]["10"]["Power"] = 125
            Gear[item]["Levels"]["11"]["Power"] = 127.5
            Gear[item]["Levels"]["12"]["Power"] = 130
            Gear[item]["Levels"]["13"]["Power"] = 132.5
            Gear[item]["Levels"]["14"]["Power"] = 135
            Gear[item]["Levels"]["15"]["Power"] = 137.5

    with open("GearV3"+".json", "w") as filez:
        json.dump(Gear, filez, indent=4)

def cellsV2():
    with open("Cells.json") as f:
        Data = json.load(f)
    final = {}
    for item in Data:
        for perk in Data[item]:
            final.update({perk : {"Description" : Data[item][perk] , "Type" : item}})
            for rank in range(1,7):
                final[perk].update({"Tier "+str(rank) : {"Description" : "", "Buffs" : {"Test 1" : "", "Test 2" : ""}}})


    with open("CellsV2"+".json", "w") as filez:
        json.dump(final, filez, indent=4)



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

def cellexport():
    with open("CellsV2.json") as f:
        Data = json.load(f)

    with open('Cell Data.csv', 'w', newline="\n") as csvfile:
        fieldnames = ["Name", "Description", "Type", "T1D", "T1B", "T2D", "T2B", "T3D", "T3B", "T4D", "T4B", "T5D", "T5B", "T6D", "T6B"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in Data:
            writer.writerow({
                'Name': item,
                "Description": Data[item]["Description"],
                "Type": Data[item]["Type"],
                "T1D": Data[item]["Tier 1"]["Description"],
                "T1B": Data[item]["Tier 1"]["Buffs"],
                "T2D": Data[item]["Tier 2"]["Description"],
                "T2B": Data[item]["Tier 2"]["Buffs"],
                "T3D": Data[item]["Tier 3"]["Description"],
                "T3B": Data[item]["Tier 3"]["Buffs"],
                "T4D": Data[item]["Tier 4"]["Description"],
                "T4B": Data[item]["Tier 4"]["Buffs"],
                "T5D": Data[item]["Tier 5"]["Description"],
                "T5B": Data[item]["Tier 5"]["Buffs"],
                "T6D": Data[item]["Tier 6"]["Description"],
                "T6B": Data[item]["Tier 6"]["Buffs"]
                })

def cellupdate():
    with open("CellsV2.json") as f:
        Data = json.load(f)
    for item in Data:
        Data[item].update({"Weapons" : [] ,"Armors" : []})

    with open("EquipsV2.json") as f:
        Gear = json.load(f)
    for piece in Gear:
        if Gear[piece]["Equip Type"] == "Weapon":
            if Gear[piece]["Cell"] != "None":
                Data[Gear[piece]["Cell"]]["Weapons"].append(piece)
        else:
            if Gear[piece]["Cell"] != "None":
                Data[Gear[piece]["Cell"]]["Armors"].append(piece)

    with open("CellsV2"+".json", "w") as filez:
        json.dump(Data, filez, indent=4)


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

def behemupdate():
    with open("EquipsV2.json") as f:
        Gear = json.load(f)

    with open("Behemoths.json") as b:
        Behemoths = json.load(b)

    for item in Behemoths:
        Behemoths[item].update({"Gear" : []})
    for item in Gear:
        if Gear[item]["Source Behemoth"] != "None":
            Behemoths[Gear[item]["Source Behemoth"]]["Gear"].append(item)

    with open("Behemoths.json", "w") as filez:
        json.dump(Behemoths, filez, indent=4)


def partcsv():
    with open("EquipsV2.json") as f:
        Gear = json.load(f)
    with open('Parts.csv', 'w', newline="\n") as csvfile:
        fieldnames = ["Item", "Simple", "Base", "+5 To +6", "+9 To +10"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in Gear:
            v1 = {}
            v2 = {}
            v3 = {}
            for mat in Gear[item]["Levels"]["0"]["Mats"]:
                if mat not in ["Rams","Peerless Arcstone","Shining Arcstone","Dull Arcstone","Blaze Orbs","Frost Orbs","Terra Orbs","Shock Orbs","Neutral Orbs"]:
                    v1.update({mat : Gear[item]["Levels"]["0"]["Mats"][mat]})

            for mat in Gear[item]["Levels"]["6"]["Mats"]:
                if mat not in ["Rams","Peerless Arcstone","Shining Arcstone","Dull Arcstone","Blaze Orbs","Frost Orbs","Terra Orbs","Shock Orbs","Neutral Orbs"]:
                    v2.update({mat : Gear[item]["Levels"]["6"]["Mats"][mat]})

            for mat in Gear[item]["Levels"]["10"]["Mats"]:
                if mat not in ["Rams","Peerless Arcstone","Shining Arcstone","Dull Arcstone","Blaze Orbs","Frost Orbs","Terra Orbs","Shock Orbs","Neutral Orbs"]:
                    v3.update({mat : Gear[item]["Levels"]["10"]["Mats"][mat]})


                
            writer.writerow({'Item': Gear[item]["Ingame Name"], 'Simple': item, 'Base': v1, '+5 To +6': v2, '+9 To +10': v3,})


def intexport():
    with open("GearV3.json") as f:
        Gear = json.load(f)
    with open("CellsV3.json") as f:
        Cells = json.load(f)
    inte = {}
    str2int = {}
    int2str = {}
    gear2int = {"None" : 0}
    int2gear = {0: "None"}
    gt2int = {"None" : 0}
    int2gt = {0: "None"}
    ct2int = {"None" : 0}
    int2ct = {0: "None"}
    cell2int = {"None" : 0}
    int2cell = {0: "None"}
    for item in Cells:
        if Cells[item]["Type"] not in ct2int:
            int2ct.update({ len(ct2int)+1000 : Cells[item]["Type"] })
            ct2int.update({ Cells[item]["Type"] : len(ct2int)+1000 })
        if item not in cell2int:
            int2cell.update({ len(cell2int) : item})
            cell2int.update({ item : { 0 : len(cell2int) , 1 : ct2int[Cells[item]["Type"]] } })
    for item in Gear:
        if Gear[item]["Region"] not in gt2int:
            int2gt.update({ len(gt2int) : Gear[item]["Region"]})
            gt2int.update({ Gear[item]["Region"] : len(gt2int) })
        if item not in gear2int:
            int2gear.update({ len(gear2int) : item})
            gear2int.update({ item : len(gear2int) })
            try:
                try:
                    gear2int.update({ item : { 0 : len(gear2int) ,  1 : ct2int[Gear[item]["Slot 1"]] ,  2 : ct2int[Gear[item]["Slot 2"]] ,  3 : cell2int[Gear[item]["Cell"]][0] }})
                except:
                    gear2int.update({ item : { 0 : len(gear2int) ,  1 : ct2int[Gear[item]["Slot 1"]] ,  2 : ct2int[Gear[item]["Slot 2"]] ,  3 : 0 }})
            except:
                try:
                    gear2int.update({ item : { 0 : len(gear2int) ,  1 : ct2int[Gear[item]["Slot"]] ,  2 : 0 ,  3 : cell2int[Gear[item]["Cell"]][0] }})
                except:
                    gear2int.update({ item : { 0 : len(gear2int) ,  1 : ct2int[Gear[item]["Slot"]] ,  2 : 0 ,  3 : 0 }})
    inte.update({"gt2int" : gt2int })
    inte.update({"int2gt" : int2gt })
    inte.update({"ct2int" : ct2int })
    inte.update({"int2ct" : int2ct })
    inte.update({"gear2int" : gear2int })
    inte.update({"int2gear" : int2gear })
    inte.update({"cell2int" : cell2int })
    inte.update({"int2cell" : int2cell })
    with open("DBV3.json", "w") as filez:
        json.dump(inte, filez, indent=4)
    with open("DBV3.yaml", "w") as filez:
        yaml.dump(inte, filez, indent=4)


def intexportl():
    with open("GearV3.json") as f:
        Gear = json.load(f)
    with open("CellsV3.json") as f:
        Cells = json.load(f)
    inte = {}
    str2int = {}
    int2str = {}
    gear2int = {"None" : 0}
    int2gear = {0: "None"}
    gt2int = {"None" : 0}
    int2gt = {0: "None"}
    ct2int = {"None" : 0}
    int2ct = {0: "None"}
    cell2int = {"None" : 0}
    int2cell = {0: "None"}
    head = {}
    torso = {}
    arms = {}
    legs = {}
    for item in Cells:
        if Cells[item]["Type"] not in ct2int:
            int2ct.update({ len(ct2int)+1000 : Cells[item]["Type"] })
            ct2int.update({ Cells[item]["Type"] : len(ct2int)+1000 })
        if item not in cell2int:
            int2cell.update({ len(cell2int) : item})
            cell2int.update({ item : { 0 : len(cell2int) , 1 : ct2int[Cells[item]["Type"]] } })
    for item in Gear:
        if Gear[item]["Region"] not in gt2int:
            int2gt.update({ len(gt2int) : Gear[item]["Region"]})
            gt2int.update({ Gear[item]["Region"] : len(gt2int) })
        if item not in gear2int:
            int2gear.update({ len(gear2int) : item})
            try:
                try:
                    gear2int.update({ item : { "ID" : len(gear2int) ,  "Cell Slot One Type" : ct2int[Gear[item]["Slot 1"]] ,  "Cell Slot Two Type" : ct2int[Gear[item]["Slot 2"]] ,  "Innate Cell" : cell2int[Gear[item]["Cell"]][0] , "Innate Cell Type" : cell2int[Gear[item]["Cell"]][1] , "Region" : gt2int[Gear[item]["Region"]]}})
                except:
                    gear2int.update({ item : { "ID" : len(gear2int) ,  "Cell Slot One Type" : ct2int[Gear[item]["Slot 1"]] ,  "Cell Slot Two Type" : ct2int[Gear[item]["Slot 2"]] ,  "Innate Cell" : 0  , "Innate Cell Type" : 0, "Region" : gt2int[Gear[item]["Region"]]}})
            except:
                try:
                    gear2int.update({ item : { "ID" : len(gear2int) ,  "Cell Slot One Type" : ct2int[Gear[item]["Slot"]] ,  "Cell Slot Two Type" : 0 ,  "Innate Cell" : cell2int[Gear[item]["Cell"]][0] , "Innate Cell Type" : cell2int[Gear[item]["Cell"]][1] , "Region" : gt2int[Gear[item]["Region"]]}})
                except:
                    gear2int.update({ item : { "ID" : len(gear2int) ,  "Cell Slot One Type" : ct2int[Gear[item]["Slot"]] ,  "Cell Slot Two Type" : 0 ,  "Innate Cell" : 0  , "Innate Cell Type" : 0 , "Region" : gt2int[Gear[item]["Region"]]}})

    

    inte.update({"gt2int" : gt2int })
    inte.update({"int2gt" : int2gt })
    inte.update({"ct2int" : ct2int })
    inte.update({"int2ct" : int2ct })
    inte.update({"gear2int" : gear2int })
    inte.update({"int2gear" : int2gear })
    inte.update({"cell2int" : cell2int })
    inte.update({"int2cell" : int2cell })
    with open("DBV3l.json", "w") as filez:
        json.dump(inte, filez, indent=4)
    with open("DBV3l.yaml", "w") as filez:
        yaml.dump(inte, filez, indent=4)



##
##    with open("demofile.yaml") as f:
##        xx = yaml.load(f)
##    for item in xx:
##        print(item)
###    print(xx)

#split()
#initdata()
#elements()
#fromexcel()
#hecate()
#mats()
intexportl()
##cellsV2()
##cellexport()
##cellupdate()
##behemupdate()
##partcsv()
