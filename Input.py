import pygame
from pygame.locals import *
from lib import *

global taille_case, lenth, height, marginTop, marginRight
taille_case = 40
length = 800
height = 600
marginTop = 80
marginRight = 160


class Input:
    def quiter():
        pygame.mixer.music.stop()
        pygame.mixer.stop()
        pygame.display.quit()
        quit()

    def upgradeMenu(tour, game):
        x = tour.getCenter()[0] + taille_case / 2
        y = tour.getCenter()[1] - 40
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    Input.quiter()

                if event.type == MOUSEBUTTONDOWN:
                    if event.pos[0] > x and event.pos[0] < x + 180 and event.pos[1] > y and event.pos[1] < y + 80:
                        if event.pos[0] > x and event.pos[0] < x + 31:
                            if event.pos[1] > y + 5 and event.pos[1] < y + 36:
                                game.upgrade(tour)
                                return
                            if event.pos[1] > y + 44 and event.pos[1] < y + 76:
                                game.sell(tour)
                                return
                    else:
                        return

    def getClickInMap():
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    Input.quiter()

                if event.type == MOUSEBUTTONDOWN:
                    if event.pos[0] < length - marginRight and event.pos[1] > marginTop:
                        return event.pos
                    else:
                        return

    def checkOnTower(game, pos):
        for tour in game.towers:
            if tour.getCenter() == pos:
                return tour
        return False

    def checkOnPath(game, pos):
        x = int((pos[0] - taille_case / 2) / taille_case)
        y = int((pos[1] - taille_case / 2) / taille_case)
        return game.pathmap[x][int(y - marginTop / taille_case)]

    def buyTower(game):
        pos = Input.getClickInMap()
        if pos is None:
            return False
        pos = normPosCenter(pos)

        if Input.checkOnTower(game, pos) is not(False):
            return False
        if Input.checkOnPath(game, pos):
            return False
        return pos

    def buyCannon(game):
        if(game.gold >= 150):
            pos = Input.buyTower(game)
            if pos is False:
                return
            game.gold -= 150
            game.addCannon(normPosCenter(pos))

    def buySniper(game):
        if(game.gold >= 300):
            pos = Input.buyTower(game)
            if pos is False:
                return
            game.gold -= 300
            game.addSniper(normPosCenter(pos))

    def checkBuy(game, pos):
        if pos[0] > length - marginRight + taille_case * 1.25 and pos[0] < length - taille_case * 1.25:
            if pos[1] > marginTop * 1.2 and pos[1] < marginTop * 1.2 + 1.5 * taille_case:
                game.screen.achat(game.towers[0])
                Input.buyCannon(game)
            if pos[1] > marginTop * 2.2 and pos[1] < marginTop * 2.2 + 1.5 * taille_case:
                game.screen.achat(game.towers[1])
                Input.buySniper(game)
            if pos[1] > marginTop * 3.2 and pos[1] < marginTop * 3.2 + 1.5 * taille_case:
                pass  # Input.buyLaNouvelleTour()
                game.screen.achat(game.towers[0])

    def checkUpgrade(game, pos):
        tour = Input.checkOnTower(game, pos)
        if tour is False:
            return
        game.screen.upgradeMenu(tour, game)
        Input.upgradeMenu(tour, game)

    def checkOther(game, pos):
        pass

    def pause():
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    Input.quiter()

                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        return

    def find(game):
        for event in pygame.event.get():
            if event.type == QUIT:
                Input.quiter()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                if event.pos[0] > 640:
                    Input.checkBuy(game, event.pos)

                elif event.pos[1] > 80:
                    Input.checkUpgrade(game, normPosCenter(event.pos))

                else:
                    Input.checkOther(game, event.pos)

            if event.type == KEYDOWN:

                if event.key == K_SPACE:
                    game.screen.pause()
                    Input.pause()

                if event.key == K_F1:
                    game.screen.achat(game.towers[0])
                    Input.buyCannon(game)

                if event.key == K_F2:
                    game.screen.achat(game.towers[1])
                    Input.buySniper(game)

    def waitReady():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    Input.quiter()

                if event.type == MOUSEBUTTONDOWN:
                    if event.pos[0] > length - 196 and event.pos[0] < length - 5:
                        if event.pos[1] > 4 and event.pos[1] < 57:
                            return

    def checkQuit():
        for event in pygame.event.get():
            if event.type == QUIT:
                Input.quiter()
