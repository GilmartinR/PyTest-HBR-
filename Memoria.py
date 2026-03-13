import Classes as mm
import SkillsList as slist
import PassiveSkills as plist



## Global Passives
InspiringSpark = mm.passiveSkill("Inspiring Spark")
## Personal Passives
Resonance = mm.passiveSkill("Resonance")
BlueSky = mm.passiveSkill("Blue Sky")
CooperativeSpirit = mm.passiveSkill("Cooperative Spirit")

basic = mm.Skill("Basic Attack", 0,0,"enemy",2,False, 1)
orbSPregenAoi = mm.limitedskill("Skillful Means",1,False,"self",0,False, 0,1)
orbSPregenRuka = mm.limitedskill("Skillful Means",1,False,"self",0,False, 0,1)
## Diva Ruka Implementation
ruka5 = mm.Memoria("Diva Ruka", LB=1)
ruka5s21 = mm.Skill("Luna", 7, True, "Single Ally", 0, False, 3)
ruka5s22 = mm.Skill("Luna EX", 7, True, "Single Ally", 0, False, 3)
ruka5ex = mm.limitedskill("Song To Shooting Stars", 14,True,"All Allies",0,False,5,4)
ruka5.equipmentSP = 3
ruka5.skills = [basic, ruka5s21, ruka5s22, ruka5ex,orbSPregenRuka]
ruka5.passives = [InspiringSpark, Resonance]

## Thunder Aoi Implementation
aoi2 = mm.Memoria("Maid Aoi", LB=1)
aoi1ex = mm.limitedskill("Angels Wings", 10, False, "self", 0, True, 3, 4)
aoi2ex = mm.limitedskill("Big PP Thunder Damage", 13, False,"enemy",3,False, 0, 4)

aoi2.skills = [basic,aoi1ex,aoi2ex,orbSPregenAoi]
aoi2.passives = [InspiringSpark, CooperativeSpirit, BlueSky]
aoi2.equipmentSP = 3

class MMcollection:
    def __init__(self):
        self.collection = [ruka5, aoi2]