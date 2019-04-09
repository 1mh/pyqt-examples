from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

import sys

UIClass, QtBaseClass = uic.loadUiType("dialog.ui")

class Window(UIClass, QtBaseClass):
    def __init__(self):
        UIClass.__init__(self)
        QtBaseClass.__init__(self)
        self.setupUi(self)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())