import Memoria


def skillful_means(*args):
    #print(args)
    memor = args[0]
    memor.sp += 3
    print("Increased own SP by 3")

def song_to_shooting_stars(*args):
    turncount = args[-1]
    lst = args[0]
    #print(lst)
    if (turncount > 0):   
        print("'Song to Shooting Stars' is Active for " + str(turncount) + " turns")
        if turncount < 5:
            for x in lst:
                x.sp +=2 
        for x in lst:
            x.buffs["Crit Rate (STSS) - 100%"] = str(turncount) + " turns"
            x.buffs["Crit DMG (STSS) - 100%"] = str(turncount) + " turns"
            x.buffs["Diva (STSS)"] = str(turncount) + " turns"
    else:
        x.buffs.pop("Crit Rate (STSS) - 100%")
        x.buffs.pop("Crit DMG (STSS) - 100%")
        x.buffs.pop("Diva (STSS)")

def angels_wings(*args):
    memor = args[0]
    enemy_debuffs = args[1]
    turncount = args[2]
    if turncount == 3:
        memor.buffs["AW - 100% DMG RED"] = "2 hits"
    if turncount > 0:
        print("Angel's Wings is active - Enemy provoked for " + str(turncount) + " turns")
        enemy_debuffs["AW - Provoked"] = str(turncount) + " turns"
    else:
        enemy_debuffs.pop("AW - Provoked")

def luna(*args):
    target = args[0]
    skill = args[1]
    mode = args[2]
    actv_skills = args[3]
    if mode == 0:
        #Countdown mode
        curr = target.buffs["Luna (Non EX)"]
        turncount = int(curr[0:1])
        if turncount == 1:
            target.buffs.pop("Luna (Non EX)")
            actv_skills[target].pop(skill)
        else:
            turncount -=1
            target.buffs["Luna (Non EX)"] = str(turncount) + " turns"
    else:
        #Enable mode
        target.buffs["Luna (Non EX)"] = "3 turns"

