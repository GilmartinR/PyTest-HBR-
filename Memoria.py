import Classes as mm
import SkillsList as slist
import PassiveSkills as plist



## Global Passives
InspiringSpark = mm.passiveSkill("Inspiring Spark")
## Personal Passives
Resonance = mm.passiveSkill("Resonance")
BlueSky = mm.passiveSkill("Blue Sky")
CooperativeSpirit = mm.passiveSkill("Cooperative Spirit")
Meditation = mm.passiveSkill("Meditation")

## Basic Attacks, Skillfull means
basic = mm.attack("Basic Attack", 0,["enemy"],2, "Neutral")
orbSPregenAoi = mm.limitedskill("Skillful Means",1,False,["self"],0, 0,1)
orbSPregenRuka = mm.limitedskill("Skillful Means",1,False,["self"],0, 0,1)
orbSPregenMegumi = mm.limitedskill("Skillful Means",1,False,["self"],0, 0,1)
## Diva Ruka Implementation
ruka5 = mm.Memoria("Diva Ruka", LB=1)
luna = mm.Skill("Luna", 7, True, ["self","Single Ally"], 0, 3)
ruka5ex = mm.limitedskill("Song To Shooting Stars", 14,True,["All Allies"],0,5,4)
ruka5.equipmentSP = 3
ruka5.skills = [basic, luna, ruka5ex,orbSPregenRuka]
ruka5.passives = [InspiringSpark, Resonance]

## Thunder Aoi Implementation
aoi2 = mm.Memoria("Maid Aoi", LB=1)
aoi1ex = mm.limitedskill("Angels Wings", 10, False, ["self"], 0, 3, 4)
aoi2ex = mm.limitedAttack("Big PP Thunder Damage", 13,["self","enemy"],3, "Thunder", 4)

aoi2.skills = [basic,aoi1ex,aoi2ex,orbSPregenAoi]
aoi2.passives = [InspiringSpark, CooperativeSpirit, BlueSky]
aoi2.equipmentSP = 3

## Thunder Megumi
megumi5 = mm.Memoria("Thunder Megumi", LB=1)
megumi5ex = mm.limitedAttack("Sea Breeze High Voltage", 14, ["self", "field", "enemy"], 3, "Thunder", 4)
HardKnocks = mm.attack("Hard Knocks", 8, ["enemy"], 2, "Neutral")
megumi5.skills = [basic, HardKnocks, megumi5ex, orbSPregenMegumi]
megumi5.passives = [InspiringSpark, Meditation] #
megumi5.equipmentSP = 10


class MMcollection:
    def __init__(self):
        self.collection = [ruka5, aoi2, megumi5]