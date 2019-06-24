# QML Python example

Qt can be broadly split into two technologies: _Qt Widgets_ is the old core. It displays GUI elements in a way that is typical for operating systems such as Windows or macOS. A more recent alternative is _Qt Quick_. This technology is optimized for mobile and touch screen devices. It is better suited for very custom graphics and fluid animations.

Qt Quick uses a markup language called QML. This example shows how you can combine QML with Python.

<p align="center"><img src="qml-python-example.png" alt="QML Python Example"></p>

The sample application displays a pin wheel in front of some hills. When you click with the mouse, the wheel rotates.

The QML code lies in [`main.qml`](main.qml). It is invoked from Python via [`main.py`](main.py). For instructions how to run it, please see [here](https://github.com/1mh/pyqt-examples#running-the-examples).

Some code in this directory has special license requirements. For more information, please see [`LICENSE.md`](LICENSE.md).
