# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(1293, 987)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 1241, 561))
        self.groupBox.setObjectName("groupBox")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setGeometry(QtCore.QRect(30, 30, 1171, 521))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 1171, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mapLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mapLayout.setContentsMargins(0, 0, 0, 0)
        self.mapLayout.setObjectName("mapLayout")
        self.startBtn = QtWidgets.QPushButton(self.tab)
        self.startBtn.setGeometry(QtCore.QRect(1230, 840, 51, 31))
        self.startBtn.setObjectName("startBtn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 560, 1211, 391))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cameraView1 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.cameraView1.setGeometry(QtCore.QRect(30, 30, 371, 351))
        self.cameraView1.setObjectName("cameraView1")
        self.cameraView2 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.cameraView2.setGeometry(QtCore.QRect(430, 30, 371, 351))
        self.cameraView2.setObjectName("cameraView2")
        self.cameraView3 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.cameraView3.setGeometry(QtCore.QRect(830, 30, 371, 351))
        self.cameraView3.setObjectName("cameraView3")
        self.pauseBtn = QtWidgets.QPushButton(self.tab)
        self.pauseBtn.setGeometry(QtCore.QRect(1230, 880, 51, 31))
        self.pauseBtn.setObjectName("pauseBtn")
        self.stopBtn = QtWidgets.QPushButton(self.tab)
        self.stopBtn.setGeometry(QtCore.QRect(1230, 920, 51, 31))
        self.stopBtn.setObjectName("stopBtn")
        TabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        TabWidget.addTab(self.tab1, "")

        self.retranslateUi(TabWidget)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.groupBox.setTitle(_translate("TabWidget", "Junction Floor #1"))
        self.startBtn.setText(_translate("TabWidget", "Start"))
        self.groupBox_2.setTitle(_translate("TabWidget", "Camera Views"))
        self.pauseBtn.setText(_translate("TabWidget", "Pause"))
        self.stopBtn.setText(_translate("TabWidget", "Stop"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Tab 1"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    from slots import SlotsHandler
    from system import System

    system = System()
    slots_handler = SlotsHandler(ui, TabWidget, system)
    TabWidget.show()
    sys.exit(app.exec_())

