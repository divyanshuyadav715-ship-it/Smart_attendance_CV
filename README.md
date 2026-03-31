Project Description

The Smart Attendance System is a Python-based application that uses face recognition to automatically mark attendance. Instead of manual attendance, the system captures faces through a webcam, identifies individuals using a trained model, and records their attendance with timestamps.

This project is useful for:

Colleges & Schools
Offices & Organizations
Events & Workshops
 Features
 Capture face images and create dataset
 Train model using LBPH (Local Binary Pattern Histogram)
 Real-time face detection and recognition
 Automatic attendance marking (no duplicates)
 Saves attendance in CSV file
 Simple and lightweight implementation
 Tech Stack
Language: Python
Libraries:
OpenCV
NumPy
Pandas
Pickle

 Project Structure
 
smart-attendance-system/

│── dataset/                 # Stores face images (auto-created)

│── trainer/                 # Stores trained model files

│── attendance/              # Stores attendance CSV

│

│── create_folders.py        # Creates required folders

│── capture_images.py        # Capture face images

│── train_model.py           # Train face recognition model

│── mark_attendance.py       # Run attendance system

│

│── requirements.txt         # Dependencies

│── README.md                # Documentation

 System Requirements
Python 3.7 or above
Webcam (built-in or external)
OS: Windows / Linux / macOS
 Installation & Setup
Step 1: Clone the Repository

git clone https://github.com/your-username/smart-attendance-system.git

cd smart-attendance-system

Step 2: Install Required Libraries

pip install -r requirements.txt

If you face issues, install manually:


pip install opencv-contrib-python numpy pandas
 
 How to Use (Step-by-Step)
 
 Step 1: Create Required Folders

Run:

python create_folders.py

This will create:

dataset/

trainer/

attendance/

 Step 2: Capture Face Images

Run:

python capture_images.py

Enter your name when prompted

Look at the camera

System will capture 50 images automatically

 Tip: Ensure good lighting and clear face visibility

 Step 3: Train the Model

Run:

python train_model.py

This will:

Process all images in dataset/

Train the face recognition model

Save files in trainer/:

model.yml

labels.pkl

 Step 4: Start Attendance System

Run:

python mark_attendance.py

Webcam will open

Faces will be detected and recognized

Attendance will be marked automatically

Press ESC to stop

 Output

Attendance will be saved in:

attendance/attendance.csv

Example:


Name,Time

Divyanshu,10:15:23

Rahul,10:16:05

 How It Works

The system captures images and stores them in dataset/

Images are converted to grayscale for processing

LBPH algorithm is used to train the model

During recognition:

Face is detected using Haar Cascade

Compared with trained data
