import pygame
from pygame.locals import *
from lib import *
from Screen import *
from Sniper import *
from Cannon import *
from Input import *
from Game import *

# pygame.transform.rotate(Surface, angle)

global taille_case, lenth, height, marginTop, marginRight, finlcase, finhcase, goldparmob, tempo
taille_case = 40
length = 800
height = 600
marginTop = 80
marginRight = 160
length -= (length - marginRight) % taille_case
height -= (height - marginTop) % taille_case
finlcase = (length - marginRight) // taille_case
finhcase = (height - marginTop) // taille_case
goldparmob = 20
tempo = 5  # ms entre chaque frame


def main():
    # init screen
    screen = Screen(length, height)

    # création de la bitmap du chemin
    path = []
    for x in range(0, (length - marginRight) // taille_case + 1):
        path.append([])
        for y in range(0, (height - marginTop) // taille_case + 1):
            if (x == 1 and y <= finhcase - 2) or (x > 1 and x <= finlcase - 2 and y == finhcase - 2) or (x == finlcase - 2 and y < finhcase - 2 and y >= 4) or (x > finlcase - 2 and y == 4):
                path[x].append(1)
            else:
                path[x].append(0)

    # création de la game
    path[16][4] = 2  # détermine l'arrivee
    startx = taille_case * 3 // 2
    starty = marginTop - taille_case // 2
    startdir = 2  # 0 haut, 1 droite, 2 bas, 3 gauche
    game = Game(path, screen, startx, starty, startdir, goldparmob)

    # ajout des tours de démo et les inutilisable

    game.addTower(Cannon((length - marginRight // 2,
                          1.2 * marginTop + 3 * taille_case // 4)))
    game.addTower(Sniper((length - marginRight // 2,
                          2.2 * marginTop + 3 * taille_case // 4)))
    game.addTower(Sniper((length - marginRight // 2,
                          3.2 * marginTop + 3 * taille_case // 4)))
    game.towers[0].actif = False
    game.towers[1].actif = False
    game.towers[2].actif = False

    # initialisation de l'écran avec chemin, démarcation de la map et tours de démo
    screen = Screen(length, height)
    screen.afficher(game)
    pygame.display.flip()

    # test
    game.autowave = False
    # print(pygame.font.get_fonts())

    game.waveInit()
    while True:
        t = pygame.time.get_ticks()
        game.moveMonsters()
        game.towersTurn()
        Input.find(game)

        screen.afficher(game)

        if(game.testEndWave()):
            if(not(game.autowave)):
                screen.endWave()
                Input.waitReady()
            game.nextWave()

        pygame.display.flip()
        pygame.time.wait(t + tempo - pygame.time.get_ticks())


main()

# faire le cout des tours et le rendu en gold quand vente
