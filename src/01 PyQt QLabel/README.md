# PyQt QLabel

The code below gives an example of how Qt's `QLabel` can be used to create a very simple Hello World app:

![PyQt QLabel screenshot](pyqt-qlabel.png)

```
from PyQt5.QtWidgets import *
app = QApplication([])
label = QLabel('Hello World!')
label.show()
app.exec_()
```

The source code is also in [`main.py`](main.py). For instructions how to run it, please see [here](https://github.com/1mh/pyqt-examples#running-the-examples).
