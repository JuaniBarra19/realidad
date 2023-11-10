import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

detector = HandDetector(maxHands=2, detectionCon=0.8)

while True:
    success, img = cap.read()
    #img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)