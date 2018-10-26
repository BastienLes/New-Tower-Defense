from Sniper import *
from Cannon import *
from Monstre import *


class Game(object):
    def __init__(self, path, screen, startx, starty, startdir, gain):
        super(Game, self).__init__()
        self.towers = []
        self.monsters = []
        self.pathmap = path
        self.gold = 500
        self.vie = 20
        self.vague = 1
        self.screen = screen
        self.autowave = False
        self.startx = startx
        self.starty = starty
        self.startdir = startdir
        self.gain = gain

    def gainGold(self):
        self.gold += self.gain

    def setGain(self, goldparmob):
        self.gain = goldparmob

    def perteVie(self, degats):
        self.vie -= degats

    def mobHp(self):
        return self.vague // 2 + 5

    def mobNb(self):
        return self.vague // 3 + 3

    def setMobNb(self):
        for i in range(0, self.mobNb() - len(self.monsters)):
            self.monsters.append(Monstre(self))

    def addTower(self, tour):
        self.towers.append(tour)

    def addMonster(self, monstre):
        self.monsters.append(monstre)

    def addSniper(self, pos):
        self.towers.append(Sniper(pos))

    def addCannon(self, pos):
        self.towers.append(Cannon(pos))

    def upgrade(self, tour):
        if(self.gold >= tour.getUpgradePrice()):
            self.gold -= tour.getUpgradePrice()
            tour.lvlup()

    def sell(self, tour):
        for tower in self.towers:
            if tower == tour:
                self.gold += tour.getSellValue()
                self.towers.remove(tour)

    def distance(x, y, x2, y2):
        return abs(x2 - x) + abs(y2 - y)

    def moveMonsters(self):
        for i in range(0, len(self.monsters)):
            if (i == 0 or self.monsters[i - 1].mort or 40 <= distance(self.monsters[i].x, self.monsters[i].y, self.monsters[i - 1].x, self.monsters[i - 1].y)):
                self.monsters[i].move()

    def testRange(self, tower):
        for mon in self.monsters:
            if(not(mon.mort) and distance(mon.x, mon.y, tower.x, tower.y) <= tower.getPo()):
                return tower.shoot(mon)

    def towersTurn(self):
        for tour in self.towers:
            if(tour.actif):
                tour.play(self)

    def testEndWave(self):
        for mon in self.monsters:
            if (not(mon.mort)):
                return False
        return True

    def waveInit(self):
        self.setMobNb()
        x = self.startx
        y = self.starty
        hp = self.mobHp()
        direc = self.startdir
        for mon in self.monsters:
            mon.mort = False
            mon.x = x
            mon.y = y
            mon.vie = hp
            mon.dir = direc

    def nextWave(self):
        self.vague += 1
        self.waveInit()
        self.screen.decompte()
