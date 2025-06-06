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
        self.poison: bool = False #Start not poisoned
        self.vulnerability: float = 0.0 #0% Starting Vulnerability Multiplier

    #Called by the receiving attack's player, honestly doesn't matter since we have both player in parameter anyways
    def takeDMG(self, attacker, baseDMG):
        #CRIT Check
        calcCRIT: bool
        if random.randrange(0, 1) <= attacker.CRITRate:
            calcCRIT = True
        else:
            calcCRIT = False

        #Don't mind the long formula, I prefer this so less variable
        #If CRIT
        if calcCRIT:
            DMGTaken: int = baseDMG * (1 + attacker.DMGDealt) * (1 + attacker.CRITDMG) * (1 + self.vulnerability) * (1 - self.DEF/(self.DEF+1000)) * random.randrange(0.9, 1.1)
        #Not CRIT
        else:
            DMGTaken: int = baseDMG * (1 + attacker.DMGDealt) * (1 + self.vulnerability) * (1 - self.DEF/(self.DEF+1000)) * random.randrange(0.9, 1.1)

        #DMG Calc done, apply to self
        self.currHP -= DMGTaken

        #If got poison
        if self.poison:
            self.currHP -= 0.1 * self.maxHP