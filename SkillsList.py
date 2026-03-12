import Memoria as mm


def skillful_means(*args):
    #print(args)
    memor = args[0]
    memor.sp += 3
    print("Increased own SP by 3")

def song_to_shooting_stars(*args):
    allies = args[0]
    for ally in allies:
        CritRate = mm.crit_rate_buff("Crit Rate Up - Songstress Blessing", True, 5, None, 100)
        CritDmg = mm.crit_dmg_buff("Crit DMG Up - Songstress Blessing", True, 5, None, 90)
        ally.buffs_upd.append(CritRate)
        ally.buffs_upd.append(CritDmg)

def angels_wings(*args):
    memor = args[0]
    AngelWings = mm.dmg_reduction_buff("Angel's Wings", False, 2, 100)
    memor.buffs_upd.append(AngelWings)
    print("Angel's Wings is active - Enemy provoked for 3 turns")

def luna(*args):
    target = args[0]
    Luna = mm.multihitBuff("Luna", True, 3, 5, 12)
    target.buffs_upd.append(Luna)
    

def basic_attack(*args):
    print("Did a Basic Attack!")
