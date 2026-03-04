import Memoria as mm
import SkillsList as slist
from collections import defaultdict

basic = mm.Skill("Basic", 0,0,"enemy",2,False, 1)
orbSPregen = mm.limitedskill("Skillful Means",1,False,"self",0,False, 0,1)
## Diva Ruka Implementation
ruka5 = mm.Memoria("Diva Ruka", LB=1)
ruka5s21 = mm.Skill("Luna", 7, True, "Single Ally", 0, False, 3)
ruka5s22 = mm.Skill("Luna EX", 7, True, "Single Ally", 0, False, 3)
ruka5ex = mm.limitedskill("Song To Shooting Stars", 14,True,"All Allies",0,False,5,4)
ruka5.equipmentSP = 3
ruka5.skills = [basic, ruka5s21, ruka5s22, ruka5ex,orbSPregen]

## Thunder Aoi Implementation
aoi2 = mm.Memoria("Maid Aoi", LB=1)
aoi1ex = mm.limitedskill("Angels Wings", 10, False, "self", 0, True, 3, 4)
aoi2ex = mm.limitedskill("Big PP Thunder Damage", 13, False,"enemy",3,False, 0, 4)

aoi2.skills = [basic,aoi1ex,aoi2ex,orbSPregen]
aoi2.equipmentSP = 3

print("Battle Start!\n")
# Set allies in battle - currently 1 Line, 2 allies
allies = [ruka5, aoi2]

#Check equipment for SP boosting at battle start
for x in allies:
    x.sp += x.equipmentSP
    if x.limitbreak > 0:
        x.spregenfl += 1

#List of all active skills, ative debuffs on enemies, and their durations
actskls_duration = {}
active_single_skills = defaultdict(dict)
debuffs_on_enemy = {}
activeskills = []
for i in range(10): ##10 rounds of simulated moves
    print("Round : " + str(i+1))

    #Countdown Active Skills and Buffs within said Skills
    for skills in actskls_duration:
        actskls_duration[skills] -= 1
    for ally in allies:
        copy = active_single_skills[ally].copy()
        for skill in copy:
            args = []
            args.append(ally)
            args.append(skill)
            args.append(0)
            args.append(active_single_skills)
            args = tuple(args)
            skillnamesearch = str.lower(skill.skillname).replace(' ','_')
            try:
                skilleffect = getattr(slist, skillnamesearch)
                skilleffect(*args)
            except:
                print("Skill has not been implemented yet")
    for skill in activeskills:
        args = []
        match skill.target:
            case "self":
                args.append(unit) #Can break if the self buff was not on the last unit!
                # Also same idea of implementation behind 1 char active buffs like Luna?
                # Also need to do something with Buff Usage?
            case "All Allies":
                args.append(allies)
        if skill.debuffs:
            args.append(debuffs_on_enemy)
        if skill.isactive:
            args.append(actskls_duration[skill.skillname])
        #print(args)
        args = tuple(args)
        skillnamesearch = str.lower(skill.skillname).replace(' ','_')
        try:
            skilleffect = getattr(slist, skillnamesearch)
            skilleffect(*args)
        except:
            print("Skill has not been implemented yet")
        if actskls_duration[skill.skillname] == 0:
            del actskls_duration[skill.skillname]
            activeskills.remove(skill)

    #Select to see buffs or take action
    
    for unit in allies:
        unit.sp = unit.sp + unit.spregenfl
        if unit.sp > 20:
            unit.sp = 20
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
                print("-------- Buffs on " + unit.name + " ------")
                for x in unit.buffs:
                    print(x + " : " + unit.buffs[x])
                print("------------------------------------")
            elif skillchoice <= len(unit.skills):
                skill = unit.skills[skillchoice-1]
                if unit.sp >= skill.spcost:
                    checksp = False
                else:
                    print("Not enough SP: use a different skill")
            else:
                print("Please make a valid selection")
        
        

        args = []
        match skill.target:
            case "self":
                args.append(unit)
            case "All Allies":
                args.append(allies)
            case "Single Ally":
                print("Please choose a target for the skill")
                for x in allies:
                    print(str(allies.index(x)) + ". " + x.name)
                targetchoice = input("Write number of selected character: ")
                targetchoice = int(targetchoice)
                target_ally = allies[targetchoice]
                args.append(target_ally)
        if skill.debuffs:
            args.append(debuffs_on_enemy)
        if skill.isactive:
            match skill.target:
                case "self":
                    args.append(skill)
                    args.append(1)
                    active_single_skills[unit][skill] = 1
                    args.append(active_single_skills)
                case "All Allies":
                    actskls_duration[skill.skillname] = skill.length
                    activeskills.append(skill)
                case "Single Ally":
                    args.append(skill)
                    args.append(1)
                    active_single_skills[target_ally][skill] = 1
                    args.append(active_single_skills)
            args.append(skill.length)
        #print(args)
        args = tuple(args)
        skillnamesearch = str.lower(skill.skillname).replace(' ','_')
        try:
            skilleffect = getattr(slist, skillnamesearch)
            skilleffect(*args)
            print("Used skill: " + str(skill.skillname))
        except:
            print("Skill has not been implemented yet")
        
        print("")
        unit.sp -= skill.spcost

