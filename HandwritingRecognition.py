import cv2
import numpy as np
from HandTrackingModule import HandTracker

def main():
    cap = cv2.VideoCapture(0)
    detector = HandTracker()
    canvas = np.zeros((480, 640, 3), np.uint8)

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        detector.findHands(img)
        lmlist = detector.getHandPosition(img)

        if len(lmlist) != 0:
            x, y = lmlist[8][1], lmlist[8][2]
            cv2.circle(canvas, (x, y), 10, (255, 255, 255), cv2.FILLED)

        img = cv2.addWeighted(img, 0.5, canvas, 0.5, 0)
        cv2.imshow("Handwriting Recognition", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
