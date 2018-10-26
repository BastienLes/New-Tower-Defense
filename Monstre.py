global taille_case
taille_case = 40


class Monstre(object):
    def __init__(self, game):
        super(Monstre, self).__init__()
        self.x = None
        self.y = None
        self.dir = None
        self.vie = None
        self.mort = False
        self.speed = 1
        self.game = game

    def perteHp(self, dmg):
        self.vie -= dmg
        if self.vie < 1:
            self.vie = 0
            self.mort = True
            self.game.gainGold()

    def urlimg(self):
        return "./image/mob" + str(self.vie) + ".png"

    def getCenter(self):
        return (self.x, self.y)

    def getOrigin(self):
        return (self.x - 15, self.y - 15)

    def bitmapPos(self, x, y):
        return int(x / taille_case), int(y / taille_case - 2)

    def convertDir(self):
        if self.dir > 3:
            self.dir -= 4
        if self.dir < 0:
            self.dir += 4

    def findDir(self, bitmap):
        x = self.bitmapPos(self.x, self.y)[0]
        y = self.bitmapPos(self.x, self.y)[1]
        if self.dir % 2 == 0:
            if bitmap[x + 1][y]:
                self.dir = 1
            else:
                self.dir = 3
        else:
            if bitmap[x][y + 1]:
                self.dir = 2
            else:
                self.dir = 0

    def move(self):
        if self.mort is True:
            return
        x = self.x
        y = self.y
        tmp = 0
        if self.dir == 0:
            pos = self.bitmapPos(x, int(y - taille_case / 2 - 1))
            tmp = self.game.pathmap[pos[0]][pos[1]]
            if tmp:
                self.y -= self.speed
        elif self.dir == 1:
            pos = self.bitmapPos(int(x + taille_case / 2 + 1), y)
            tmp = self.game.pathmap[pos[0]][pos[1]]
            if tmp:
                self.x += self.speed
        elif self.dir == 2:
            pos = self.bitmapPos(x, int(y + taille_case / 2 + 1))
            tmp = self.game.pathmap[pos[0]][pos[1]]
            if tmp:
                self.y += self.speed
        elif self.dir == 3:
            pos = self.bitmapPos(int(x - taille_case / 2 - 1), y)
            tmp = self.game.pathmap[pos[0]][pos[1]]
            if tmp:
                self.x -= self.speed
        else:
            self.convertDir()
            self.move(self.game.pathmap)
        if tmp == 2:
            self.mort = True
            self.game.perteVie(1)
            return
        if x == self.x and y == self.y:
            self.findDir(self.game.pathmap)
