from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import (QLabel, QTextEdit, QWidget)
from ImagePrint import Thread

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Bokdol AppView'
        self.initUI()

    @pyqtSlot(QImage)
    def setImage(self, image):
        # 메인화면 출력
        self.label.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def setStatusImage(self, image):
        #상태창 출력
        self.statuslabel.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def setCoordImage(self, image):
        #좌표창 출력
        self.coordlabel.setPixmap(QPixmap.fromImage(image))

    def initUI(self):
        #윈도우 타이틀, 창 배경
        self.setWindowTitle(self.title)
        self.setStyleSheet('background:#B7DEFB')
        self.setGeometry(800, 400, 600, 400)

        #화면 출력창
            #전체창
        self.label = QLabel(self)
        self.label.setGeometry(10, 190, 300, 199)
            #상태창
        self.statuslabel = QLabel(self)
        self.statuslabel.setGeometry(350, 175, 180, 60)
            #좌표
        self.coordlabel = QLabel(self)
        self.coordlabel.setGeometry(350, 245, 180, 60)
            #채팅

        #인공지능 상태창, 입력창
        StatusWindow = QTextEdit(self)
        StatusWindow.setGeometry(10, 20, 300, 150)
        StatusWindow.setStyleSheet('background:#FFFFFF')
        InputEdit = QTextEdit(self)
        InputEdit.setGeometry(350, 20, 240, 150)
        InputEdit.setStyleSheet('background:#FFFFFF')

        #화면 갱신
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.changeStatusPixmap.connect(self.setStatusImage)
        th.changeCoordPixmap.connect(self.setCoordImage)
        th.start()
