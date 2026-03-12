import Memoria as mm
import SkillsList as slist
from collections import defaultdict


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

## Thunder Aoi Implementation
aoi2 = mm.Memoria("Maid Aoi", LB=1)
aoi1ex = mm.limitedskill("Angels Wings", 10, False, "self", 0, True, 3, 4)
aoi2ex = mm.limitedskill("Big PP Thunder Damage", 13, False,"enemy",3,False, 0, 4)

aoi2.skills = [basic,aoi1ex,aoi2ex,orbSPregenAoi]
aoi2.equipmentSP = 3

## 

print("Battle Start!\n")
# Set allies in battle - currently 1 Line, 2 allies
allies = [ruka5, aoi2]

#Check equipment for SP boosting at battle start
for x in allies:
    x.sp += x.equipmentSP
    if x.limitbreak > 0:
        x.spregenfl += 1

#List of all active skills, ative debuffs on enemies, and their durations
action_selection = defaultdict(dict)
debuffs_on_enemy = {}
activeskills = []
for i in range(10): ##10 rounds of simulated moves
    print("-------------------------------------------------------------------\n")
    print("Round : " + str(i+1))

    #Countdown Active Skills and Buffs within said Skills
    for skill in activeskills:
        skill.length -= 1
        if skill.length == 0:
            activeskills.remove(skill)
    for ally in allies:
        for buff in ally.buffs_upd:
            if buff.isActive:
                buff.length -= 1
            if buff.length == 0:
                ally.buffs_upd.remove(buff)
    choice_made = False
    
    for unit in allies:
        copyact = action_selection[unit].copy()
        for skill in copyact:
            action_selection[unit].pop(skill)
        action_selection[unit][unit.skills[0]] = ["enemy"]
        unit.sp = unit.sp + unit.spregenfl
        if unit.sp > 20:
            unit.sp = 20

    valid_input = False
    while not choice_made:
            print("Current unit actions:")
            for unit in allies:
                for skill_choice in action_selection[unit]:
                    try:
                        skill_uses = " : " + str(skill_choice.uselimit) + " uses left"
                    except:
                        skill_uses = ""
                    print(str(allies.index(unit) + 1)+". " + unit.name + " ("+str(unit.sp)+" SP) - " + skill_choice.skillname + skill_uses)
            print(str(len(allies)+1) + ". Swap Characters")
            print(str(len(allies)+2) + ". Confirm choices")
            choice = input("Select a character to take action, swap characters or confirm choice: ")
            print("")
            choice = int(choice) - 1
            if (choice > len(allies)) or (choice < 0):
                pass
                #invalid choice
            elif choice < len(allies):
                unit = allies[choice]
                print("Current sp on " + unit.name + " is " + str(unit.sp))
                checksp = True
                print("Available skills on " + unit.name + ": ")
                print("0. Check Current Buffs")
                for skills in unit.skills:
                    try:
                        skill_uses = " : " + str(skills.uselimit) + " uses left"
                    except:
                        skill_uses = ""
                    print(str(unit.skills.index(skills) + 1)+'. ' + skills.skillname + " - " + str(skills.spcost) + " SP" + skill_uses)
                while checksp:
                    skillchoice = input("Choose which skill to use: ")
                    skillchoice = int(skillchoice)
                    
                    if skillchoice == 0: ## Print Unit Buffs
                        print("-------- Buffs on " + unit.name + " ------")
                        for buff in unit.buffs_upd:
                            buff.print()
                        print("------------------------------------")

                    elif skillchoice <= len(unit.skills): ## Attempt to select skill
                        skill = unit.skills[skillchoice-1]
                        skilllim_pass = True
                        try:
                            if skill.uselimit == 0:
                                skilllim_pass = False                                
                        except:
                            pass
                        if (unit.sp >= skill.spcost) and (skilllim_pass == True):
                            checksp = False
                            copyact = action_selection[unit].copy()
                            for x in copyact:
                                action_selection[unit].pop(x)
                            #add target selection
                            match skill.target:
                                case "self":
                                    action_selection[unit][skill] = unit
                                case "All Allies":
                                    action_selection[unit][skill] = allies
                                case "Single Ally":
                                    print("Please choose a target for the skill")
                                    for x in allies:
                                        print(str(allies.index(x)) + ". " + x.name)
                                    targetchoice = input("Write number of selected character: ")
                                    targetchoice = int(targetchoice)
                                    target_ally = allies[targetchoice]
                                    action_selection[unit][skill] = target_ally
                                    print("Target is - " + target_ally.name)
                                case "enemy":
                                    action_selection[unit][skill] = "enemy"
                            valid_input = True
                        else:
                            print("Not enough SP or uses remaining: use a different skill")
                    else:
                        print("Please make a valid selection")
                print("")

            if choice == len(allies): ## Choose to swap allies
                print("Please choose an ally")
                for x in allies:
                    print(str(allies.index(x)+1) + ". " + x.name)
                x = input("Write number of selected ally: ")
                x = int(x)-1
                targetchoice = input("Write number of selected ally to swap unit with: ")
                targetchoice = int(targetchoice)-1
                target_ally = allies[targetchoice]
                unit = allies[x]
                allies[x], allies[targetchoice] = target_ally, unit
                print("")
            
            if choice == (len(allies) + 1): ## Confirm Choices
                choice_made = True

    ## ACTIVATING SKILLS

    for unit in allies:
        args = []
        for skill in action_selection[unit]:
            try:
                if skill.uselimit > 0:
                    skill.uselimit -=1                               
            except:
                pass
            match skill.target:
                case "self":
                    args.append(unit)
                case "All Allies":
                    args.append(allies)
                case "Single Ally":
                    args.append(action_selection[unit][skill])
                case "Field":
                    args.append[activeskills]
            if skill.debuffs:
                args.append(debuffs_on_enemy)
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

