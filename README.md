# PyQt Examples 2019

Learn to create desktop apps with Python and Qt. Screenshots on Ubuntu below. You can also use Windows or macOS.

| <a href="src/01 PyQt QLabel"><img src="src/01 PyQt QLabel/pyqt-qlabel.png" alt="PyQt QLabel" width=100px></a> | <a href="src/02 PyQt Widgets"><img src="src/02 PyQt Widgets/pyqt-widgets.png" alt="PyQt widgets screenshot" width=200px></a> | <a href="src/03 QVBoxLayout PyQt5"><img src="src/03 QVBoxLayout PyQt5/qvboxlayout-pyqt5.png" alt="QVBoxLayout PyQt5" width=100px></a> | <a href="src/04 PyQt Signals and Slots"><img src="src/04 PyQt Signals and Slots/pyqt-signals-and-slots.jpg" alt="PyQt Signals and Slots" width=170px></a> | <a href="src/05 Qt Designer Python"><img src="src/05 Qt Designer Python/qt-designer-windows.png" alt="Qt Designer Python" width=190px></a> |
| :--: | :--: | :--: | :--: | :--: |
| <a href="src/01 PyQt QLabel">Hello World!</a> | <a href="src/02 PyQt Widgets">Common PyQt Widgets</a> | <a href="src/03 QVBoxLayout PyQt5">Layouts</a> | <a href="src/04 PyQt Signals and Slots">Signals and Slots</a> | <a href="src/04 Qt Designer Python">Qt Designer & Python</a> |

| <a href="src/06 QML Python example"><img src="src/06 QML Python example/qml-python-example.png" alt="QML Python example" width=200px></a> | <a href="src/07 Qt Text Editor"><img src="src/07 Qt Text Editor/screenshots/qt-text-editor.png" alt="Qt Text Editor" width=180px></a> | <a href="src/08 PyQt5 exe"><img src="src/08 PyQt5 exe/pyqt5-exe.png" alt="PyQt5 exe" width=213px></a> | <a href="src/09 Qt dark theme"><img src="src/09 Qt dark theme/qt-dark-theme.png" alt="Qt dark theme" width=180px></a> |
| :--: | :--: | :--: | :--: |
| <a href="src/06 QML Python example">QML Python example</a> | <a href="src/07 Qt Text Editor">Qt Text Editor</a> | <a href="src/08 PyQt5 exe">Packaging & deployment</a> | <a href="src/09 Qt dark theme">Qt Dark Theme</a> |

| <a href="src/10 QPainter Python example"><img src="src/10 QPainter Python example/qpainter-python-example.png" alt="QPainter Python example" width=200px></a> | <a href="src/11 PyQt Thread example"><img src="src/11 PyQt Thread example/pyqt-thread-example.png" alt="PyQt Thread example" width=175px></a> | <a href="src/12 QTreeView example in Python"><img src="src/12 QTreeView example in Python/qtreeview-example-in-python.png" alt="QTreeView example in Python" width=260px></a> | <a href="src/13 PyQt5 QListView"><img src="src/13 PyQt5 QListView/pyqt5-qlistview.png" alt="PyQt5 QListView" width=138px></a> |
| :--: | :--: | :--: | :--: |
| <a href="src/10 QPainter Python example">Action Shooter</a> | <a href="src/11 PyQt Thread example">Chat Client</a> | <a href="src/12 QTreeView example in Python">Tree Views</a> | <a href="src/13 PyQt5 QListView">Lists</a> |

| <a href="src/14 QAbstractTableModel example"><img src="src/14 QAbstractTableModel example/qabstracttablemodel-example.png" alt="QAbstractTableModel example" height=120px></a> | <a href="src/15 PyQt database example"><img src="src/15 PyQt database example/pyqt-database-example.png" alt="QAbstractTableModel example" height=120px></a> |
| :--: | :--: |
| <a href="src/14 QAbstractTableModel example">Custom Tables</a> |  <a href="src/15 PyQt database example">PyQt database example</a> |

## Running the examples

Running the examples is really easy. The only thing you need is Python 3.

First, download the [ZIP archive of this repository](https://github.com/1mh/pyqt-examples/archive/_.zip) and unpack it. Open a command prompt and use `cd` to navigate into the top-level directory of the archive.

Create a virtual environment via the command:

    python3 -m venv venv

This creates the folder `venv/` in your current directory. It will contain the necessary libraries for running the examples.

To activate the virtual environment, use the following command:

```
# On Windows:
call venv\Scripts\actviate.bat
# On Mac / Linux:
source venv/bin/activate
```

Now execute the following to install the necessary dependencies:

    pip install -Ur src/requirements.txt

Once you have done this, use `cd` to navigate to the example you're interested in in the [`src/`](src) folder. For example:

    cd "src/01 PyQt QLabel"

You'll find a `.py` file there, typically `main.py`. You can run it with the command:

    python main.py

Please note that the virtual environment must still be active for this to work.

## Using PySide2

This repository uses PyQt5 to use Qt from Python. Another, alternative binding is PySide2 (also called "Qt for Python"). It is less mature than PyQt5 but has the advantage that you can use it for free in commercial projects.

If you want to use PySide2 instead of PyQt5, simply replace all mentions of the latter by the former. For instance, in [`src/requirements.txt`](src/requirements.txt), replace `PyQt5` by `PySide2`. Similarly for any code examples: `from PyQt5.QtWidgets ...` becomes `from PySide2.QtWidgets ...` etc.

## License

Except where otherwise indicated, the contents here are © me, Michael Herrmann. I'm happy for you to use the source code under the terms of the MIT license. The screenshots may be used under the terms of the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
