import sys
from PySide6.QtWidgets import QApplication
from face_auth import Face_Recognition

app = QApplication(sys.argv)
window = Face_Recognition()
window.show()
app.exec()