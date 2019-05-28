from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

UIClass, QtBaseClass = uic.loadUiType("dialog.ui")

class Window(UIClass, QtBaseClass):
    def __init__(self):
        UIClass.__init__(self)
        QtBaseClass.__init__(self)
        self.setupUi(self)

app = QApplication([])
window = Window()
window.show()
app.exec_()