from tkinter import *
import json
from itertools import product
import math
import time
import yaml

with open("DBV2.json") as f:
    DB = yaml.load(f)

with open("Int.json") as f:
    Int = yaml.load(f)

#print(DB["12"])
def convtime(timec):
    timestr = time.localtime(timec)
    if len(str(timestr[3])) == 1:
        hour = +str(timestr[3])
    else:
        hour = str(timestr[3])

    if len(str(timestr[4])) == 1:
        minute = str(timestr[4])
    else:
        minute = str(timestr[4])

    if len(str(timestr[5])) == 1:
        second = "0"+str(timestr[5])
    else:
        second = str(timestr[5])
        
    return(hour+":"+minute+":"+second)


def timen():
    return time.time()
def et(t1,t2):
    time = t2-t1
    return(time)


def checker(item,source):
    if item in source:
        return(True)
    else:
        return(False)

def check2(v1 , v2 , v3 ,v4):
    if v1 in v4:
        return False

    elif v2 in v4:
        return False
    
    elif v1 == v3:
        return True

    elif v2 == v3:
        return True

    else:
        return False

def match(searching):
    weapons = []
    head = []
    chest = []
    legs = []
    hands = []
    for query in searching:
        query = str(query)
        for item in DB["10"]:
            typ  = DB["12"][query]
            if DB["10"][item]["Cell0"] == query:
                weapons.append(int(item))
            elif check2(DB["10"][item]["Cell1"],DB["10"][item]["Cell2"],typ,weapons) == True:
                weapons.append(int(item))

        for item in DB["0"]:
            if DB["0"][item]["Cell0"] == query:
                head.append(int(item))
                
            elif check2(DB["0"][item]["Cell1"],DB["0"][item]["Cell2"],typ,weapons) == True:
                head.append(int(item))

            
        for item in DB["1"]:
            if DB["1"][item]["Cell0"] == query:
                chest.append(int(item))
            elif check2(DB["1"][item]["Cell1"],DB["1"][item]["Cell2"],typ,weapons) == True:
                chest.append(int(item))

#        print(chest)            

        for item in DB["2"]:
            if DB["2"][item]["Cell0"] == query:
                legs.append(int(item))
            elif check2(DB["2"][item]["Cell1"],DB["2"][item]["Cell2"],typ,weapons) == True:
                legs.append(int(item))

        for item in DB["3"]:
            if DB["3"][item]["Cell0"] == query:
                hands.append(int(item))
            elif check2(DB["3"][item]["Cell1"],DB["3"][item]["Cell2"],typ,weapons) == True:
                hands.append(int(item))


    z = product(weapons,head,chest,legs,hands)
    print("GG")    
    tt = []    
    for combo in z:
        tt.append(combo)
    print(len(tt))
    return(tt)

def match2(searching):
    weapons = []
    head = []
    chest = []
    legs = []
    hands = []
    for query in searching:
        for item in DB["10"]:
            typ  = DB["12"][query]
            if DB["10"][item]["Cell0"] == query:
                weapons.append(item)
        for item in DB["0"]:
            if DB["0"][item]["Cell0"] == query:
                head.append(item)
        for item in DB["1"]:
            if DB["1"][item]["Cell0"] == query:
                chest.append(item)
        for item in DB["2"]:
            if DB["2"][item]["Cell0"] == query:
                legs.append(item)
        for item in DB["3"]:
            if DB["3"][item]["Cell0"] == query:
                hands.append(item)
    else:
        z = product(weapons,head,chest,legs,hands)

    tt = []    
    for combo in z:
        tt.append(combo)
    return(tt)


def build(Sets):
    begin = timen()

    Criteria = {}
    for item in Sets:
        if item[0] != "None":
            if item[0] not in Criteria: 
                Criteria.update({item[0] : int(item[1])})
            else:
                Criteria[item[0]] += int(item[1])
    for item in Criteria:
        Criteria[item] = int(math.ceil(float(Criteria[item]/3)))

    pack = []
    for item in Criteria:
        pack.append(item) 
##This Is Going To Form All Possible Matches Based On Perks Asked For
    con = match(pack)
    end3 = timen()
    print(et(begin,end3),"Time Time To Make All Matches")
    values = Criteria
    mat = []
    for item in con:
        val = perfect(extract(item),values,item)
        if val == False:
            fin = item
#            fin.append(extract(item))
            mat.append(str(fin))
#            print(item)
    print(len(mat))
    end = timen()

    nam = "XX"
    fn = nam+".txt"
    final = open(fn,"w")

    final.write(str("\n\n".join(mat)))
    final.close()
    end2 = timen()
    print("Done")
    print(et(begin,end),"Time To Check All Comboes")
    print(et(begin,end2),"Time Including Writing To Disc")

def perfect(setii,crit,arm):
#    print(rej)
    crit = dict(crit)
    orig = dict(crit)
    seti = setii
    cri = crit
    print(seti,"set perks")
    print(cri,"criteria perks")

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
##    for item in rej:
##        if item in setii and item != "None":
##            fail = True
##    
    return(fail)

def celcheck(setii,crit):
    print(setii)
    for item in crit:
        if item !=0:
            if DB["12"][item] in setii:
                if (setii[DB["12"][item]] - crit[item]) >= 0:
                    setii[DB["12"][item]] = setii[DB["12"][item]] - crit[item]
                    crit[item] = 0
    return(crit)


def extract(Set):
    com = {4 : 1}
#    Weap,Helm,Chest,Legs,Hands
    for item in Set:
        item = str(item)

        if DB["13"][item]["Cell0"] not in com:
            com.update({DB["13"][item]["Cell0"] : 1})
        else:
            com[DB["13"][item]["Cell0"]] += 1

        if DB["13"][item]["Cell1"] not in com:
            com.update({DB["13"][item]["Cell1"] : 1})
        else:
            com[DB["13"][item]["Cell1"]] += 1

        if DB["13"][item]["Cell2"] not in com:
            com.update({DB["13"][item]["Cell2"] : 1})
        else:
            com[DB["13"][item]["Cell2"]] += 1
            

    return(com)

#def rank(mat,cri)
#    for item in 





#build([["33",2],["0",2]])

#build([[33,2],[0,2],[11,2],[22,2],[44,2]])

begin = timen()
x = []
i = 0
while i <10000000:
    x.append("i")
    i ++
end3 = timen()
print(et(begin,end3),"Test Time")

#x = extract(['Charrogg Exotic Weapon', 'Rezakiri Head', 'Drask Chest', 'Boreus Legs', 'Boreus Hands'])
#print(x)
##find()
#perfect(extract(['Charrogg Exotic Weapon', 'Rezakiri Head', 'Drask Chest', 'Boreus Legs', 'Boreus Hands']),{'Aetheric Attunement': 2},('Charrogg Exotic Weapon', 'Hellion Head', 'Charrogg Chest', 'Charrogg Legs', 'Charrogg Hands'),[])
