from Tower import *
from lib import *


class Cannon(Tower):
    def __init__(self, pos):
        super(Cannon, self).__init__(pos)

    def urlimg(self):
        return "./image/1_" + str(self.lvl) + "tour" + self.getSprite() + ".png"

    def getPo(self):
        return int(2 * 40 * exp(1.5, self.lvl - 1))

    def getDmg(self):
        return int(1 * exp(1.5, self.lvl - 1))

    def getCd(self):
        return int(1 * 33 * exp(0.75, self.lvl - 1))

    def getUpgradePrice(self):
        return int(1 * 150 * exp(1.5, self.lvl))

    def getSellValue(self):
        return int(1 * 75 * exp(1.5, self.lvl))
