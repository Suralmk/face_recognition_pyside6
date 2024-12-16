from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QMessageBox
from AuthCamera import Ui_AuthDialig
import cv2
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
import face_recognition
from auth import Authentication
import numpy as np

class AuthCameraAction(Ui_AuthDialig ,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Face detection camera")

        # Create a layout for displaying the camera
        self.layout = QVBoxLayout(self.auth_camera_frame)
        self.camera_label = QLabel(self)
        self.layout.addWidget(self.camera_label)

    def start_auth_camera(self):
        self.capture = cv2.VideoCapture(0)

        # Ware taking pics from the video frame every 30ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.detect_faces)
        self.timer.start(30)
    
    def detect_faces(self):
        auth = Authentication()

        ret, frame = self.capture.read() or None

        # convert frame to rgb for face detection
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #Find all faces in the frame
        face_locations = face_recognition.face_locations(rgb_frame)

        users = auth.get_all_users()

        # Adding all the face encodings we have  for each user in a list
        known_encodings = [np.frombuffer(user[4]) for user in users if user[4] is not None]
        face_encodings =  face_recognition.face_encodings(frame, face_locations)

        if face_locations:
            self.message_label.setText(f" {len(face_encodings)} face detected")
        else: 
            self.message_label.setText(f"No face detected")

        # Drawing a rectangle in the detexted face
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        # Display the face frame in the pyside6 camera label
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        qt_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.camera_label.setPixmap(QPixmap.fromImage(qt_img))

        # Now it is tome to login th =e user
  
        print(users)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            if True in matches:
                # stop the timer 
                self.timer.stop()
                # release the camara
                self.capture.release()
                #identify the user
                user = users[matches.index(True)]

                # lofin the user with face encoding
                accepted = auth.face_login(user[2])
                print(accepted, "Accepted")
                # Close the dialog with  int(result) = 1
                if accepted: 
                    self.accept()
                    return
                
            # else we will  notofy the user the face is not recognized
            QMessageBox.warning(self, "Face detection failed", "User fae is not recognized")
            return
        
    # when the camera dialog closes
    def closeEvent(self, event):
        self.timer.stop()
        self.capture.release()
        event.accept()
