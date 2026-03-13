import typing
import types

class Skill:
    def __init__(self, Name : str, Cost: int, Active: bool, target: list, Hits: int, length: int):
        self.skillname = Name
        self.spcost = Cost
        self.isactive = Active
        self.target = target
        self.hits = Hits
        self.length = length
    
    def print(self):
        print(self.skillname)

    def effect(self):
        print("There is no effect at the moment")

class attack:
    def __init__(self, Name, Cost, Target, Hits, Element):
        self.skillname = Name
        self.spcost = Cost
        self.target = Target
        self.hits = Hits
        self.element = Element

class limitedskill(Skill):
    def __init__(self, Name, Cost, Active, target, Hits, length, Uses:int):
        super().__init__(Name, Cost, Active, target, Hits, length)
        self.uselimit = Uses

class limitedAttack(attack):
    def __init__(self, Name, Cost, Target, Hits, Element, Uses:int):
        super().__init__(Name, Cost, Target, Hits, Element)
        self.uselimit = Uses

## BUFFS

class Buff:
    def __init__(self, name, active, length, type:str):
        self.name = name
        self.isActive = active
        self.length = length
        self.type = type

class skill_atk_increase(Buff):
    def __init__(self, name, type, active, length, element, value):
        super().__init__(name, active, length, type)
        self.element = element
        self.value = value
    
    def print(self):
        text = ""
        if self.element is not None:
            text = text + self.element + " "
        text = text + "Skill Atk increased by " + str(self.value) + "%"
        if self.isActive:
            text = text + " for " + str(self.length) + " turns"
        else:
            text = text + f" ({self.length} uses)"
        print(text)
        
class crit_rate_buff(Buff):
    def __init__(self, name, type, active, length, element, value):
        super().__init__(name, active, length, type)
        self.element = element
        self.value = value
    
    def print(self):
        text = ""
        if self.element is not None:
            text = text + self.element + " "
        text = text + "Crit Rate increased by " + str(self.value) + "%"
        if self.isActive:
            text = text + " for " + str(self.length) + " turns"
        else:
            text = text + f" ({self.length} uses)"
        print(text)

class crit_dmg_buff(Buff):
    def __init__(self, name, type, active, length, element, value):
        super().__init__(name, active, length, type)
        self.element = element
        self.value = value
    
    def print(self):
        text = ""
        if self.element is not None:
            text = text + self.element + " "
        text = text + "Crit DMG increased by " + str(self.value) + "%"
        if self.isActive:
            text = text + " for " + str(self.length) + " turns"
        else:
            text = text + f" ({self.length} uses)"
        print(text)

class multihitBuff(Buff):
    def __init__(self, name, type, active, length, hitcount, value_per_hit):
        super().__init__(name, active, length, type)
        self.hitcount = hitcount
        self.value_per_hit = value_per_hit
        self.totalvalue = self.hitcount * self.value_per_hit

    def __gt__(self, other):
        return self.totalvalue >= other.totalvalue
    def __eq__(self, other):
        return self.totalvalue == other.totalvalue
    
    def print(self):
        text = ""
        text = text + "Multihit increased by " + str(self.hitcount) + "x"+str(self.value_per_hit)
        if self.isActive:
            text = text + " for " + str(self.length) + " turns"
        else:
            text = text + f" ({self.length} uses)"
        print(text)

class dmg_reduction_buff(Buff):
    def __init__(self, type, name, active, length, value):
        super().__init__(name, type, active, length)
        self.value = value
    
    def print(self):
        text = f"Incoming DMG reduced by {self.value}"
        if self.isActive:
            text = text + " for " + str(self.length) + " turns"
        else:
            text = text + f" ({self.length} uses)"
        print(text)

class unique_buff(Buff):
    def __init__(self, type, name, active, length):
        super().__init__(name, type, active, length)

    def print(self):
        text = f"{self.name} active"
        if self.isActive:
            text = text + " for " + str(self.length) + " turns"
        else:
            text = text + f" ({self.length} uses)"
        print(text) 

class field_buff(Buff):
    def __init__(self, type, name, active, length, element, value):
        super().__init__(name, type, active, length)
        self.element = element
        self.value = value
    
    def print(self):
        text = f"{self.name} active"
        text += f" - {self.element} DMG increased by {self.value}"
        if self.isActive:
            text = text + " for " + str(self.length) + " turns"
        else:
            text = text + " (Indefinite)"
        print(text) 

## Random

class battlefield():
    def __init__(self, allies, enemies, field_buffs, turn):
        self.fl_allies = allies
        self.enemies = enemies
        self.fieldskills = field_buffs
        self.turn = turn

class Enemy:
    def __init__(self, Name: str, DP: int, HP: int):
        self.name = Name
        self.debuffs = []
        self.dp = DP
        self.hp = HP
        self.skills = []
        self.skills_pattern = []
        self.resistances = []
    
    def print(self):
        print(self.name)

class passiveSkill:
    def __init__(self, Name):
        self.name = Name
        self.description = str

class Memoria:
    def __init__(self, Name: str, LB: int):
        self.name = Name
        self.limitbreak = LB
        self.spreduction = 0
        self.skills = []
        self.hitboost = 0
        self.spregenfl = 2
        self.spregenbl = 2
        self.sp = 1
        self.totems = 0
        self.equipmentSP = 0
        self.buffs_upd = []
        self.debuffs = []
        self.passives = []
        self.spboosts = {}

    def print(self):
        print(self.name)

## DEBUFFS

class Debuff:
    def __init__(self, name, active, length, type:str):
        self.name = name
        self.isActive = active
        self.length = length
        self.type = type
    
class def_debuff(Debuff):
    def __init__(self, name, active, length, element, value, type):
        super().__init__(name, active, length, type)
        self.element = element
        self.value = value
    
    def print(self):
        text = ""
        if self.element is not None:
            text = text + self.element + " "
        text = text + "DEF decreased by " + str(self.value) + "%"
        if self.isActive:
            text = text + " for " + str(self.length) + " turns"
        else:
            text = text + f" ({self.length} uses)"
        print(text)