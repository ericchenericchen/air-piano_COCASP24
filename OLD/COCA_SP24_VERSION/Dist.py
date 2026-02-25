from math import sqrt


def distance(coords, other):
    return sqrt((other[0] -(coords[0]))**2 + (other[1] - coords[1])**2)