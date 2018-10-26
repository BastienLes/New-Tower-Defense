from Tower import *
from lib import *


class Sniper(Tower):
    def __init__(self, pos):
        super(Sniper, self).__init__(pos)

    def urlimg(self):
        return "./image/2_" + str(self.lvl) + "tour" + self.getSprite() + ".png"

    def getPo(self):
        return int(4 * 40 * exp(1.5, self.lvl - 1))

    def getDmg(self):
        return int(2 * exp(1.5, self.lvl - 1))

    def getCd(self):
        return int(2 * 33 * exp(0.75, self.lvl - 1))

    def getUpgradePrice(self):
        return int(2 * 150 * exp(1.5, self.lvl))

    def getSellValue(self):
        return int(2 * 75 * exp(1.5, self.lvl))
