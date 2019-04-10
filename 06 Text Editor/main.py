from os.path import basename
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def closeEvent(self, event):
        if text.document().isModified():
            answer = QMessageBox.question(
                window, 'Text Editor',
                'You have unsaved changes. Save before closing?',
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
            )
            if answer & QMessageBox.Save:
                save()
            elif answer & QMessageBox.Cancel:
                event.ignore()

app = QApplication([])
window = MainWindow()
text = QTextEdit()
window.setCentralWidget(text)
window.setWindowTitle('Text Editor')

file_path = None

def save_as():
    global file_path
    new_path = QFileDialog.getSaveFileName(window, 'Save As', file_path)[0]
    if new_path:
        file_path = new_path
        save()

def save():
    if not file_path:
        save_as()
    else:
        with open(file_path, 'w') as f:
            f.write(text.toPlainText())
        text.document().setModified(False)

def open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window, 'Open', file_path)[0]
    if path:
        text.setPlainText(open(path).read())
        file_path = path

file_menu = window.menuBar().addMenu("&File")

open_action = QAction("&Open")
open_action.setShortcut(QKeySequence.Open)
open_action.triggered.connect(open_file)
file_menu.addAction(open_action)

save_action = QAction("&Save")
save_action.setShortcut(QKeySequence.Save)
save_action.triggered.connect(save)
file_menu.addAction(save_action)

save_as_action = QAction("Save &As...")
save_as_action.triggered.connect(save_as)
file_menu.addAction(save_as_action)

exit_action = QAction("E&xit")
exit_action.triggered.connect(window.close)
file_menu.addAction(exit_action)

help_menu = window.menuBar().addMenu("&Help")

about_action = QAction("&About")
help_menu.addAction(about_action)
help_menu.triggered.connect(lambda: QMessageBox.about(window, 'About Text Editor', '<center>'
            '<h1>Text Editor</h1>&zwnj;'
            '<img src="icon.png">'
            '</center>'
            '<p>Version 31.4.159.265358<br/>'
            'Copyright &copy; Company Inc.</p>'))

window.show()

app.exec_()