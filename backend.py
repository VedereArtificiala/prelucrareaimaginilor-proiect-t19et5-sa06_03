import sys, os
from proccesing import segmentRows

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, \
    QMainWindow
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QPixmap
from mainwindow import Ui_MainWindow
import cv2 as cv


class AppDemo(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setAcceptDrops(True)
        self.label_drag_drop.setStyleSheet("QLabel {border:3px dashed #aaa}")
        self.pushButton_prelucrare.clicked.connect(self.apasama)
        self.file_path = ""

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.file_path=file_path
            self.label_nume_imagine.setText("Nume imagine -- " + str(file_path).split('/')[-1])
            self.label_drag_drop.setPixmap(QPixmap(file_path))
            event.accept()
        else:
            event.ignore()

    def apasama(self):
        print('Hei,m-ai apasat')
        print(self.file_path)
        new_image = None
        print(os.getcwd())
        if self.file_path != '':
            segmentRows(self.file_path, os.getcwd())
            #threshold, new_image = cv.threshold(cv.imread(self.file_path), 128,255, cv.THRESH_BINARY)
            #cv.imshow('fereastra',new_image)
            #cv.imwrite(f'{os.getcwd()}/bin_img.jpg',new_image)
            #self.label_drag_drop.setPixmap(QPixmap(f'{os.getcwd()}/bin_img.jpg'))
            #os.remove(f'{os.getcwd()}/bin_img.jpg')