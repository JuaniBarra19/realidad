import time
import socket
import json
import mediapipe as mp
import cv2

host = "127.0.0.1" 
port = 50001
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
landmarks_data = {'landmarks': [], 'connections': list(mp_holistic.POSE_CONNECTIONS)}

class Camera():
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def image(self):
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    print("Error al capturar el fotograma")
                    break

                # Recolor Feed
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                results = holistic.process(image)

                # Recolor image back to BGR for rendering
                #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Dibujar landmarks en la cara
                #mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)

                if results.pose_landmarks is not None:
                # Almacena las coordenadas de los landmarks
                    landmarks_data['landmarks'] = [(landmark.x, landmark.y, landmark.z) for landmark in results.pose_landmarks.landmark]
                    landmarks_json = json.dumps(landmarks_data) 
                    self.client_socket.sendall(landmarks_json.encode('utf-8'))
                else:
                    continue
                    
                    #mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
                
                #if results.face_landmarks is not None:
                #    landmarks_data['face_landmarks'] = [(landmark.x, landmark.y, landmark.z) for landmark in results.face_landmarks.landmark]
                
                

                #cv2.imshow('Webcam con Landmarks', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
        


a = Camera()
a.image()