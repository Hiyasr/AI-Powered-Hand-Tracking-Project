import cv2
import numpy as np
import pyautogui
from HandTrackingModule import HandTracker

wCam, hCam = 640, 480
wScr, hScr = pyautogui.size()
frameR = 150
smoothing = 5
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = HandTracker()

def Mouse(img):
    global frameR, smoothing, plocX, plocY, clocX, clocY, wScr, hScr
    detector.findHands(img)
    lmlist = detector.getHandPosition(img)

    if len(lmlist) != 0:
        Xindex, Yindex = lmlist[8][1], lmlist[8][2]
        Xmiddle, Ymiddle = lmlist[12][1], lmlist[12][2]

        fingers = [1 if id in [8, 12] else 0 for id, _, _ in lmlist]

        if fingers[0] == 1 and fingers[1] == 0:
            xMouse = np.interp(Xindex, (frameR, wCam - frameR), (0, wScr))
            yMouse = np.interp(Yindex, (frameR, hCam - frameR), (0, hScr))
            clocX = plocX + (xMouse - plocX) / smoothing
            clocY = plocY + (yMouse - plocY) / smoothing
            pyautogui.moveTo(clocX, clocY)
            cv2.circle(img, (Xindex, Yindex), 15, (20, 180, 90), cv2.FILLED)
            plocY, plocX = clocY, clocX

        if fingers[0] == 1 and fingers[1] == 1:
            length = np.linalg.norm(np.array([Xindex, Yindex]) - np.array([Xmiddle, Ymiddle]))
            if length < 40:
                pyautogui.click()

    return img

def main():
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = Mouse(img)
        cv2.imshow("Virtual Mouse", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
