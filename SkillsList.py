import Memoria


def skillful_means(memor:Memoria):
    memor.sp += 3
    print("Increased own SP by 3")

def song_to_shooting_stars(list, turncount):
    print("'Song to Shooting Stars' is Active for " + str(turncount) + " turns")
    if (turncount > 0):   
        if turncount < 5:
            for x in list:
                x.sp +=2 
        for x in list:
            x.buffs["Crit Rate (STSS) - 100%"] = str(turncount) + " turns"
            x.buffs["Crit DMG (STSS) - 100%"] = str(turncount) + " turns"
            x.buffs["Diva (STSS)"] = str(turncount) + " turns"
    else:
        del x.buffs["Crit Rate (STSS) - 100%"]
        del x.buffs["Crit DMG (STSS) - 100%"]
        del x.buffs["Diva (STSS)"]