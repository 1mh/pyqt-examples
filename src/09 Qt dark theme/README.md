# Qt Dark Theme

This example shows how Qt's style mechanisms can be used to set a dark theme. It adapts the text editor from [example 7](../07%20Qt%20Text%20Editor).

![Qt Dark Theme](qt-dark-theme.png)

As you can see in [`main.py`](main.py), this example uses `QApplication.setStyle(...)` and a `QPalette` to change the application's colors:

    # Force the style to be the same on all OSs:
    app.setStyle("Fusion")

    # Now use a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    ...
    app.setPalette(palette)

To run this example yourself, please follow the [instructions in the main README of this repository](https://github.com/1mh/pyqt-examples#running-the-examples).
