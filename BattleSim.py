import Classes as mm
import SkillsList as slist
import PassiveSkills as plist
import Memoria as collection
from collections import defaultdict

## Helper Funcitons ----------------------------------

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

## ----------------------------------------------------

## Import current Memoria collection from Memoria.py
memoriaCollection = collection.MMcollection()

print("Battle Start!\n")
# Set allies in battle - currently 1 Line, 2 allies
allies = memoriaCollection.collection
turn = 0
activeskills = []
Battlefield = mm.battlefield(allies, None, activeskills, turn)
#Check equipment for SP boosting at battle start
for x in allies:
    x.sp += x.equipmentSP
    

#List of all active skills, ative debuffs on enemies, and their durations
action_selection = defaultdict(dict)
debuffs_on_enemy = {}

for i in range(10): ##10 rounds of simulated moves
    Battlefield.turn += 1
    print("-------------------------------------------------------------------\n")
    print("Round : " + str(Battlefield.turn))

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
    
    ## Activate Passives HERE once buffs have done countdown before 'turn start'
    for unit in allies:
        for passive in unit.passives:
            activatePassive(passive, unit, Battlefield)

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
                    print(str(unit.skills.index(skills) + 1)+'. ' + skills.skillname + " - " + str(skillcost(skills, unit)) + " SP" + skill_uses)
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
                        if (unit.sp >= (skillcost(skill, unit))) and (skilllim_pass == True):
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
            unit.sp = unit.sp - (skillcost(skill, unit))

