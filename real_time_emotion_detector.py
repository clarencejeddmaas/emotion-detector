# 1. Import the required libraries
import cv2
from fer import FER

# 2. Initialize emotion detector and video capture

# Create the emotion detector using FER library
emotion_detector = FER()

# Start capturing video from computer's camera
video_capture = cv2.VideoCapture(0)

# Emotions that will be shown
emotion_categories = ['Happy', 'Sad', 'Angry', 'Surprised', 'Neutral']
