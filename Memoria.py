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
        self.buffs = {}
        self.debuffs = {}

    def print(self):
        print(self.name)

class attack(Skill):
    def __init__(self, Name, Cost, target, debuffs, Hits):
        super().__init__(Name, Cost, target, debuffs, Hits)

class limitedskill(Skill):
    def __init__(self, Name, Cost, Active, target, Hits, debuffs, length, Uses:int):
        super().__init__(Name, Cost, Active, target, Hits, debuffs, length)
        self.uselimit = Uses

