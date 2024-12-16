from MainPage import Ui_MainWindow
from  PySide6.QtWidgets import QMainWindow, QMessageBox
from auth_camera import AuthCameraAction
from auth import Authentication
from take_picture import TakePic
from PySide6.QtGui import QImage, QPixmap
class Face_Recognition(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Face Recognition and Authentication")

        self.auth = Authentication()
        # We start the applcation from the login page
        self.stackedWidget.setCurrentIndex(1) # Homepage index = 0, Login index = 1, Register index = 2

        # Make the buttons  navigate to register page
        self.login_register_btn.clicked.connect(self.switch_to_register)
        self.register_login.clicked.connect(self.switch_to_login)

        # open AuthCamera when "Login with face ID" button is clicked
        self.face_login_btn.clicked.connect(self.open_face_auth_camera)

        # Connect Register button
        self.register_btn.clicked.connect(self.register_user)

        #Connect login Button
        self.login_btn.clicked.connect(self.login_user)

        #connect logout button
        self.home_logout_btn.clicked.connect(self.logout_user)

        #connect to take picture dialog
        self.home_take_pic_btn.clicked.connect(self.open_take_pic_dialog)

    def switch_to_register(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_login(self):
        self.stackedWidget.setCurrentIndex(1)

    def open_face_auth_camera(self):
        self.authCamera =  AuthCameraAction()
        self.authCamera.start_auth_camera()
        result = self.authCamera.exec()

        # int(result) == 1 means face authentication is succesful
        # we are creating a diffrent login method/ logic for face recognition
        # we are validating thr face encoding not the username and the passwod
        if int(result) == 1:
            self.stackedWidget.setCurrentIndex(0)
            user = self.auth.get_current_user()[0]
            self.home_full_name.setText(user[1])
            self.home_username.setText(user[2])
            if user[3] is not None:
                image = QImage(f"{user[2]}_image.jpg")
                self.home_user_pic.setPixmap(QPixmap.fromImage(image))
    
    def register_user(self):
        name = self.register_full_name.text()
        username = self.register_username.text().strip()
        password = self.register_password.text().strip()

        # validating if all fields are inserted
        if  not name or not username or not password:
            QMessageBox.critical(
                self, "Registration Failed", "Please enter all the required fields. \n Full name, Username and Password",
                QMessageBox.StandardButton.Ok
            )
            return
        
        for user in self.auth.all_users:
            if username in user:
                QMessageBox.critical(
                    self, "Registration Failed", "Username already exists!",
                QMessageBox.StandardButton.Ok
                )
                return
            
        user = self.auth.register_user(name, username, password)

            # Clear the input fields if the user is registerd succesfully
        if user:
            self.register_full_name.clear()
            self.register_username.clear()
            self.register_password.clear()
        else:
            QMessageBox.critical(
                    self, "Registration Failed", f"{user}",  QMessageBox.StandardButton.Ok
                )
    def login_user(self):
        username = self.login_username.text().strip()
        password = self.login_password.text().strip()

        if self.auth.login_user(username, password):
            # clear input fields
            self.login_password.clear()
            self.login_username.clear()
            user = self.auth.current_user[0]
            # Navigate to home page
            self.stackedWidget.setCurrentIndex(0)
            self.home_full_name.setText(user[1])
            self.home_username.setText(user[2])
            if user[3] is not None:
                image = QImage(f"{user[2]}_image.jpg")
                self.home_user_pic.setPixmap(QPixmap.fromImage(image))

            self.show_message("Login Succesfull", f" Welcome {user[1]} You are sucesfully logged in")
        else:
            QMessageBox.critical(
                self, "Login Failed", "Invalid username or password", QMessageBox.StandardButton.Ok
            )
            
    def logout_user(self):
        self.auth.logout_user()
        self.stackedWidget.setCurrentIndex(1)
        image = QImage("images/demo_user.png")
        self.home_user_pic.setPixmap(QPixmap.fromImage(image))
        self.show_message("Logout Succesfull", "You have succesfully logged out!")

    def open_take_pic_dialog(self):
        # Initialize take picture with the username of the current logged in  user
        self.take_pic = TakePic(username=self.auth.current_user[0][2])
        self.take_pic.start_camera()
        self.take_pic.exec()

    def closeEvent(self, event):
        self.auth.logout_user()
        event.accept()

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()