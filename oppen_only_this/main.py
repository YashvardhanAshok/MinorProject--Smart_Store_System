import cv2
import numpy as np
from pyzbar.pyzbar import decode
import dlib
import math
import cv2
import mediapipe as mp
import pyzbar.pyzbar as pyzbar

# Initialize MediaPipe models
mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh
mp_pose = mp.solutions.pose

# Initialize PyZbar
zbar = pyzbar.pyzbar.decode

# Function to draw bounding boxes and labels
def draw_boxes_and_labels(image, results, labels):
    for detection in results.detections:
        # Draw bounding box
        bbox = detection.location_data.relative_bounding_box
        h, w, c = image.shape
        x, y, w, h = int(bbox.xmin * w), int(bbox.ymin * h), int(bbox.width * w), int(bbox.height * h)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Draw label
        if labels:
            label = f"{labels[detection.label_id]}"
            cv2.putText(image, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Function to process video frames
def process_frame(frame):
    # Convert to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Face Detection and Age Estimation
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(rgb_frame)
        if results.detections:
            for detection in results.detections:
                # Calculate age (you'll need to implement an age estimation model)
                # ...
                age = estimate_age(detection)
                # Draw bounding box and age label
                draw_boxes_and_labels(frame, results, [f"Age: {age}"])

    # Object Detection (Vegetables)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        results = pose.process(rgb_frame)
        if results.pose_landmarks:
            # Detect and label vegetables using pose landmarks
            # ...

    # QR Code Detection and Reading
    # barcodes = zbar(frame)
    for barcode in barcodes:
        # Decode QR code data
        barcode_data = barcode.data.decode('utf-8')
        # Draw bounding box and print data
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, barcode_data, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        print(barcode_data)

    return frame

# Main function to capture and process video
def main():
    cap = cv2.VideoCapture(0)  # 0 for default camera

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = process_frame(frame)

        cv2.imshow('Video', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
age_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def estimate_age(face):
    return np.random.randint(20, 50)

def detect_vegetables(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    green_lower = np.array([35, 100, 50])
    green_upper = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, green_lower, green_upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  # Ignore small areas
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Vegetable", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

def read_qr_codes(frame):
    qr_codes = decode(frame)
    for qr in qr_codes:
        points = np.array([qr.polygon], np.int32).reshape((-1, 1, 2))
        cv2.polylines(frame, [points], True, (255, 0, 0), 2)
        data = qr.data.decode('utf-8')
        x, y, w, h = qr.rect
        cv2.putText(frame, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        print(f"QR Code Data: {data}")

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            face_region = gray[y:y + h, x:x + w]
            age = estimate_age(face_region)
            cv2.putText(frame, f"Age: {age}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        detect_vegetables(frame)

        read_qr_codes(frame)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
