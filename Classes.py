import typing
import types

class Skill:
    def __init__(self, Name : str, Cost: int, Active: bool, target: str, Hits: int, debuffs:bool, length: int):
        self.skillname = Name
        self.spcost = Cost
        self.isactive = Active
        self.target = target
        self.hits = Hits
        self.length = length
        self.debuffs = debuffs
    
    def print(self):
        print(self.skillname)

    def effect(self):
        print("There is no effect at the moment")

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

class attack(Skill):
    def __init__(self, Name, Cost, target, debuffs, Hits):
        super().__init__(Name, Cost, target, debuffs, Hits)

class limitedskill(Skill):
    def __init__(self, Name, Cost, Active, target, Hits, debuffs, length, Uses:int):
        super().__init__(Name, Cost, Active, target, Hits, debuffs, length)
        self.uselimit = Uses

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

class Buff:
    def __init__(self, name, active, length):
        self.name = name
        self.isActive = active
        self.length = length

class skill_atk_increase(Buff):
    def __init__(self, name, active, length, element, value):
        super().__init__(name, active, length)
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
    def __init__(self, name, active, length, element, value):
        super().__init__(name, active, length)
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
    def __init__(self, name, active, length, element, value):
        super().__init__(name, active, length)
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
    def __init__(self, name, active, length, hitcount, value_per_hit):
        super().__init__(name, active, length)
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
    def __init__(self, name, active, length, value):
        super().__init__(name, active, length)
        self.value = value
    
    def print(self):
        text = f"Incoming DMG reduced by {self.value}"
        if self.isActive:
            text = text + " for " + str(self.length) + " turns"
        else:
            text = text + f" ({self.length} uses)"
        print(text)

class unique_buff(Buff):
    def __init__(self, name, active, length):
        super().__init__(name, active, length)

    def print(self):
        text = f"{self.name} active"
        if self.isActive:
            text = text + " for " + str(self.length) + " turns"
        else:
            text = text + f" ({self.length} uses)"
        print(text) 

class battlefield():
    def __init__(self, allies, enemies, activeskills, turn):
        self.fl_allies = allies
        self.enemies = enemies
        self.fieldskills = activeskills
        self.turn = turn

class passiveSkill:
    def __init__(self, Name):
        self.name = Name
        self.description = str
