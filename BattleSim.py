import Memoria as mm
import SkillsList as slist

basic = mm.Skill("Basic", 0,0,"enemy",2,1)
orbSPregen = mm.limitedskill("Skillful Means",1,False,"self",0,0,1)
## Diva Ruka Implementation
ruka5 = mm.Memoria("Diva Ruka", LB=1)
ruka5s21 = mm.multihitboost("Luna", 7, True, "Single Ally", 0, 3, 5)
ruka5s22 = mm.multihitboost("Luna EX", 7, True, "Single Ally", 0, 3, 3)
ruka5ex = mm.limitedskill("Song To Shooting Stars", 14,True,"All Allies",0,5,4)
ruka5.equipmentSP = 3
ruka5.skills = [basic, ruka5s21, ruka5s22, ruka5ex,orbSPregen]

## Thunder Aoi Implementation
aoi2 = mm.Memoria("Maid Aoi", LB=1)
aoi1ex = mm.limitedskill("Angel's Wings", 10, False, "self", 0, 0, 4)
aoi2ex = mm.limitedskill("Big PP Thunder Damage", 13, False,"enemy",3,0,4)

aoi2.skills = [basic,aoi1ex,aoi2ex,orbSPregen]
aoi2.equipmentSP = 3

print("Battle Start!\n")
allies = [ruka5, aoi2]
for x in allies:
    x.sp += x.equipmentSP
    if x.limitbreak > 0:
        x.spregenfl += 1
actskls_duration = {}
activeskills = []
for i in range(10): ##10 rounds of simulated moves
    print("Round : " + str(i+1))

    #Countdown Active Skills and Buffs within said Skills
    for skills in actskls_duration:
        actskls_duration[skills] -= 1
    for skill in activeskills:
        if skill.target == "self":
            skillnamesearch = str.lower(skill.skillname).replace(' ','_')
            skilleffect = getattr(slist, skillnamesearch)
            skilleffect(unit, actskls_duration[skill.skillname])
        if skill.target == "All Allies":
            skillnamesearch = str.lower(skill.skillname).replace(' ','_')
            skilleffect = getattr(slist, skillnamesearch)
            skilleffect(allies, actskls_duration[skill.skillname])
        if actskls_duration[skill.skillname] == 0:
            del actskls_duration[skill.skillname]
            activeskills.remove(skill)

    #Select to see buffs or take action
    
    for unit in allies:
        unit.sp = unit.sp + unit.spregenfl
        print("Current sp on " + unit.name + " is " + str(unit.sp))
        checksp = True
        print("Available skills on " + unit.name + ": ")
        print("0. Check Current Buffs")
        for skills in unit.skills:
            print(str(unit.skills.index(skills) + 1)+'. ' + skills.skillname + " - " + str(skills.spcost) + " SP")
        while checksp:
            skillchoice = input("Choose which skill to use: ")
            skillchoice = int(skillchoice)
            if skillchoice == 0:
                for x in unit.buffs:
                    print(x + " : " + unit.buffs[x])
            elif skillchoice <= len(unit.skills):
                skill = unit.skills[skillchoice-1]
                if unit.sp >= skill.spcost:
                    checksp = False
                else:
                    print("Not enough SP: use a different skill")
            else:
                print("Please make a valid selection")
        
        print("Used skill: " + str(skill.skillname))
        if skill.isactive:
            actskls_duration[skill.skillname] = skill.length
            activeskills.append(skill)
        if skill.target == "self":
            skillnamesearch = str.lower(skill.skillname).replace(' ','_')
            skilleffect = getattr(slist, skillnamesearch)
            skilleffect(unit)
        if skill.target == "All Allies":
            skillnamesearch = str.lower(skill.skillname).replace(' ','_')
            skilleffect = getattr(slist, skillnamesearch)
            skilleffect(allies, skill.length)
        print("")
        unit.sp -= skill.spcost

    
