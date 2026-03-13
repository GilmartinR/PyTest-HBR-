import Classes as mm
import SkillsList as slist
import PassiveSkills as plist
import Memoria as collection
from collections import defaultdict
from operator import itemgetter, attrgetter

def activatePassive(passive, unit, field):
    args = tuple([unit, field])
    skillnamesearch = str.lower(passive.name).replace(' ','_')
    try:
        paseffct = getattr(plist, skillnamesearch)
        paseffct(*args)
    except:
        print("Passive Skill has not been implemented yet")

def skillcost(skill, unit) -> int:
    cost = skill.spcost - unit.spreduction
    if cost<0:
        cost = 0
    return cost

def use_atk_buffs(unit, attack, field)->float: #returns a multiplier, uses limited amount buffs
    #select skill atk buffs first
    final_multiplier = 1
    select_neutral_atk_buffs = [buff for buff in unit.buffs_upd if ((buff.type=="skillatk") and (buff.element == "Neutral"))]
    sorted(select_neutral_atk_buffs, key=attrgetter('value'), reverse=True)
    sorted(select_neutral_atk_buffs, key=attrgetter('isActive'), reverse=True)
    select_multihit_buff = [buff for buff in unit.buffs_upd if ((buff.type=="multihit"))]
    sorted(select_multihit_buff, key=attrgetter('totalvalue'),reverse=True)
    sorted(select_multihit_buff, key=attrgetter('isActive'), reverse=True)
    #print(select_multihit_buff)
    try:
        if select_multihit_buff[0].isActive:
            final_multiplier *= ((select_multihit_buff[0].totalvalue + 100) / 100)
            
    except:
        pass
    print(f"Attack multiplier - {final_multiplier}")