# QTreeView example in Python

A _tree view_ is what's classicaly used to display files and folders: A hierarchical structure where items can be expanded. This example application shows a tree view can be used in PyQt5 to display your local files.

<p align="center"><img src="qtreeview-example-in-python.png" alt="QTreeView example in Python"></p>

To run the example, please follow [the instructions in the README of this repository](https://github.com/1mh/pyqt-examples#running-the-examples).

The data shown it the tree view comes from [`QDirModel`](https://doc.qt.io/qt-5/qdirmodel.html). This is a part of Qt's [Model/View framework](https://doc.qt.io/qt-5/model-view-programming.html). The nice thing about it is that you can visualize the same data in different ways. The next example, [PyQt5 QListview](../13%20PyQt5%20QListView), shows how this can be exploited to display your files as a list instead of a tree.