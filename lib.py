import math
import random

global taille_case
taille_case = 40


def exp(x, n):
    result = 1
    for i in range(0, n):
        result *= x
    return result


def sqrt(x):
    return math.sqrt(x)


def abs(x):
    return math.abs(x)


def normOrigin(x):  # normalize to the origin of the box
    return x - x % taille_case


def normCenter(x):  # normalize to the center of the box
    return int(x - x % taille_case + taille_case / 2)


def normPosCenter(pos):
    return normCenter(pos[0]), normCenter(pos[1])


def normPosOrigin(pos):
    return normOrigin(pos[0]), normOrigin(pos[1])


def distance(x1, y1, x2, y2):
    X = x2 - x1
    Y = y2 - y1
    return sqrt(pow(X, 2) + pow(Y, 2))
