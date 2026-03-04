import typing
import types

class Skill:
    def __init__(self, Name : str, Cost: int, Active: bool, target: str, Hits: int, length: int):
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

class multihitboost(Skill):
    def __init__(self, Name, Cost, Active, target, Hits, length, multihitboost: int):
        super().__init__(Name, Cost, Active, target, Hits, length)
        self.multihitboost = multihitboost

class attack(Skill):
    def __init__(self, Name, Cost, target, Hits):
        super().__init__(Name, Cost, target, Hits)

class spboostskill(Skill):
    def __init__(self, Name, Cost, Active, target, length):
        super().__init__(Name, Cost, Active, target, length)

class limitedskill(Skill):
    def __init__(self, Name, Cost, Active, target, Hits, length, Uses:int):
        super().__init__(Name, Cost, Active, target, Hits, length)
        self.uselimit = Uses

