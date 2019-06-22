import json

with open("Cells.json") as f:
    Cells = json.load(f)

eff = []
for item in Cells:
    for perk in item:
        eff.append(Cells[item][perk])
            with open('Weapon Data.csv', 'w', newline="\n") as csvfile:
