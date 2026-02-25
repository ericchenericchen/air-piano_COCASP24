import math
from math import sqrt

class Press:
    def __init__(self, orig_hand_positions): #store orig_hand as (x,y,z) coords
        self.orig_hand = orig_hand_positions

    def distance(coords, other): #calculate just the (x,y) distance, skip z value
        return sqrt((other[0] - coords[0])**2 + (other[1] - coords[1])**2)

    def _compare_finger_distance(self, a, b, hand_positions): #find the distance between a and b, return if more than 15
        orig_dist = math.dist(self.orig_hand[a], self.orig_hand[b])
        curr_dist = math.dist(hand_positions[a], hand_positions[b])
        return orig_dist - curr_dist >= 15

    def thumbDown(self, hand_positions):
        return self._compare_finger_distance(4, 3, hand_positions)

    def indexDown(self, hand_positions):
        return self._compare_finger_distance(8, 7, hand_positions)

    def middleDown(self, hand_positions):
        return self._compare_finger_distance(12, 11, hand_positions)

    def ringDown(self, hand_positions):
        return self._compare_finger_distance(16, 15, hand_positions)

    def pinkyDown(self, hand_positions):
        return self._compare_finger_distance(20, 19, hand_positions)
