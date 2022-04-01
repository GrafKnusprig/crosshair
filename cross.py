import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Crosshair(QtWidgets.QWidget):
    def __init__(self, parent=None, windowSize=24, penWidth=2):
	#hunt showdown needs 108 pixels
        offset = int(sys.argv[1]) if len(sys.argv)>1 else 0
        QtWidgets.QWidget.__init__(self, parent)
        self.ws = windowSize
        self.resize(windowSize+1, windowSize+1)
        self.pen = QtGui.QPen(QtGui.QColor(255,51,255,255))                
        self.pen.setWidth(penWidth)                                            
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center() + QtCore.QPoint(1,1 + offset))


    def paintEvent(self, event):
        ws = self.ws
        d = 6
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        # painter.drawLine( x1,y1, x2,y2    )
        painter.drawLine(int(ws/2), 0, int(ws/2), int(ws/2 - ws/d))   # Top
        painter.drawLine(int(ws/2), int(ws/2 + ws/d), int(ws/2) , ws)   # Bottom
        painter.drawLine(0, int(ws/2), int(ws/2 - ws/d), int(ws/2))   # Left
        painter.drawLine(int(ws/2 + ws/d), int(ws/2), ws, int(ws/2))   # Right


app = QtWidgets.QApplication(sys.argv) 

widget = Crosshair(windowSize=24, penWidth=1)
widget.show()

sys.exit(app.exec_())
