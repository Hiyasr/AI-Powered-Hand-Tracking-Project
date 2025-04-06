import cv2
from HandTrackingModule import HandTracker

def recognize_gesture(fingers):
    return sum(fingers)  # Example: Count fingers as gesture

def main():
    cap = cv2.VideoCapture(0)
    detector = HandTracker()

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        detector.findHands(img)
        lmlist = detector.getHandPosition(img)

        if len(lmlist) != 0:
            fingers = [1 if id in [8, 12, 16, 20] else 0 for id, _, _ in lmlist]
            gesture = recognize_gesture(fingers)
            cv2.putText(img, f"Gesture: {gesture}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("ASL Recognition", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
