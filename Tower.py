class Tower(object):
    def __init__(self, pos):
        super(Tower, self).__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.lvl = 1
        self.actif = True
        self.etat = self.getCd()

    def urlimg(self):
        raise NotImplementedError('subclasses must override afficher(self)!')

    def getOrigin(self):
        return (self.x - 15, self.y - 15)

    def getCenter(self):
        return (self.x, self.y)

    def getPo(self):
        raise NotImplementedError('subclasses must override afficher(self)!')

    def getDmg(self):
        raise NotImplementedError('subclasses must override afficher(self)!')

    def getCd(self):
        raise NotImplementedError('subclasses must override afficher(self)!')

    def lvlup(self):
        if(self.lvl < 3):
            self.lvl += 1
            self.etat = self.getCd()

    def getSprite(self):
        if (self.etat == self.getCd()):
            return '_ready'
        return str(28 * self.etat // self.getCd())

    def action(self):
        if (self.etat >= self.getCd()):
            self.shoot()
        else:
            self.etat += 1

    def shoot(self, monstre):
        monstre.perteHp(self.getDmg())
        self.etat = 0

    def play(self, game):
        if(self.etat == self.getCd()):
            game.testRange(self)
        else:
            self.action()

    def getUpgradePrice(self, game):
        raise NotImplementedError('subclasses must override afficher(self)!')

    def getSellValue(self, game):
        raise NotImplementedError('subclasses must override afficher(self)!')
