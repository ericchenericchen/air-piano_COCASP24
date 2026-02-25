import cv2
import math
# from pypiano import Piano
# from mingus.containers import Note
# from mingus.midi import fluidsynth
from HandTrackingModule import FindHands
from cvzone.HandTrackingModule import HandDetector

from Press import Press

#recalibrate
def recalibrate (hand_positions) :
    hand1_positions = []

    while len(hand1_positions) != 21: # waiting for hand
        _, img = cap.read()
        hands, img = detector.findHands(img)
        cv2.imshow("Image", img)

        # if your hand has 21 points on it, store it in hand1
        hand1_positions = [] if len(hands) ==0 else hands[0]["lmList"] #take first hand as an array

    # in order index middle ring pinky
    orig_hand = []
    orig_hand.append((hand1_positions[7], hand1_positions[8]))
    orig_hand.append((hand1_positions[11], hand1_positions[12]))
    orig_hand.append((hand1_positions[15], hand1_positions[16]))
    orig_hand.append((hand1_positions[19], hand1_positions[20]))
    orig_hand.append((hand1_positions[3], hand1_positions[4]))

    return orig_hand #returns the array of fingertips

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.6, maxHands= 2)

_, img = cap.read()
hands, img = detector.findHands(img) #read in hands as (x, y, z) array for each joint
cv2.imshow("Image", img)

#only try to store hands[0]["lmList"] if it exists in hands (otherwise it'll bug out)
hand1_positions = [] if len(hands) ==0 else hands[0]["lmList"]

# hand2_positions = hands[1]["lmList"]
pressKeys = Press(recalibrate(hand1_positions))

while True:
    _, img = cap.read()
    hands, img = detector.findHands(img)
    cv2.imshow("Image", img)

    hand1_positions = [] if len(hands) ==0 else hands[0]["lmList"]
    #hand2_positions = hands[1]["lmList"]
    pressKeys = Press(recalibrate(hand1_positions))

    if(len(hand1_positions) != 21):
        continue

    counter = 0
    # print("size of hand1", len(hand1_positions))
    # for pos in hand1_positions:
    #     # fingertips: (7, 8) (11, 12) (15, 16) (19, 20)
    #     if((counter % 4 == 0)):
    #         cv2.circle(img, pos, 5, (0, 0, 255), cv2.FILLED)
    #     elif (counter % 4 == 3):
    #         cv2.circle(img, pos, 5, (0, 255, 0), cv2.FILLED)             
    #     counter += 1

    if(len(hand1_positions) != 0):
        print(pressKeys.distance(hand1_positions[3], hand1_positions[4])) # dist between thumb top and middle

    #for pos in hand2_positions:
        #cv2.circle(img, pos, 5, (255,0,0), cv2.FILLED)
    # print("Index finger up:", detector.index_finger_up(img))
    # print("Middle finger up:", detector.middle_finger_up(img))
    # print("Ring finger up:", detector.ring_finger_up(img))
    # print("Little finger up:", detector.little_finger_up(img))

    if(pressKeys.thumbDown(hand1_positions)):
        print("thumb down")
    if(pressKeys.indexDown(hand1_positions)):
        print("index down")
    if(pressKeys.middleDown(hand1_positions)):
        print("middle down")
    if(pressKeys.ringDown(hand1_positions)):
        print("ring down")
    if(pressKeys.pinkyDown(hand1_positions)):
        print("pinky down")
    
    if cv2.waitKey(10) == ord('q'):
        break