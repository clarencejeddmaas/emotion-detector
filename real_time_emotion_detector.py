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

# 3. Capture video frame
def capture_frame():
    frame_captured, video_frame = video_capture.read()

    # If the frame is not correctly captured, return None
    if not frame_captured:
        return None
    return video_frame

# 4. Detect the emotions in frame
def detect_emotions_in_frame(video_frame):

    # Use the detector to find emotions in the frame
    detected_faces = emotion_detector.detect_emotions(video_frame)

    if detected_faces:
        return detected_faces[0]
    return None

# 4. Extract emotion data

def extract_emotion_data(face_data):
    emotion_scores = face_data["emotions"]
    dominant_emotion_label = max(emotion_scores, key=emotion_scores.get)
    return emotion_scores, dominant_emotion_label
