# PyQt Examples

A collection of small desktop applications to help you learn PyQt5.

| <a href="src/01 PyQt QLabel"><img src="src/01 PyQt QLabel/pyqt-qlabel.png" alt="PyQt QLabel" width=100px></a> | <a href="src/02 PyQt Widgets"><img src="src/02 PyQt Widgets/pyqt-widgets.png" alt="PyQt widgets screenshot" width=200px></a> | <a href="src/03 QVBoxLayout PyQt5"><img src="src/03 QVBoxLayout PyQt5/qvboxlayout-pyqt5.png" alt="QVBoxLayout PyQt5" width=100px></a> | <a href="src/04 PyQt Signals and Slots"><img src="src/04 PyQt Signals and Slots/pyqt-signals-and-slots.jpg" alt="PyQt Signals and Slots" width=180px></a> | <a href="src/05 Qt Designer Python"><img src="src/05 Qt Designer Python/qt-designer-python.png" alt="Qt Designer Python" width=180px></a> |
| :--: | :--: | :--: | :--: | :--: |
| <a href="src/01 PyQt QLabel">Hello World</a> | <a href="src/02 PyQt Widgets">Common PyQt Widgets</a> | <a href="src/03 QVBoxLayout PyQt5">Layouts</a> | <a href="src/04 PyQt Signals and Slots">Signals and Slots</a> | <a href="src/04 Qt Designer Python">Qt Designer & Python</a> |

| <a href="src/06 QML Python example"><img src="src/06 QML Python example/qml-python-example.png" alt="QML Python example" width=200px></a> |
| :--: |
| <a href="src/06 QML Python example">QML Python example</a> |

## Running the examples

You can run the examples on Windows, Mac and Linux. The only thing you need is Python 3. Create a virtual environment via the command:

    python3 -m venv venv

This creates the folder `venv/` in your current directory. It will contain the necessary libraries for running the examples.

To activate the virtual environment, use the following command:

```
# On Windows:
call venv\Scripts\actviate.bat
# On Mac / Linux:
source venv/bin/activate
```

Then, execute the following to install the necessary dependencies:

    pip install -Ur src/requirements.txt

Once you have done this, use `cd` to navigate to the example you're interested in in the [`src/`](src) folder. You'll find a `.py` file there, typically `main.py`. You can run it with the command:

    python main.py

Please note that the virtual environment must still be active for this to work.
