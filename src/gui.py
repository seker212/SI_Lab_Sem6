from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import re, os

# from app import *

class Okno(QMainWindow):
    def __init__(self, *args, **kwargs):       
        super(Okno, self).__init__(*args, *kwargs)
        self.setWindowTitle("Slitherlink")
#region
        #Title
        titleText = QLabel()
        titleText.setText("Slithelink")
        titleText.setAlignment(Qt.AlignHCenter)
        titleText.setFont(QFont('Lucida Console',30))

        titleButton = QPushButton()
        titleButton.setFixedSize(40,40)
        titleButton.setIcon(QIcon('Icons/info.png'))
        titleButton.clicked.connect(self.infoWindow)

        titleLayout = QHBoxLayout()
        titleLayout.addWidget(titleText)
        titleLayout.addWidget(titleButton)
        titleLayout.setAlignment(Qt.AlignTop)
        titleLayoutW = QWidget()
        titleLayoutW.setLayout(titleLayout)

        #File
        fileText = QLabel()
        fileText.setText("Wybierz plik z wartościami:")
        fileText.setFont(QFont('Lucida Console',12))

        self.filePath = QLineEdit()
        self.filePath.setReadOnly(True)
        self.filePath.setText("")
        self.filePath.setAlignment(Qt.AlignCenter)
        self.filePath.setFont(QFont('Lucida Console',10))

        self.fileButton = QPushButton()
        self.fileButton.setFixedSize(40,40)
        self.fileButton.setIcon(QIcon('Icons/folder.png'))
        self.fileButton.clicked.connect(self.fileButtonClicked)

        fileLayout = QHBoxLayout()
        fileLayout.addWidget(fileText)
        fileLayout.addWidget(self.filePath)
        fileLayout.addWidget(self.fileButton)
        fileLayoutW = QWidget()
        fileLayoutW.setLayout(fileLayout)

        #File window
        self.fileDialog = QFileDialog()
        self.fileDialog.setNameFilter("Text Files (*.txt)")
        self.fileDialog.hide()


#endregion

        self.main = QVBoxLayout()
        self.main.addWidget(titleLayoutW)
        self.main.addWidget(fileLayoutW)

        self.grid = QGridLayout()
        self.createGrid()
        new_gridW = QWidget()
        new_gridW.setLayout(self.grid)
        new_gridW.setStyleSheet("background-color:white;")
        self.main.addWidget(new_gridW)
        
        mainW = QWidget()
        mainW.setLayout(self.main)

        self.setCentralWidget(mainW)

    def createGrid(self):   
        self.colCounter = 1
        self.rowCounter = 1
        for i in range(0,5):
            self.createRowEdges(5)
            self.rowCounter+=1
            self.createRowValues(5)
            self.rowCounter+=1
        self.createRowEdges(5)

    def createRowEdges(self, colnum):
        self.grid.addWidget(Point(), int(self.rowCounter), int(self.colCounter))
        self.colCounter+=1
        for i in range(colnum):
            self.grid.addWidget(EdgeHorizontal(), int(self.rowCounter), int(self.colCounter))
            self.colCounter+=1
            self.grid.addWidget(Point(), int(self.rowCounter), int(self.colCounter))
            self.colCounter+=1
        self.colCounter = 1

    def createRowValues(self, colnum):
        self.grid.addWidget(EdgeVertical(), int(self.rowCounter), int(self.colCounter))
        self.colCounter+=1
        for i in range(colnum):
            self.grid.addWidget(Value(2), int(self.rowCounter), int(self.colCounter))
            self.colCounter+=1
            self.grid.addWidget(EdgeVertical(), int(self.rowCounter), int(self.colCounter))
            self.colCounter+=1
        self.colCounter = 1

    def fileButtonClicked(self):
        self.fileDialog.show()

        if self.fileDialog.exec():
            files = self.fileDialog.selectedFiles()
            self.filePath.setText(files[0])    

    def infoWindow(self):
        infoW = QMessageBox()
        infoW.setWindowTitle("Slitherlink")
        infoW.setWindowIcon(QIcon('Icons/info.png'))
        infoW.setStyleSheet("QLabel{min-width: 600px;}")
        f = open("info.txt", "r", encoding='utf8')
        text = f.read()
        infoW.setText(text)
        infoW.setWindowModality(Qt.ApplicationModal)
        infoW.exec_()

class Point(QLabel):
    def __init__(self, parent = None):
        super(QLabel, self).__init__(parent)
        self.setFixedSize(3,3)
        self.setStyleSheet("background-color:black;")

class EdgeVertical(QLabel):
    def __init__(self, parent = None):
        super(QLabel, self).__init__(parent)
        self.setFixedSize(3,60)
        self.setStyleSheet("background-color:black;")

class EdgeHorizontal(QLabel):
    def __init__(self, parent = None):
        super(QLabel, self).__init__(parent)
        self.setFixedSize(60,3)
        self.setStyleSheet("background-color:black;")

class Value(QLabel):
    def __init__(self, value, parent = None):
        super(QLabel, self).__init__(parent)
        self.setFixedSize(60,60)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont('Lucida Console',20))
        self.setText(str(value))
        

#App and window initialization
guiapp = QApplication(sys.argv)

window = Okno()
window.setFixedSize(800, 800)
window.setStyleSheet("background-color: rgb(220,220,220);")
window.show()

guiapp.exec_()