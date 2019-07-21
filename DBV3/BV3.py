from tkinter import *
import json
from itertools import product,combinations
import math
import time
import os
import numpy as np
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#with open(os.path.join(BASE_DIR,"base\\static\\DBV2.json")) as f:
#    DB = json.load(f)

#with open(os.path.join(BASE_DIR,"base\\static\\Int.json")) as f:
#    Int = json.load(f)


with open("DBV3L.json") as f:
    DB = json.load(f)
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

def s_c(value):#slot_conversion
    value = int(math.ceil(float(value)))
    return(value)
def timen():
    return time.time()
def et(t1,t2):
    time = t2-t1
    return(time)


def m_s(Perks_Wanted):#make_sets
    print(Perks_Wanted)
    begin = timen()
    Gear = ([],[],[],[],[])
    Types = []
    for item in Perks_Wanted:
        Types.append(DB["cell2int"][DB["int2cell"][str(item)]]["1"])
    for item in DB["gear2int"]:
        if item == "None":  
            pass
        elif DB["gear2int"][item]["Innate Cell"] in Perks_Wanted:
            if DB["gear2int"][item]["Region"] in [1,2,3,4]:
                Gear[DB["gear2int"][item]["Region"]-1].append(DB["gear2int"][item]["ID"])
            else:
                print(DB["gear2int"][item])
                Gear[4].append(DB["gear2int"][item]["ID"])
        elif DB["gear2int"][item]["Cell Slot One Type"] or DB["gear2int"][item]["Cell Slot Two Type"] in Types:
            if DB["gear2int"][item]["Region"] in [1,2,3,4]:
                Gear[DB["gear2int"][item]["Region"]-1].append(DB["gear2int"][item]["ID"])
            else:
                Gear[4].append(DB["gear2int"][item]["ID"])
    #print(Gear[0],Gear[1],Gear[2],Gear[3],Gear[4],Types)
    print(Gear)
    return([product(Gear[0],Gear[1],Gear[2],Gear[3],Gear[4]),Types])

def contains(Build):
    has = {"1005" : 1}
    for item in Build:
        item = str(item)
        if DB["gear2int"][DB["int2gear"][item]]["Innate Cell"] not in has:
            has.update({DB["gear2int"][DB["int2gear"][item]]["Innate Cell"] : 1})
        else:
            has[DB["gear2int"][DB["int2gear"][item]]["Innate Cell"]] += 1
            
        if DB["gear2int"][DB["int2gear"][item]]["Cell Slot One Type"] not in has:
            has.update({DB["gear2int"][DB["int2gear"][item]]["Cell Slot One Type"] : 1})
        else:
            has[DB["gear2int"][DB["int2gear"][item]]["Cell Slot One Type"]] += 1

        if DB["gear2int"][DB["int2gear"][item]]["Cell Slot Two Type"] not in has:
            has.update({DB["gear2int"][DB["int2gear"][item]]["Cell Slot Two Type"] : 1})
        else:
            has[DB["gear2int"][DB["int2gear"][item]]["Cell Slot Two Type"]] += 1
    del has[0]
    has = pieces(has)
    return(has)
                       
def g_c(Input):#  get_criteria
    Perks = {}
    for item in Input:
        if item[0] not in Perks:
            Perks.update({item[0] : s_c(item[1])}) 
        else:
            Perks[item[0]] += s_c(item[1]) 
    Temp = m_s(Perks.keys())
    Types = list(Perks.keys())
    Criteria = list(set(Temp[1]+list(Perks.keys())))
    Builds = Temp[0]
    del Temp
    x = []
    val = 0
    for B in Builds:
#        print(B)
        BuildPerks = contains(B)
        yy = len(BuildPerks)
        CritPerks = pieces(dict(Perks))
        fail = False

        for item in Perks:
            
            if item and DB["cell2int"][DB["int2cell"][str(item)]]["1"] not in BuildPerks:
                fail = True
                break
            else:
                fail = False
                pass
#        print(BuildPerks,B,"Build")
        yy = len(BuildPerks)
        TempPerks = list(CritPerks)
        for item in CritPerks:
            if fail == False:
#                print(B,BuildPerks)
                if item in BuildPerks:
                    BuildPerks.remove(item)
                    TempPerks.remove(item)
                elif DB["cell2int"][DB["int2cell"][str(item)]]["1"] in BuildPerks:
                    BuildPerks.remove(DB["cell2int"][DB["int2cell"][str(item)]]["1"])
                    TempPerks.remove(item)
                else:
#                    print("It Failed")
                    break
            
##                    if yy-len(BuildPerks) == 12:
##                        print(yy-len(BuildPerks))
##                    fail = True

        if TempPerks == []:
            print(B,"Final")
    

##                except:
##                    print("somethin failed")
##                    break                
##        print("\n")
##        if fail == False:
##            x.append(B)
##            if val != len(x):
##                print(len(x))
##            val = len(x)
##    for item in x:
##        print(item)

def pieces(Bleck):
    Items = []
    for item in Bleck:
        while Bleck[item] != 0:
            Items.append(item)
            Bleck[item] -= 1
    return(Items)

##g_c([[6,1],[25,2],[14,1],[23,1]])
##g_c([[25,8],[23,1],[13,2]])
g_c([[5,2],[38,2],[24,2],[22,2],[40,2],[42,2]])
##5
##38
##24
##22
##40
##42

    
def perfect(setii,crit,arm):
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
##    for item in rej:
##        if item in setii and item != "None":
##            fail = True
##    
    return(fail)

def build2(Sets):
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
#            print(item)
#    print(len(mat))
    end = timen()
    end2 = timen()
    print("Done")
    print(et(begin,end),"Time To Check All Comboes")
    print(et(begin,end2),"Time Including Writing To Disc")

def celcheck(setii,crit):
#    print(crit)
    for item in crit:
        if item !=0:
            if DB["12"][item] in setii:
                if (setii[DB["12"][item]] - crit[item]) >= 0:
                    setii[DB["12"][item]] = setii[DB["12"][item]] - crit[item]
                    crit[item] = 0
    return(crit)


def extract(Set):
    com = {"4" : 1}
#    Weap,Helm,Chest,Legs,Hands
    for item in Set:

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

#build([["5",2],["38",2],["24",2],["22",2],["40",2],["42",2]])
