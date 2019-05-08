from os.path import expanduser
from PyQt5.QtWidgets import *

home_directory = expanduser('~')

app = QApplication([])
model = QFileSystemModel()
model.setRootPath(home_directory)
view = QTreeView()
view.setModel(model)
view.setRootIndex(model.index(home_directory))
view.show()
app.exec_()