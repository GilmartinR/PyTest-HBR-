def inspiring_spark(*args):
    unit = args[0]
    field = args[1]
    if unit in field.fl_allies:
        unit.spboosts["Inspiring Spark"] = 1
    else:
        unit.spboosts["Inspiring Spark"] = 0

def resonance(*args):
    unit = args[0]
    field = args[1]
    for buff in unit.buffs_upd:
        if buff.name == "Songstress' Blessing":
            for fl_ally in field.fl_allies:
                fl_ally.spboosts["Songstress' Blessing"] = 2
            return
    for fl_ally in field.fl_allies:
                fl_ally.spboosts["Songstress' Blessing"] = 0
            
def blue_sky(*args):
    unit = args[0]
    field = args[1]
    if field.turn == 1:
         for ally in field.fl_allies:
              ally.spreduction += 1

def cooperative_spirit(*args):
    unit = args[0]
    field = args[1]
    if field.turn == 1:
        for ally in field.fl_allies:
            for skill in ally.skills:
                try:
                    skill.uselimit += 1
                except:
                    pass

def _(*args):
    unit = args[0]
    field = args[1]

def _(*args):
    unit = args[0]
    field = args[1]

def _(*args):
    unit = args[0]
    field = args[1]

def _(*args):
    unit = args[0]
    field = args[1]
def _(*args):
    unit = args[0]
    field = args[1]