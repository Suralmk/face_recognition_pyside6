import cv2
import face_recognition
from auth import Authentication
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QMessageBox
from PySide6.QtCore import QTimer
from TakePicture import Ui_TakePictureDialog
import face_recognition

class TakePic(Ui_TakePictureDialog, QDialog):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Take Picture")
        self.username = username
        # create a label for the image
        self.layout = QVBoxLayout(self.take_pic_frame)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        #connnect take picture button
        self.take_pic_button.clicked.connect(self.take_image)

        #connect cancel button
        self.cancel_pic_button.clicked.connect(self.close)
       
    def start_camera(self):
        self.capture = cv2.VideoCapture(0)

        # Ware taking pics from the video frame every 30ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)
    
    def update_frame(self):
        ret, frame = self.capture.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.image_label.setPixmap(QPixmap.fromImage(image))
            face_encoding = face_recognition.face_encodings(frame)

            if len(face_encoding) > 1:
                self.message_label.setText(f"Error, {len(face_encoding)} face detected!")
                return
            else:
                self.message_label.setText(f"Your face detected!")

    def take_image (self):
        auth = Authentication()
        ret, frame  = self.capture.read()

        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image_path = f"{self.username}_image.jpg"
            cv2.imwrite(image_path, frame_rgb)
            captured_image = face_recognition.load_image_file(image_path)
            captured_encoding = face_recognition.face_encodings(captured_image)[0]
            
            # update face_endcoding in DB for the log   ged in user
            auth.update_encoding(captured_encoding, self.username)
            QMessageBox.information(self, "Image Updated", f"Dear {self.username} image is captured succesfully")

    # when the camera dialog closes
    def closeEvent(self, event):
        self.timer.stop()
        self.capture.release()
        event.accept()            