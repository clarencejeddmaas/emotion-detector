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

# 5. Draw a box around the face
def draw_face_bounding_box(video_frame, face_data):
    face_x, face_y, face_width, face_height = face_data['box']
    cv2.rectangle(video_frame, (face_x, face_y), (face_x + face_width, face_y + face_height), (0, 255, 0), 2)
    return face_x, face_y, face_width, face_height

# 6. Display dominant emotion above bounding box
def display_dominant_emotion(video_frame, face_x, face_y, dominant_emotion_label):
    cv2.putText(video_frame, f'Emotion: {dominant_emotion_label.capitalize()}', (face_x, face_y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 2)

# 7. Display all emotion scores below the bounding box
def display_emotion_scores(video_frame, face_x, face_y, face_height, emotion_scores):
    emotion_text_y_position = face_y + face_height + 10
    for emotion_label, emotion_score in emotion_scores.items():
        cv2.putText(video_frame, f'{emotion_label.capitalize()}: {emotion_score:.2f}', 
                    (face_x, emotion_text_y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        emotion_text_y_position += 15

# Main loop for real-time emotion detection
while True:
    # 8. Capture the video frame
    video_frame = capture_frame()

    # If frame is None, break the loop
    if video_frame is None:
        break

    # 9. Detect emotions in the captured frame
    face_data = detect_emotions_in_frame(video_frame)
    
    if face_data:
        # Extract emotion data and display
        emotion_scores, dominant_emotion_label = extract_emotion_data(face_data)
        face_x, face_y, face_width, face_height = draw_face_bounding_box(video_frame, face_data)
        display_dominant_emotion(video_frame, face_x, face_y, dominant_emotion_label)
        display_emotion_scores(video_frame, face_x, face_y, face_height, emotion_scores)