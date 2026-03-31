import os

folders = ["dataset", "trainer", "attendance"]

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

print("Folders created successfully!")
