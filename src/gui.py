from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import re, os

from app import *

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
        titleLayoutW = QWidget()
        titleLayoutW.setLayout(titleLayout)

        #File
        fileText = QLabel()
        fileText.setText("Wybierz plik z wartościami:")
        fileText.setFont(QFont('Lucida Console',12))

        self.filePath = QLineEdit()
        self.filePath.setReadOnly(True)
        self.filePath.setText("")
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

        #Magic button
        self.solveButton = QPushButton()
        self.solveButton.setText("DO MAGIC")
        self.solveButton.clicked.connect(self.solveButtonClicked)

#endregion

        self.main = QVBoxLayout()
        self.main.addWidget(titleLayoutW)
        self.main.addWidget(fileLayoutW)
        self.main.addWidget(self.solveButton)
        self.main.addStretch()
        
        mainW = QWidget()
        mainW.setLayout(self.main)
        self.setCentralWidget(mainW)

    def createGrid(self):
        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignHCenter)

        self.colCounter = 1
        self.rowCounter = 1
        for i in range(0,self.matrix.n):
            self.createRowEdges()
            self.rowCounter+=1
            self.createRowValues()
            self.rowCounter+=1
        self.createRowEdges()

        self.gridW = QWidget()
        self.gridW.setLayout(self.grid)
        width = self.matrix.m*55
        height = self.matrix.n*55
        self.gridW.setFixedSize(width, height)
        self.gridW.setStyleSheet("background-color:white;")

        if len(self.main) > 4:
            self.main.itemAt(4).widget().setParent(None)
        self.main.addWidget(self.gridW)

    def createRowEdges(self):
        self.grid.addWidget(Point(), int(self.rowCounter), int(self.colCounter))
        self.colCounter+=1
        for i in range(self.matrix.m):
            self.grid.addWidget(EdgeHorizontal(), int(self.rowCounter), int(self.colCounter))
            self.colCounter+=1
            self.grid.addWidget(Point(), int(self.rowCounter), int(self.colCounter))
            self.colCounter+=1
        self.colCounter = 1

    def createRowValues(self):
        self.grid.addWidget(EdgeVertical(), int(self.rowCounter), int(self.colCounter))
        self.colCounter+=1
        valueColCounter = 0
        for i in range(self.matrix.m):
            val = self.matrix.GetValue(int((self.rowCounter/2)-1), valueColCounter)
            if val is None:
                val = ""
            valueColCounter+=1
            self.grid.addWidget(Value(val), int(self.rowCounter), int(self.colCounter))
            self.colCounter+=1
            self.grid.addWidget(EdgeVertical(), int(self.rowCounter), int(self.colCounter))
            self.colCounter+=1
        self.colCounter = 1
    
    def solveButtonClicked(self):
        run(self.matrix)

    #TODO: add validation of file:
    # Matrix size

    def fileButtonClicked(self):
        self.fileDialog.show()

        if self.fileDialog.exec():
            files = self.fileDialog.selectedFiles()
            self.filePath.setText(files[0])

            self.matrix = load(files[0])
            if (self.matrix.n < 2 or self.matrix.n > 15):
                pass #TODO: Error
            if (self.matrix.m < 2 or self.matrix.m > 15):
                pass #TODO: Error
            
            self.createGrid()

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

class Edge(QLabel):
    def __init__(self, parent = None):
        super(QLabel, self).__init__(parent)
        self.setStyleSheet("background-color:black;")
        self.setVisible = False

    def SetVisible(self):
        self.setVisible = True

class EdgeVertical(Edge):
    def __init__(self, parent = None):
        super(Edge, self).__init__(parent)
        self.setFixedSize(3,40)

class EdgeHorizontal(Edge):
    def __init__(self, parent = None):
        super(Edge, self).__init__(parent)
        self.setFixedSize(40,3)
    
class Value(QLabel):
    def __init__(self, value, parent = None):
        super(QLabel, self).__init__(parent)
        self.setFixedSize(40,40)
        self.setAlignment(Qt.AlignCenter)
        # self.setStyleSheet("background-color:blue;")
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont('Lucida Console',16))
        self.setText(str(value))
        
#App and window initialization
guiapp = QApplication(sys.argv)

window = Okno()
window.setFixedSize(850, 850)
window.setStyleSheet("background-color: rgb(220,220,220);")
window.show()

guiapp.exec_()