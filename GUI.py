import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QFrame, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("CrackPractic")
        self.setWindowIcon(QIcon(self.getPath("data/horse.ico")))
        self.setFixedWidth(1000)

        #переменые виджетов
        self.label = QLabel(self.getDay())
        update = QPushButton("Следущий день")
        copy = QPushButton("Скопить")
        athor = QPushButton("Автор")
        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout(self)
        self.vframe = QFrame()
        hframe = QFrame()

        #панель с кнопками
        hbox.addWidget(update)
        hbox.addWidget(copy)
        hbox.addWidget(athor)
        hframe.setLayout(hbox)

        #назначаю кнопки
        update.clicked.connect(self.updateDay)
        copy.clicked.connect(self.copyDay)

        #создание экрана
        vbox.addWidget(self.label)
        vbox.addWidget(hframe)
        self.label.setAlignment(Qt.AlignCenter)
        self.vframe.setLayout(vbox)

        self.setCentralWidget(self.vframe)

    def getDay(self):
        import json
        import random
        import re

        text = ''
        massifTem = []

        def setText(text, input):
            text = ' ' + input
            return text

        with open(self.getPath("data/dataPtactic.json"), encoding="utf8") as json_file:
            data = json.load(json_file)

        text = text + '\n ' + data['pm1'][0][1]
        text = text + '\n ' + data['pm1'][0][0]
        text = text + '\n ' + data['pm4'][1][0]
        text = text + '\n ' + data['pm4'][0][0]

        for i in range(20):
            intPm = str(random.randint(1, 5))
            intPmTema = random.randint(0, len(data['pm' + intPm]) - 1)
            if intPmTema == 0 and intPm == 1:
                intPmTema = 2
            intPmTemaWord = random.randint(0, len(data['pm' + intPm][intPmTema]) - 1)
            if data['pm' + intPm][intPmTema][intPmTemaWord] in text:
                pass
            else:
                text = text + '\n ' + data['pm' + intPm][intPmTema][intPmTemaWord]

        return(text)

    def updateDay(self):
        self.label.setText(self.getDay())
        self.setCentralWidget(self.vframe)

    def copyDay(self):
        try:
            from Tkinter import Tk
        except ImportError:
            from tkinter import Tk
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.label.text())
        r.update()  # now it stays on the clipboard after the window is closed
        r.destroy()

    def getPath(self, relative_path):
        import os, sys
        """ Get absolute path to resource, works for dev and for PyInstaller """
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.getcwd()
        return os.path.join(base_path, relative_path)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
