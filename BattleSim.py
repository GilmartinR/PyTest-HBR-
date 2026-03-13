import Classes as mm
import SkillsList as slist
import PassiveSkills as plist
import Memoria as collection
from collections import defaultdict
import HelperFunctions as hf

## Helper Funcitons ----------------------------------


## ----------------------------------------------------

## Import current Memoria collection from Memoria.py
memoriaCollection = collection.MMcollection()

print("Battle Start!\n")
# Set allies in battle - currently 1 Line, 2 allies
allies = memoriaCollection.collection
turn = 0
field_buffs = []
Battlefield = mm.battlefield(allies, None, field_buffs, turn)
#Check equipment for SP boosting at battle start
for x in allies:
    x.sp += x.equipmentSP
    

#List of all active skills, ative debuffs on enemies, and their durations
action_selection = defaultdict(dict)

for i in range(10): ##10 rounds of simulated moves
    Battlefield.turn += 1
    print("-------------------------------------------------------------------\n")
    print("Round : " + str(Battlefield.turn))

    #Countdown Active Skills and Buffs within said Skills
    for ally in allies:
        for buff in ally.buffs_upd:
            if buff.isActive:
                buff.length -= 1
                #print(f"reduced length of {buff.name} by 1")
        for buff in ally.buffs_upd:
            if buff.length == 0:
                ally.buffs_upd.remove(buff)
    for fieldbuff in Battlefield.fieldskills:
        if fieldbuff.isActive:
            fieldbuff.length -= 1
        fieldbuff.print()
        if fieldbuff.length == 0:
            Battlefield.fieldskills.remove(fieldbuff)
    choice_made = False
    
    ## Activate Passives HERE once buffs have done countdown before 'turn start'
    for unit in allies:
        for passive in unit.passives:
            hf.activatePassive(passive, unit, Battlefield)

    for unit in allies:
        copyact = action_selection[unit].copy()
        for skill in copyact:
            action_selection[unit].pop(skill)
        action_selection[unit][unit.skills[0]] = ["enemy"]
        for key in unit.spboosts:
            unit.sp += unit.spboosts[key]
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
                    print(str(unit.skills.index(skills) + 1)+'. ' + skills.skillname + " - " + str(hf.skillcost(skills, unit)) + " SP" + skill_uses)
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
                        if (unit.sp >= (hf.skillcost(skill, unit))) and (skilllim_pass == True):
                            checksp = False
                            copyact = action_selection[unit].copy()
                            for x in copyact:
                                action_selection[unit].pop(x)
                            #add target selection
                            action_selection[unit][skill] = []
                            for target in skill.target:
                                #print(target)
                                match target:
                                    case 'self':
                                        action_selection[unit][skill].append(unit)
                                    case "All Allies":
                                        action_selection[unit][skill].append(allies)
                                    case 'Single Ally':
                                        print("Please choose a target for the skill")
                                        for x in allies:
                                            print(str(allies.index(x)+1) + ". " + x.name)
                                        targetchoice = input("Write number of selected character: ")
                                        targetchoice = int(targetchoice)-1
                                        target_ally = allies[targetchoice]
                                        action_selection[unit][skill].append(target_ally)
                                        print("Target is - " + target_ally.name)
                                    case "field":
                                        action_selection[unit][skill].append(Battlefield)
                                    case "enemy":
                                        action_selection[unit][skill].append("enemy")
                            
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
            for target in skill.target:
                match target:
                    case "self":
                        args.append(unit)
                    case "All Allies":
                        args.append(allies)
                    case "Single Ally":
                        args.append(action_selection[unit][skill][skill.target.index(target)])
                    case "field":
                        args.append(Battlefield)
                    case "enemy":
                        args.append(action_selection[unit][skill][skill.target.index(target)])
                        hf.use_atk_buffs(unit, skill, Battlefield)
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
            unit.sp = unit.sp - (hf.skillcost(skill, unit))

