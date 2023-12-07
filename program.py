import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import (QApplication,
                             QWidget)
from ui_file import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 400)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event) -> None:
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        color = QColor(r, g, b)
        qp.setPen(color)
        d = randint(0, 195)
        qp.drawEllipse(100, 100, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
