import json

with open("CellsV2.json") as f:
    Cells = json.load(f)

with open("EquipsV2.json") as f:
    Gear = json.load(f)

        
equip = {}
equiptypes = {}
cells = {}
celltypes = {}
behemoths = {}

arrays = {"Equips" : equip , "Equiptypes" : equiptypes , "Cells" : cells , "Cell Types" : celltypes , "Behemoths" : behemoths , }

for item in Gear:
    equip.update({ item : len(equip) })

for item in Gear:
    if Gear[item]["Region"] not in equiptypes:
        equiptypes.update({ Gear[item]["Region"] : len(equiptypes) })

for item in Cells:
    if Cells[item]["Type"] not in celltypes:
        celltypes.update({ Cells[item]["Type"] : len(celltypes) })

for item in Cells:
    cells.update({ item : len(cells) })

for item in Gear:
    if Gear[item]["Source Behemoth"] not in behemoths:
        behemoths.update({ Gear[item]["Source Behemoth"] : len(behemoths) })



with open("Int.json", "w") as f:
    json.dump(arrays, f, indent=4)


