import torch
import cv2
from torchvision import transforms, models
from PIL import Image
import os


def detect_grocery(image_path):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    results = model(image_path)

    grocery_items = []
    for result in results.xyxy[0]:  
        label = model.names[int(result[5])]  
        confidence = result[4].item()  
        grocery_items.append((label, confidence))

    return grocery_items

def predict_age_gender(image_path):
    age = 25  
    gender = "Male"  
    return age, gender

def estimate_height(image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    bbox_height = 300  
    estimated_height_cm = (bbox_height / height) * 170  
    return estimated_height_cm

def log_detections(image_path):
    age, gender = predict_age_gender(image_path)
    print(f"Age: {age}, Gender: {gender}")

    estimated_height = estimate_height(image_path)
    print(f"Estimated Height: {estimated_height} cm")

    grocery_items = detect_grocery(image_path)
    print("Detected Grocery Items:")
    for item, confidence in grocery_items:
        print(f" - {item}: {confidence:.2f} confidence")

image_path = 'Back_End/image.png'  
log_detections(image_path)

