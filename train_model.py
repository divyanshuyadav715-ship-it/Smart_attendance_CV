import cv2
import numpy as np
import os
import pickle

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_map = {}
label_id = 0

for person in os.listdir("dataset"):
    path = os.path.join("dataset", person)
    label_map[label_id] = person

    for img in os.listdir(path):
        img_path = os.path.join(path, img)
        gray = cv2.imread(img_path, 0)
        faces.append(gray)
        labels.append(label_id)

    label_id += 1

recognizer.train(faces, np.array(labels))
recognizer.save("trainer/model.yml")

with open("trainer/labels.pkl", "wb") as f:
    pickle.dump(label_map, f)

print("Training completed successfully!")
