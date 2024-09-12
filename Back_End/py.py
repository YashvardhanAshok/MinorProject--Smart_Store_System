import torch
import cv2
from torchvision import transforms, models
from PIL import Image
import os

# Function to load YOLOv5 model and run inference
def detect_grocery(image_path):
    # Load YOLOv5 model (make sure you've cloned the repo and installed the dependencies)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # YOLOv5 small model

    # Perform inference
    results = model(image_path)

    # Get labels and confidence for detected objects
    grocery_items = []
    for result in results.xyxy[0]:  # Each detected object
        label = model.names[int(result[5])]  # Object label (class name)
        confidence = result[4].item()  # Confidence score
        grocery_items.append((label, confidence))

    return grocery_items

# Age and Gender Prediction Placeholder
def predict_age_gender(image_path):
    # Replace with actual model
    age = 25  # Placeholder for age prediction
    gender = "Male"  # Placeholder for gender prediction
    return age, gender

# Height Estimation (Simplified)
def estimate_height(image_path):
    # Placeholder height estimation logic based on bounding box height in pixels
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    bbox_height = 300  # Example: placeholder for actual bounding box height in pixels
    estimated_height_cm = (bbox_height / height) * 170  # Assume average human height of 170cm
    return estimated_height_cm

# Main Function to Log Detections
def log_detections(image_path):
    # Step 1: Predict Age and Gender
    age, gender = predict_age_gender(image_path)
    print(f"Age: {age}, Gender: {gender}")

    # Step 2: Estimate Height
    estimated_height = estimate_height(image_path)
    print(f"Estimated Height: {estimated_height} cm")

    # Step 3: Detect Grocery Items
    grocery_items = detect_grocery(image_path)
    print("Detected Grocery Items:")
    for item, confidence in grocery_items:
        print(f" - {item}: {confidence:.2f} confidence")

# Example Usage
image_path = 'Back_End/image.png'  
log_detections(image_path)

