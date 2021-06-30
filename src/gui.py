from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import re, os

from app import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):       
        super(MainWindow, self).__init__(*args, *kwargs)
        self.setWindowTitle("Slitherlink")

        self.edited = False
#region
        #Title
        titleText = QLabel()
        titleText.setText("Slithelink")
        titleText.setAlignment(Qt.AlignHCenter)
        titleText.setFont(QFont('Century',30))

        titleButton = QPushButton()
        titleButton.setFixedSize(120,40)
        titleButton.setText("Info")
        titleButton.setFont(QFont('Century',12))
        titleButton.setStyleSheet("background-color: rgb(220,220,225);")
        titleButton.clicked.connect(self.infoWindow)

        titleLayout = QHBoxLayout()
        titleLayout.addWidget(titleText)
        titleLayout.addWidget(titleButton)
        titleLayoutW = QWidget()
        titleLayoutW.setLayout(titleLayout)

        #File
        fileText = QLabel()
        fileText.setText("Wybierz plik z wartościami:")
        fileText.setFont(QFont('Century',16))

        self.filePath = QLineEdit()
        self.filePath.setReadOnly(True)
        self.filePath.setText("")
        self.filePath.setStyleSheet("background-color: rgb(220,220,225);")
        self.filePath.setFont(QFont('Lucida Console',10))

        self.fileButton = QPushButton()
        self.fileButton.setFixedSize(120,40)
        self.fileButton.setText("Wybierz plik")
        self.fileButton.setFont(QFont('Century',12))
        self.fileButton.setStyleSheet("background-color: rgb(220,220,225);")
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

        #Custom grid
        widthLabel = QLabel()
        widthLabel.setText("Szerokość:")
        widthLabel.setFont(QFont('Century',16))

        self.widthSpin = QSpinBox()
        self.widthSpin.setFont(QFont('Century',12))
        self.widthSpin.setStyleSheet("background-color: rgb(220,220,225);")
        self.widthSpin.setRange(2,12)

        heightLabel = QLabel()
        heightLabel.setText("Wysokość:")
        heightLabel.setFont(QFont('Century',16))

        self.heightSpin = QSpinBox()
        self.heightSpin.setFont(QFont('Century',12))
        self.heightSpin.setStyleSheet("background-color: rgb(220,220,225);")
        self.heightSpin.setRange(2,12)

        customButton = QPushButton()
        customButton.setFixedSize(120,40)
        customButton.setFont(QFont('Century',12))
        customButton.setText("Stwórz planszę")
        customButton.setStyleSheet("background-color: rgb(220,220,225);")
        customButton.clicked.connect(self.customButtonClicked)

        customLayout = QHBoxLayout()
        customLayout.addWidget(widthLabel)
        customLayout.addWidget(self.widthSpin)
        customLayout.addWidget(heightLabel)
        customLayout.addWidget(self.heightSpin)
        customLayout.addWidget(customButton)
        customLayoutW = QWidget()
        customLayoutW.setLayout(customLayout)

        #Magic button
        self.solveButton = QPushButton()
        self.solveButton.setText("ROZWIĄŻ")
        self.solveButton.setFont(QFont('Century',10))
        self.solveButton.setStyleSheet("background-color: rgb(220,220,225);")
        self.solveButton.setDisabled(True)
        self.solveButton.clicked.connect(self.solveButtonClicked)

        #Status label
        self.statusLabel = QLabel()
        self.statusLabel.setAlignment(Qt.AlignHCenter)
        self.statusLabel.setText("")
        self.statusLabel.setFont(QFont('Century',16))
        
        self.up = QVBoxLayout()
        self.up.addWidget(titleLayoutW)
        self.up.addWidget(fileLayoutW)
        self.up.addWidget(customLayoutW)
        self.up.addWidget(self.solveButton)
        self.up.addWidget(self.statusLabel)
        self.up.addStretch()
        self.upW = QWidget()
        self.upW.setLayout(self.up)

