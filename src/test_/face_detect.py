#!/usr/bin/env python3
import cv2
def detect_faces_from_camera():
    face_cascade = cv2.CascadeClassifier('../haarcascade/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        count = 0
        for (x, y, w, h) in faces:
            count += 1
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        print("Number of faces detected:", count)

    cap.release()
    cv2.destroyAllWindows()
    
def main():
    detect_faces_from_camera()
if __name__ == "__main__":
    main()
    