import cv2
import pandas as pd
from datetime import datetime
import pickle

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/model.yml")

with open("trainer/labels.pkl", "rb") as f:
    label_map = pickle.load(f)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

attendance = []

cam = cv2.VideoCapture(0)

print("Press ESC to stop")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        id, conf = recognizer.predict(gray[y:y+h, x:x+w])

        if conf < 70:
            name = label_map[id]

            if name not in [i[0] for i in attendance]:
                time = datetime.now().strftime("%H:%M:%S")
                attendance.append([name, time])

            cv2.putText(frame, name, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()

df = pd.DataFrame(attendance, columns=["Name", "Time"])
df.to_csv("attendance/attendance.csv", index=False)

print("Attendance saved successfully!")
