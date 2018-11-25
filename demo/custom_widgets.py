from gui_utils import cvt_numpy_to_qscene

from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui

import cv2
import random


class MapField(QtWidgets.QWidget):
    def __init__(self, img_shape, parent=None):
        super(MapField, self).__init__(parent)
        self._img_shape = img_shape
        self._points = []

    def add_point(self, x, y, color):
        self._points.append({'x': x, 'y': y, 'color': color})
        self.update()

    def clear_points(self):
        self._points = []
        self.update()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        size = self.size()
        qp.setPen(QtCore.Qt.black)

        for point in self._points:
            x = (size.width() - self._img_shape[1]) // 2 + point['x']
            y = point['y']
            color = point['color']

            br = QtGui.QBrush(QtGui.QColor(*color))
            qp.setBrush(br)

            qp.drawEllipse(QtCore.QPoint(x, y), 10, 10)

        # for i in range(1000):
        #     x = random.randint((size.width() - self._img_shape[1]) // 2,
        #                        (size.width() - self._img_shape[1]) // 2 + self._img_shape[1])
        #     y = random.randint(1, size.height() - 1)
        #     qp.drawEllipse(QtCore.QPoint(x, y), 10, 10)
