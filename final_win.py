from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget,QVBoxLayout,QHBoxLayout
# app = QApplication([])
# main_win = QWidget()
# main_win.setWindowTitle('Здоровье')
# main_win.move(900,70)
# main_win.resize(600,500)
# vline = QVBoxLayout()
# text1 = QLabel('Индекс Руфье: 4.8')
# text2 = QLabel('Работа способность сердца: выше среднего')
# vline.addWidget(text1, alignment = Qt.AlignCenter)
# vline.addWidget(text2, alignment = Qt.AlignCenter)
# main_win.setLayout(vline)
# main_win.show()
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.setUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle('Здоровье')
        self.move(900,70)
        self.resize(600,500)
    def setUI(self):
        self.vline = QVBoxLayout()
        self.text1 = QLabel('Индекс Руфье: 4.8')
        self.text2 = QLabel('Работа способность сердца: выше среднего')
        self.vline.addWidget(self.text1, alignment = Qt.AlignCenter)
        self.vline.addWidget(self.text2, alignment = Qt.AlignCenter)
        self.setLayout(self.vline)
# FinalWin()
# app.exec_()