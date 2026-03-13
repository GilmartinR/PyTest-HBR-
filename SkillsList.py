import Classes as cl


def skillful_means(*args):
    #print(args)
    memor = args[0]
    memor.sp += 3
    print("Increased own SP by 3")

def song_to_shooting_stars(*args):
    allies = args[0]
    for ally in allies:
        CritRate = cl.crit_rate_buff("Crit Rate Up - Songstress Blessing", "critrate", True, 5, None, 100)
        CritDmg = cl.crit_dmg_buff("Crit DMG Up - Songstress Blessing", "critdmg", True, 5, None, 90)
        SongBless = cl.unique_buff("Songstress' Blessing","unique", True, 5)
        ally.buffs_upd.append(CritRate)
        ally.buffs_upd.append(CritDmg)
        ally.buffs_upd.append(SongBless)

def angels_wings(*args):
    memor = args[0]
    AngelWings = cl.dmg_reduction_buff("Angel's Wings","dmgreduction", False, 2, 100)
    memor.buffs_upd.append(AngelWings)
    print("Angel's Wings is active - Enemy provoked for 3 turns")

def luna(*args):
    ruka = args[0]
    target = args[1]
    has_songstress = False
    for buff in ruka.buffs_upd:
        if buff.name == "Songstress' Blessing":
            has_songstress = True
    if has_songstress:
        Luna = cl.multihitBuff("Luna","multihit", True, 3, 3, 40)
    else:
        Luna = cl.multihitBuff("Luna","multihit", True, 3, 5, 12)
    target.buffs_upd.append(Luna)
    

def basic_attack(*args):
    print("Did a Basic Attack!")

def sea_breeze_high_voltage(*args):
    unit = args[0]
    field = args[1]
    target = args[2] #Need to implement enemies
    SeaBreeze = cl.field_buff("Sea Breeze Thunder Field","field", True, 8, "Thunder", 65)
    for buff in unit.buffs_upd:
        if buff.name == "Meditation":
            SeaBreeze.value += 15
            SeaBreeze.isActive = False
            break 
    field.fieldskills.clear()
    field.fieldskills.append(SeaBreeze)

