# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AuthCamera.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_AuthDialig(object):
    def setupUi(self, AuthDialig):
        if not AuthDialig.objectName():
            AuthDialig.setObjectName(u"AuthDialig")
        AuthDialig.resize(401, 358)
        AuthDialig.setStyleSheet(u"background:white;")
        self.gridLayout = QGridLayout(AuthDialig)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.auth_camera_frame = QFrame(AuthDialig)
        self.auth_camera_frame.setObjectName(u"auth_camera_frame")
        self.auth_camera_frame.setFrameShape(QFrame.Shape.NoFrame)

        self.gridLayout.addWidget(self.auth_camera_frame, 0, 0, 1, 1)

        self.message_label = QLabel(AuthDialig)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setMaximumSize(QSize(16777215, 50))
        self.message_label.setStyleSheet(u"background: rgb(0, 85, 127);\n"
"color:white;\n"
"font: 18pt \"Segoe UI\";\n"
"padding: 0 10px;")

        self.gridLayout.addWidget(self.message_label, 1, 0, 1, 1)


        self.retranslateUi(AuthDialig)

        QMetaObject.connectSlotsByName(AuthDialig)
    # setupUi

    def retranslateUi(self, AuthDialig):
        AuthDialig.setWindowTitle(QCoreApplication.translate("AuthDialig", u"Dialog", None))
        self.message_label.setText(QCoreApplication.translate("AuthDialig", u"message label ", None))
    # retranslateUi

