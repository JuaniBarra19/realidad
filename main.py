import mediapipe as mp
import cv2


mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)



with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)
        # Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Print coordinates of face landmarks
        if results.face_landmarks:
            for landmark in results.face_landmarks.landmark:
                x, y, z = landmark.x, landmark.y, landmark.z
                #print(f"Face Landmark - X: {x}, Y: {y}, Z: {z}")
        # Print coordinates of hand landmarks
        if results.left_hand_landmarks:
            for landmark in results.left_hand_landmarks.landmark:
                x, y, z = landmark.x, landmark.y, landmark.z
                #print(f"Left Hand Landmark - X: {x}, Y: {y}, Z: {z}")
        if results.right_hand_landmarks:
            for landmark in results.right_hand_landmarks.landmark:
                x, y, z = landmark.x, landmark.y, landmark.z
                #print(f"Right Hand Landmark - X: {x}, Y: {y}, Z: {z}")
        print("aaaaaaaaaaaaaaaaaa")
        cv2.imshow('Raw Webcam Feed', image)
        cap.release()
        cv2.destroyAllWindows()






