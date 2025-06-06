import random

class Player:
    #Class Attributes
    def __init__(self):
        #Self Stat
        self.maxHP: int = 3687106 #Dummy value, taken from 3.4 HSR MoC 12 Svarog
        self.currHP: int = self.maxHP #Starting HP is equal to max HP
        self.SP: int = 10 #Starting SP is 10/20
        self.DEF: int = 1100 #Base DEF from lvl 95 enemy in HSR

        #Combat Modifier
        self.CRITRate: float = 0.05 #5% starting CRIT Rate
        self.CRITDMG: float = 0.5 #50% starting CRIT DMG
        self.DMGDealt: float = 0.0 #0% starting DMG Dealt Multiplier

        #Debuff
        self.vulnerability: float = 0.0 #0% Starting Vulnerability Multiplier

    #Called by the receiving attack's player, honestly doesn't matter since we have both player in parameter anyways
    def takeDMG(self, attacker, baseDMG):
        #CRIT Check
        calcCRIT: bool
        if random.random() <= attacker.CRITRate:
            calcCRIT = True
        else:
            calcCRIT = False

        #Don't mind the long formula, I prefer this so less variable
        #If CRIT
        if calcCRIT:
            DMGTaken: int = baseDMG * (1 + attacker.DMGDealt) * (1 + attacker.CRITDMG) * (1 + self.vulnerability) * (1 - self.DEF/(self.DEF+1000)) * random.uniform(0.9, 1.1)
        #Not CRIT
        else:
            DMGTaken: int = baseDMG * (1 + attacker.DMGDealt) * (1 + self.vulnerability) * (1 - self.DEF/(self.DEF+1000)) * random.uniform(0.9, 1.1)

        #DMG Calc done, apply to self
        self.currHP -= DMGTaken

        #Remove buffs from Attacker after attacking
        attacker.CRITRate = 0.05
        attacker.CRITDMG = 0.5
        attacker.DMGDealt = 0.0

        #Remove debuff from self
        self.vulnerability = 0.0
        self.DEF = 1100

    #Call this at the start of player turn
    def turnStart(self):
        self.SP += 3 #Gain 3 SP per turn

        #Max SP is 20
        if self.SP >= 20:
            self.SP = 20

    #If use healing
    def heal(self, baseDMG):
        self.currHP += baseDMG

        #Prevent Overheal
        if self.currHP > self.maxHP:
            self.currHP = self.maxHP

    #If got Vulnerabiluity
    def applyVulnerability(self, baseDMG):
        self.vulnerability += baseDMG

    def applyDEFDown(self, baseDMG):
        self.DEF -= baseDMG * 1100

        #Prevent Negative (since that would heal if receiving attacks I think? lol)
        if(self.DEF < 0):
            self.DEF = 0