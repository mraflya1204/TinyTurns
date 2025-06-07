import random

class Player:
    #Class Attributes
    def __init__(self):
        #Self Stat
        self.maxHP: int = 3687106 #Dummy value, taken from 3.4 HSR MoC 12 Svarog
        self.currHP: int = self.maxHP #Starting HP is equal to max HP
        self.ATK: int = 3000 #Starting ATK at 1000
        self.SP: int = 10 #Starting SP is 10/20
        self.DEF: int = 1100 #Base DEF from lvl 95 enemy in HSR

        #Combat Modifier
        self.CRITRate: float = 0.05 #5% starting CRIT Rate
        self.CRITDMG: float = 0.5 #50% starting CRIT DMG
        self.DMGDealt: float = 0.0 #0% starting DMG Dealt Multiplier

        #Debuff
        self.vulnerability: float = 0.0 #0% Starting Vulnerability Multiplier

    #Called by the receiving attack's player, honestly doesn't matter since we have both player in parameter anyways
    def takeDMG(self, attacker, baseMultiplier):
        #CRIT Check
        calcCRIT: bool
        if random.random() <= attacker.CRITRate:
            calcCRIT = True
        else:
            calcCRIT = False

        #Don't mind the long formula, I prefer this so less variable
        #If CRIT
        if calcCRIT:
            DMGTaken: int = baseMultiplier * self.ATK * (1 + attacker.DMGDealt) * (1 + attacker.CRITDMG) * (1 + self.vulnerability) * (1 - self.DEF/(self.DEF+1000)) * random.uniform(0.9, 1.1)
        #Not CRIT
        else:
            DMGTaken: int = baseMultiplier * self.ATK * (1 + attacker.DMGDealt) * (1 + self.vulnerability) * (1 - self.DEF/(self.DEF+1000)) * random.uniform(0.9, 1.1)

        #DMG Calc done, apply to self
        self.currHP -= DMGTaken

        #Remove buffs from Attacker after attacking
        attacker.ATK = 3000
        attacker.CRITRate = 0.05
        attacker.CRITDMG = 0.5
        attacker.DMGDealt = 0.0

        #Remove debuff from self
        self.vulnerability = 0.0
        self.DEF = 1100

        #So I can see the DMG Number
        return int(DMGTaken)

    #Call this at the start of player turn
    def turnEnd(self):
        self.SP += 3 #Gain 3 SP per turn

        #Max SP is 20
        if self.SP >= 20:
            self.SP = 20

    #Call for CRIT Buff command
    def CRITBuff(self):
        self.CRITRate += 0.5
        self.CRITDMG += 0.5

    #Call for Enhancement command
    def enchancement(self):
        self.DMGDealt += 0.5
        self.ATK += 0.9 * self.ATK

    def debuff(self):
        self.vulnerability += 0.5
        self.DEF -= 0.5 * 1100
        if self.DEF <= 0:
            self.DEF = 0