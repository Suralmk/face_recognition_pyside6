# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TakePicture.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_TakePictureDialog(object):
    def setupUi(self, TakePictureDialog):
        if not TakePictureDialog.objectName():
            TakePictureDialog.setObjectName(u"TakePictureDialog")
        TakePictureDialog.resize(401, 358)
        TakePictureDialog.setMinimumSize(QSize(401, 358))
        TakePictureDialog.setMaximumSize(QSize(1678888, 16777215))
        TakePictureDialog.setStyleSheet(u"background:white;")
        self.gridLayout = QGridLayout(TakePictureDialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.take_pic_frame = QFrame(TakePictureDialog)
        self.take_pic_frame.setObjectName(u"take_pic_frame")
        self.take_pic_frame.setMinimumSize(QSize(0, 308))
        self.take_pic_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.take_pic_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.take_pic_frame, 0, 0, 1, 2)

        self.message_label = QLabel(TakePictureDialog)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setStyleSheet(u"font: 18pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.message_label, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 9, 9)
        self.cancel_pic_button = QPushButton(TakePictureDialog)
        self.cancel_pic_button.setObjectName(u"cancel_pic_button")
        self.cancel_pic_button.setMinimumSize(QSize(80, 30))
        self.cancel_pic_button.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"color: rgb(0, 85, 127);\n"
"border: 1px solid rgb(0, 85, 127);\n"
"")

        self.horizontalLayout.addWidget(self.cancel_pic_button)

        self.take_pic_button = QPushButton(TakePictureDialog)
        self.take_pic_button.setObjectName(u"take_pic_button")
        self.take_pic_button.setMinimumSize(QSize(80, 30))
        self.take_pic_button.setStyleSheet(u"QPushButton {\n"
"background:rgb(0, 85, 127);\n"
"color:white;\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background:rgba(0, 85, 127, 0.8);\n"
"}")

        self.horizontalLayout.addWidget(self.take_pic_button)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)


        self.retranslateUi(TakePictureDialog)

        QMetaObject.connectSlotsByName(TakePictureDialog)
    # setupUi

    def retranslateUi(self, TakePictureDialog):
        TakePictureDialog.setWindowTitle(QCoreApplication.translate("TakePictureDialog", u"Dialog", None))
        self.message_label.setText(QCoreApplication.translate("TakePictureDialog", u"TextLabel", None))
        self.cancel_pic_button.setText(QCoreApplication.translate("TakePictureDialog", u"cancel", None))
        self.take_pic_button.setText(QCoreApplication.translate("TakePictureDialog", u"Take", None))
    # retranslateUi

