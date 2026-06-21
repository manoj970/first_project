import cv2
import os
import csv
import time
from datetime import datetime

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
if face_cascade.empty():
    print("Failed to load face cascade")
    exit()

os.makedirs("snapshots", exist_ok=True)
os.makedirs("recordings", exist_ok=True)
attendance_file = "attendance.csv"

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

ret, frame = cap.read()
if not ret:
    print("Failed to read from camera")
    cap.release()
    exit()

frame = cv2.resize(frame, (640, 480))
frame_height, frame_width = frame.shape[:2]
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(os.path.join("recordings", "attendance_record.avi"), fourcc, 20.0, (frame_width, frame_height))
if not out.isOpened():
    print("Cannot open video writer. Check codec support and output path.")
    cap.release()
    exit()

# Create attendance CSV file with header if it does not exist.
if not os.path.exists(attendance_file):
    with open(attendance_file, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["timestamp", "face_count"])

attendance_logged = False
snapshot_taken = False
start_time = time.time()  # Record start time for 5 second limit

while True:
    # Check if 5 seconds have elapsed
    if time.time() - start_time > 5:
        print("5 seconds elapsed. Stopping recording.")
        break

    ret, frame = cap.read()
    if not ret:
        print("Cannot read camera frame")
        break

    frame = cv2.resize(frame, (frame_width, frame_height))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    faces = face_cascade.detectMultiScale(blur, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    attendance_text = "No face detected"

    if len(faces) > 0:
        attendance_text = f"Faces detected: {len(faces)}"
        # Log attendance only once
        if not attendance_logged:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(attendance_file, mode="a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([timestamp, len(faces)])
            attendance_logged = True
        
        # Take snapshot only once
        if not snapshot_taken:
            for (x, y, w, h) in faces:
                face_img = frame[y:y + h, x:x + w]
                filename = os.path.join("snapshots", f"face_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.png")
                cv2.imwrite(filename, face_img)
            snapshot_taken = True
    else:
        attendance_logged = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(frame, attendance_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    out.write(frame)
    cv2.imshow("Smart Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
