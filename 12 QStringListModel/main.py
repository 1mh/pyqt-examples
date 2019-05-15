from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel

app = QApplication([])
model = QStringListModel(["H", "e", "l", "l", "o", "!"])
view = QListView()
view.setModel(model)
view.show()
app.exec_()