#endregion

        self.main = QVBoxLayout()
        self.main.addWidget(self.upW)
        
        mainW = QWidget()
        mainW.setLayout(self.main)
        self.setCentralWidget(mainW)

    def createGrid(self):
        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignCenter)

        self.colCounter = 1
        self.rowCounter = 1
        for i in range(0,self.matrix.n):
            self.createRowPoints()
            self.rowCounter+=1
            self.createRowValues()
            self.rowCounter+=1
        self.createRowPoints()

        self.gridW = QWidget()
        self.gridW.setLayout(self.grid)
        self.gridW.setStyleSheet("background-color:white;")
        
        width = self.matrix.m*50+20
        height = self.matrix.n*50+20
        self.gridW.setFixedSize(width, height)    

        self.removeGrid()

        self.gridVert = QHBoxLayout()
        self.gridVert.addWidget(QLabel())
        self.gridVert.addWidget(self.gridW)
        self.gridVert.addWidget(QLabel())
        self.gridVertW = QWidget()
        self.gridVertW.setLayout(self.gridVert)

        self.down = QVBoxLayout()
        self.down.addWidget(self.gridVertW)
        self.down.addStretch()
        self.downW = QWidget()
        self.downW.setLayout(self.down)

        self.main.addWidget(self.downW)

    def createRowPoints(self):
        self.grid.addWidget(Point(), int(self.rowCounter), int(self.colCounter))
        for i in range(self.matrix.m):
            self.colCounter+=2
            self.grid.addWidget(Point(), int(self.rowCounter), int(self.colCounter))
        self.colCounter = 1

    def createRowValues(self):
        self.colCounter+=1
        valueColCounter = 0
        for i in range(self.matrix.m):
            val = self.matrix.GetValue(int((self.rowCounter/2)-1), valueColCounter)
            if val is None:
                val = ""   

            self.grid.addWidget(Value(val, int((self.rowCounter/2)-1), valueColCounter), int(self.rowCounter), int(self.colCounter))
            self.colCounter+=2
            valueColCounter+=1
        self.colCounter = 1
    
    def removeGrid(self):
        if len(self.main) > 1:   
            self.main.itemAt(1).widget().setParent(None)

    def fileButtonClicked(self):
        self.fileDialog.show()

        if self.fileDialog.exec():
            files = self.fileDialog.selectedFiles()
            self.filePath.setText(files[0])
            self.matrix = load(files[0])
            if self.matrix is None:
                self.statusLabel.setText("Nieprawidłowy format pliku")
                self.removeGrid()
                self.solveButton.setDisabled(True)
            elif (self.matrix.n < 2 or self.matrix.n > 12):
                self.statusLabel.setText("Nieprawidłowe wymiary macierzy")
                self.removeGrid()
                self.solveButton.setDisabled(True)
            elif (self.matrix.m < 2 or self.matrix.m > 12):
                self.statusLabel.setText("Nieprawidłowe wymiary macierzy")
                self.removeGrid()
                self.solveButton.setDisabled(True)
            else:
                self.statusLabel.setText("")
                self.solveButton.setDisabled(False)
                self.createGrid()

    def customButtonClicked(self):
        self.matrix = Matrix(self.heightSpin.value(), self.widthSpin.value())
        self.statusLabel.setText("")
        self.filePath.setText("")
        self.solveButton.setDisabled(False)
        self.createGrid()

    def solveButtonClicked(self):
        if self.edited:
            self.createGrid()

        self.edited = False
        result = run(self.matrix)
        if result is None:
            self.statusLabel.setText("Nie znaleziono rozwiązania")
        else:
            self.statusLabel.setText("Znaleziono rozwiązanie")
            self.coordsV, self.coordsH, solution = result
            self.convertEdgesV()
            self.convertEdgesH()

    def convertEdgesV(self):
        for edge in self.coordsV:
            if edge is not None:
                self.grid.addWidget(EdgeVertical(), edge[0]*2+2, edge[1]*2+1)

    def convertEdgesH(self):
        for edge in self.coordsH:
            if edge is not None:
                self.grid.addWidget(EdgeHorizontal(), edge[0]*2+1, edge[1]*2+2)

    def infoWindow(self):
        infoW = QMessageBox()
        infoW.setWindowTitle("Slitherlink")
        infoW.setWindowIcon(QIcon('Icons/info.png'))
        infoW.setStyleSheet("QLabel{min-width: 450px;}")
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
        self.setFixedSize(3,38)
        self.setStyleSheet("background-color:black;")

class EdgeHorizontal(QLabel):
    def __init__(self, parent = None):
        super(QLabel, self).__init__(parent)
        self.setFixedSize(38,3)
        self.setStyleSheet("background-color:black;")
    
class Value(QLabel):
    def __init__(self, value, rowPos, colPos, parent = None):
        super(QLabel, self).__init__(parent)
        self.setFixedSize(38,38)
        self.setAlignment(Qt.AlignCenter)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont('Lucida Console',16))
        self.setText(str(value))

        self.rowPos = rowPos
        self.colPos = colPos
    
        self.mousePressEvent = self.clickedEvent
    
    def clickedEvent(self, event):
        if self.text() == "3":
            newValue = ""
            window.matrix.SetValue(self.rowPos, self.colPos, None)
        elif self.text() == "":
            newValue = 0
            window.matrix.SetValue(self.rowPos, self.colPos, newValue)
        else:
            newValue = int(self.text())+1
            window.matrix.SetValue(self.rowPos, self.colPos, newValue)
        self.setText(str(newValue))
        window.edited = True
        
#App and window initialization
guiapp = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(850, 950)
window.setStyleSheet("background-color: rgb(204,204,225);")
window.show()

guiapp.exec_()