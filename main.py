from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar
from PyQt5 import QtCore
from PyQt5.QtCore import QBasicTimer
import sys
#https://build-system.fman.io/qt-designer-download
numClick = 0
def butClick():
    print('lol lol lol looooooooooooool')


def mainApp():
    app = QApplication(sys.argv)    #берем настройки компа
    window = QMainWindow()          #создаем переменную для гл окна

    window.setWindowTitle('Мои программы')
    window.setGeometry(300,500, 500, 400)   # 1)отступ по х 2)отступ по у 3)ширина 4)высота
    text = QtWidgets.QLabel(window)         # создание 1 виджета
    text.setText('Надпись № 1')
    text.move(200,50)
    text.adjustSize()

    button = QtWidgets.QPushButton(window)
    button.move(150,200)
    button.setText('Кнопка №1')
    button.setFixedWidth(300)
    button.clicked.connect(butClick)
    # progress = QtWidgets.QProgressBar(window)
    # timer = QtCore.QBasicTimer()

    window.show()
    sys.exit(app.exec_())

mainApp()