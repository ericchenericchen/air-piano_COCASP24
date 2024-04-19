import cv2
import math
from pypiano import Piano
from mingus.containers import Note
from mingus.midi import fluidsynth
from HandTrackingModule import FindHands

cap = cv2.VideoCapture(0)
detector = FindHands()
p = Piano()
def thumbDown(hand_positions, orig_hand):
    # orig_hand[0][0] = index first point; orig_hand[0][1] = index second point
    # compare above coordinates to hand1_positions[7] = index first point and hand1_positions[8] = index first point
    orig_dist = math.dist(orig_hand[4][0], orig_hand[4][1])
    curr_dist = math.dist(hand1_positions[3], hand1_positions[4])
    if((orig_dist - curr_dist) >= 15):
        return True

def indexDown(hand_positions, orig_hand):
    # orig_hand[0][0] = index first point; orig_hand[0][1] = index second point
    # compare above coordinates to hand1_positions[7] = index first point and hand1_positions[8] = index first point
    orig_dist = math.dist(orig_hand[0][0], orig_hand[0][1])
    curr_dist = math.dist(hand1_positions[7], hand1_positions[8])
    if((orig_dist - curr_dist) >= 15):
        return True
    
def middleDown(hand_positions, orig_hand):
    orig_dist = math.dist(orig_hand[1][0], orig_hand[1][1])
    curr_dist = math.dist(hand1_positions[11], hand1_positions[12])
    if((orig_dist - curr_dist) >= 15):
        return True

def ringDown(hand_positions, orig_hand):
    orig_dist = math.dist(orig_hand[2][0], orig_hand[2][1])
    curr_dist = math.dist(hand1_positions[15], hand1_positions[16])
    if((orig_dist - curr_dist) >= 15):
        return True

def pinkyDown(hand_positions, orig_hand):
    orig_dist = math.dist(orig_hand[3][0], orig_hand[3][1])
    curr_dist = math.dist(hand1_positions[19], hand1_positions[20])
    if((orig_dist - curr_dist) >= 15):
        return True

succeed, img = cap.read()
hand1_positions = detector.getPosition(img, range(21), draw=False)
print("Display full hand")
while len(hand1_positions) != 21: # waiting for hand
    succeed, img = cap.read()
    hand1_positions = detector.getPosition(img, range(21), draw=False)

# in order index middle ring pinky
orig_hand = []
orig_hand.append((hand1_positions[7], hand1_positions[8]))
orig_hand.append((hand1_positions[11], hand1_positions[12]))
orig_hand.append((hand1_positions[15], hand1_positions[16]))
orig_hand.append((hand1_positions[19], hand1_positions[20]))
orig_hand.append((hand1_positions[3], hand1_positions[4]))


while True:
    _, img = cap.read()
    hand1_positions = detector.getPosition(img, range(21), draw=False)
    hand2_positions = detector.getPosition(img, range(21), hand_no=1, draw=False)
    
    counter = 0
    print("size of hand1", len(hand1_positions))
    for pos in hand1_positions:
        # fingertips: (7, 8) (11, 12) (15, 16) (19, 20)
        if((counter % 4 == 0)):
            cv2.circle(img, pos, 5, (0, 0, 255), cv2.FILLED)
        elif (counter % 4 == 3):
            cv2.circle(img, pos, 5, (0, 255, 0), cv2.FILLED)             
        counter += 1

    if(len(hand1_positions) != 0):
        print(math.dist(hand1_positions[3], hand1_positions[4])) # dist between thumb top and middle
    #for pos in hand2_positions:
        #cv2.circle(img, pos, 5, (255,0,0), cv2.FILLED)
    # print("Index finger up:", detector.index_finger_up(img))
    # print("Middle finger up:", detector.middle_finger_up(img))
    # print("Ring finger up:", detector.ring_finger_up(img))
    # print("Little finger up:", detector.little_finger_up(img))
    if(thumbDown(hand1_positions, orig_hand)):
        p.play("C-4")
        print("thumb down")
    if(indexDown(hand1_positions, orig_hand)):
        p.play("C-4")
        print("index down")
    if(middleDown(hand1_positions, orig_hand)):
        p.play("C-4")
        print("middle down")
    if(ringDown(hand1_positions, orig_hand)):
        p.play("C-4")
        print("ring down")
    if(pinkyDown(hand1_positions, orig_hand)):
        p.play("C-4")
        print("pinky down")
    cv2.imshow("Image", img)
    if cv2.waitKey(10) == ord('q'):
        break