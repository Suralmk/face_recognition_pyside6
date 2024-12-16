# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(732, 509)
        MainWindow.setMinimumSize(QSize(400, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background:white;")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.layoutWidget = QWidget(self.Home)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(190, 130, 391, 221))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setSpacing(30)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.home_user_pic = QLabel(self.layoutWidget)
        self.home_user_pic.setObjectName(u"home_user_pic")
        self.home_user_pic.setMaximumSize(QSize(100, 100))
        self.home_user_pic.setPixmap(QPixmap(u":/images/images/download (22).png"))
        self.home_user_pic.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.home_user_pic)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.home_full_name = QLabel(self.layoutWidget)
        self.home_full_name.setObjectName(u"home_full_name")
        self.home_full_name.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"")

        self.verticalLayout_7.addWidget(self.home_full_name)

        self.home_username = QLabel(self.layoutWidget)
        self.home_username.setObjectName(u"home_username")
        self.home_username.setStyleSheet(u"font: 300 12pt \"Segoe UI\";")

        self.verticalLayout_7.addWidget(self.home_username)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.home_take_pic_btn = QPushButton(self.layoutWidget)
        self.home_take_pic_btn.setObjectName(u"home_take_pic_btn")
        self.home_take_pic_btn.setMinimumSize(QSize(200, 30))
        self.home_take_pic_btn.setStyleSheet(u"QPushButton {\n"
"background:rgb(0, 85, 127);\n"
"color:white;\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background:rgba(0, 85, 127, 0.8);\n"
"}")

        self.verticalLayout_9.addWidget(self.home_take_pic_btn)

        self.home_logout_btn = QPushButton(self.layoutWidget)
        self.home_logout_btn.setObjectName(u"home_logout_btn")
        self.home_logout_btn.setMinimumSize(QSize(200, 30))
        self.home_logout_btn.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"color: rgb(0, 85, 127);\n"
"border: 1px solid rgb(0, 85, 127);\n"
"")

        self.verticalLayout_9.addWidget(self.home_logout_btn)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.stackedWidget.addWidget(self.Home)
        self.Login = QWidget()
        self.Login.setObjectName(u"Login")
        self.gridLayout_2 = QGridLayout(self.Login)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/images/images/2473102.jpg"))

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.frame = QFrame(self.Login)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(270, 0))
        self.frame.setMaximumSize(QSize(270, 16777215))
        self.frame.setStyleSheet(u"background:white;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 181, 31))
        self.label.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 131, 21))
        self.label_3.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 210, 221, 58))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label_5)

        self.login_password = QLineEdit(self.layoutWidget1)
        self.login_password.setObjectName(u"login_password")
        self.login_password.setMinimumSize(QSize(200, 30))
        self.login_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.login_password)

        self.layoutWidget2 = QWidget(self.frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 140, 221, 58))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_4)

        self.login_username = QLineEdit(self.layoutWidget2)
        self.login_username.setObjectName(u"login_username")
        self.login_username.setMinimumSize(QSize(200, 30))

        self.verticalLayout.addWidget(self.login_username)

        self.layoutWidget3 = QWidget(self.frame)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 290, 221, 81))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.login_btn = QPushButton(self.layoutWidget3)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(200, 30))
        self.login_btn.setStyleSheet(u"QPushButton {\n"
"background:rgb(0, 85, 127);\n"
"color:white;\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background:rgba(0, 85, 127, 0.8);\n"
"}")

        self.verticalLayout_3.addWidget(self.login_btn)

        self.face_login_btn = QPushButton(self.layoutWidget3)
        self.face_login_btn.setObjectName(u"face_login_btn")
        self.face_login_btn.setMinimumSize(QSize(200, 30))
        self.face_login_btn.setStyleSheet(u"QPushButton {\n"
"background:rgb(0, 85, 127);\n"
"color:white;\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background:rgba(0, 85, 127, 0.8);\n"
"}")

        self.verticalLayout_3.addWidget(self.face_login_btn)

        self.layoutWidget4 = QWidget(self.frame)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 390, 191, 18))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.login_register_btn = QPushButton(self.layoutWidget4)
        self.login_register_btn.setObjectName(u"login_register_btn")
        self.login_register_btn.setStyleSheet(u"background:white;\n"
"color:rgb(0, 85, 127);\n"
"border:none;\n"
"")

        self.horizontalLayout.addWidget(self.login_register_btn)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Login)
        self.Register = QWidget()
        self.Register.setObjectName(u"Register")
        self.gridLayout_3 = QGridLayout(self.Register)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.Register)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(270, 0))
        self.frame_2.setMaximumSize(QSize(270, 16777215))
        self.frame_2.setStyleSheet(u"background:white;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 30, 181, 31))
        self.label_8.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 60, 131, 21))
        self.label_9.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.layoutWidget_5 = QWidget(self.frame_2)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(20, 410, 191, 18))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_2.addWidget(self.label_12)

        self.register_login = QPushButton(self.layoutWidget_5)
        self.register_login.setObjectName(u"register_login")
        self.register_login.setStyleSheet(u"background:white;\n"
"color:rgb(0, 85, 127);\n"
"border:none;\n"
"")

        self.horizontalLayout_2.addWidget(self.register_login)

        self.register_btn = QPushButton(self.frame_2)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setGeometry(QRect(20, 360, 221, 30))
        self.register_btn.setMinimumSize(QSize(200, 30))
        self.register_btn.setStyleSheet(u"\n"
"QPushButton {\n"
"background:rgb(0, 85, 127);\n"
"color:white;\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background:rgba(0, 85, 127, 0.8);\n"
"}")
        self.layoutWidget5 = QWidget(self.frame_2)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(20, 160, 221, 176))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_13 = QLabel(self.layoutWidget5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.label_13)

        self.register_full_name = QLineEdit(self.layoutWidget5)
        self.register_full_name.setObjectName(u"register_full_name")
        self.register_full_name.setMinimumSize(QSize(200, 30))

        self.verticalLayout_6.addWidget(self.register_full_name)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_11 = QLabel(self.layoutWidget5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.verticalLayout_5.addWidget(self.label_11)

        self.register_username = QLineEdit(self.layoutWidget5)
        self.register_username.setObjectName(u"register_username")
        self.register_username.setMinimumSize(QSize(200, 30))

        self.verticalLayout_5.addWidget(self.register_username)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_10 = QLabel(self.layoutWidget5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.label_10)

        self.register_password = QLineEdit(self.layoutWidget5)
        self.register_password.setObjectName(u"register_password")
        self.register_password.setMinimumSize(QSize(200, 30))
        self.register_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_4.addWidget(self.register_password)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)

        self.label_7 = QLabel(self.Register)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/images/images/2473102.jpg"))

        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.Register)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_user_pic.setText("")
        self.home_full_name.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.home_username.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.home_take_pic_btn.setText(QCoreApplication.translate("MainWindow", u"Take Picture", None))
        self.home_logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Face Recognition and ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Authentication", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.face_login_btn.setText(QCoreApplication.translate("MainWindow", u"Login with Face ID", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.login_register_btn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Face Recognition and ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Authentication", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.register_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.register_btn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_7.setText("")
    # retranslateUi

