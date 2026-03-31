import cv2
import os

name = input("Enter your name: ")
path = f"dataset/{name}"

if not os.path.exists(path):
    os.makedirs(path)

cam = cv2.VideoCapture(0)
count = 0

print("Capturing images... Look at camera")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow("Capturing", frame)

    cv2.imwrite(f"{path}/{count}.jpg", frame)
    count += 1

    if count >= 50:
        break

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()

print("Done capturing images!")
