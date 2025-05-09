import cv2
import mediapipe as mp
import time
import handtrackingmodule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(
        img)  # if we write draw = false here then the connection lines and all coordinate points will disappear.
    lmList = detector.findPosition(img,
                                   draw=False)  # if we write draw = false here then the emphasis hand marker disappears.
    if len(lmList) != 0:
        print(lmList[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime) 
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_TRIPLEX, 2, (100, 250, 100), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
