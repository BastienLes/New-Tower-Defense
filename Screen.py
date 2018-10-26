import pygame
from Input import *

global taille_case, lenth, height, marginTop, marginRight, font
taille_case = 40
length = 800
height = 600
marginTop = 80
marginRight = 160
length -= (length - marginRight) % taille_case
height -= (height - marginTop) % taille_case
pygame.font.init()
font = pygame.font.SysFont("arial", 30)


class Screen(object):
    def __init__(self, length, width):
        super(Screen, self).__init__()
        pygame.init()
        pygame.display.set_caption("New Tower Defense")
        self.length = length
        self.width = width
        self.screen = pygame.display.set_mode((length, width))

    def img(self, origine, taille, url):
        img = pygame.image.load(url)
        img = pygame.transform.scale(img, taille)
        img.set_colorkey((34, 177, 76))
        self.screen.blit(img.convert(), origine)

    def txt(self, text, origine):
        texte = font.render(str(text), 1, (255, 255, 255))
        self.screen.blit(texte, origine)

    def rect(self, origine, taille, couleur):
        rect = pygame.Surface(taille).convert()
        rect.fill(couleur)
        self.screen.blit(rect, origine)

    def tower(self, tour):
        self.img(tour.getOrigin(), (30, 30), tour.urlimg())

    def all_towers(self, towers):
        for tour in towers:
            self.tower(tour)

    def achat(self, tour):
        pos = tour.getCenter()
        x = pos[0] - taille_case * 0.75
        y = pos[1] - taille_case * 0.75
        self.rect((x, y), (taille_case * 1.5,
                           taille_case * 1.5), (170, 170, 170))
        self.tower(tour)
        pygame.display.flip()

    def monster(self, mon):
        self.img(mon.getOrigin(), (30, 30), mon.urlimg())

    def all_monsters(self, monsters):
        for monster in monsters:
            if not(monster.mort):
                self.monster(monster)

    def range(self, tour):
        pygame.draw.circle(self.screen, (255, 0, 0),
                           tour.getCenter(), tour.getPo(), 3)

    def upgradeMenu(self, tour, game):
        self.range(tour)
        pos = tour.getCenter()
        x = int(pos[0] + taille_case / 2)
        y = pos[1] - 40
        self.img((x, y), (180, 80), "./image/upgrade_menu.png")
        if (tour.lvl < 3):
            self.txt(tour.getUpgradePrice(), (x + 120, y + 5))
        else:
            self.txt("max", (x + 120, y + 5))
        self.txt(tour.getSellValue(), (x + 120, y + 45))
        self.sides()
        self.stats(game)
        self.autoWave(game.autowave)
        self.all_towers(game.towers[:3])
        pygame.display.flip()

    def sides(self):
        self.rect((0, 0), (length, marginTop),
                  (140, 140, 140))  # les deux marges
        self.rect((length - marginRight, 0),
                  (marginRight, height), (140, 140, 140))

        buyX = length - marginRight / 2 - taille_case * 0.75
        buyY = 0.2 * marginTop
        buySize = (1.5 * taille_case, 1.5 * taille_case)
        buyColor = (100, 100, 100)

        self.rect((buyX, buyY + 1 * marginTop), buySize, buyColor)
        self.rect((buyX, buyY + 2 * marginTop), buySize, buyColor)
        self.rect((buyX, buyY + 3 * marginTop), buySize, buyColor)

    def path(self, game):
        path = pygame.Surface((taille_case, taille_case)).convert()
        path.fill((255, 204, 153))
        for y in range(0, len(game.pathmap[0])):
            for x in range(0, len(game.pathmap)):
                if game.pathmap[x][y]:
                    self.screen.blit(
                        path, (x * taille_case, (y + marginTop / taille_case) * taille_case))

    def gold(self, g):
        self.img((20, 20), (50, 40), "image/gold.png")
        self.txt(g, (80, 25))

    def hp(self, hp):
        self.img((220, 20), (50, 40), "image/heart.png")
        self.txt(hp, (280, 25))

    def wave(self, w):
        self.img((420, 20), (50, 40), "image/creep.png")
        self.txt(w, (480, 25))

    def stats(self, game):
        self.gold(game.gold)
        self.hp(game.vie)
        self.wave(game.vague)

    def autoWave(self, auto):
        if(auto):
            url = "image/vague_auto_oui.png"
        else:
            url = "image/vague_auto_non.png"
        self.img((length - 145, height - 62), (140, 57), url)

    def pause(self):
        self.img((length // 2 - 80, height // 2 - 40),
                 (160, 80), "image/pause.png")
        pygame.display.flip()

    def afficher(self, game):
        self.screen.fill([200, 200, 200])
        self.path(game)
        self.all_monsters(game.monsters)
        self.sides()
        self.stats(game)
        self.all_towers(game.towers)
        self.autoWave(game.autowave)

    def endWave(self):
        self.img((length - 196, 4), (191, 53), "image/READY_Blanc.png")
        pygame.display.flip()

    def decompte(self):
        self.img((length - 196, 4), (191, 53), "image/READY_Gris.png")
        for i in range(0, 3):
            self.rect((length // 2 - 15, height // 2 - 10),
                      (40, 40), (0, 0, 0))
            self.txt((3 - i), (length // 2 - 5, height // 2 - 5))
            pygame.display.flip()
            t = pygame.time.get_ticks()
            while(t > pygame.time.get_ticks() - 1000):
                Input.checkQuit()
