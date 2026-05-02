from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget,QVBoxLayout,QHBoxLayout
# from second_win import SecondWin
app = QApplication([])
# main_win = QWidget()
# main_win.setWindowTitle('Здоровье')
# main_win.move(900,70)
# main_win.resize(600,500)
# linev1 = QVBoxLayout()
# text1 = QLabel('Добро пожаловать в программу по определению состоянию здоровья!')
# text2 = QLabel('Данное предложение поможет вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\nПроба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки  работоспособности сердца при физическорй нагрузке.\nУ испытуемого, находящегося в положении лежа на спине в течении 5 мин, определяют его частоту пульса за 15 секунд, а потом - за последние 15 секунд первой минуты периода восстановдения.\nВажно! Если в процессе проведения испытания вы почувствцете себя плохо (появится шоловокружение, шум в ушах и др.), то тест необходимо прервать и обратиться к врачу')
# button1 = QPushButton('Начать')
# linev1.addWidget(text1, alignment = Qt.AlignCenter)
# linev1.addWidget(text2, alignment = Qt.AlignCenter)
# linev1.addWidget(button1, alignment = Qt.AlignCenter)
# main_win.setLayout(linev1)
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.setUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle('Здоровье')
        self.move(900,70)
        self.resize(600,500)
    def setUI(self):
        self.linev1 = QVBoxLayout()
        self.text1 = QLabel('Добро пожаловать в программу по определению состоянию здоровья!')
        self.text2 = QLabel('Данное предложение поможет вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\nПроба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки  работоспособности сердца при физическорй нагрузке.\nУ испытуемого, находящегося в положении лежа на спине в течении 5 мин, определяют его частоту пульса за 15 секунд, а потом - за последние 15 секунд первой минуты периода восстановдения.\nВажно! Если в процессе проведения испытания вы почувствцете себя плохо (появится шоловокружение, шум в ушах и др.), то тест необходимо прервать и обратиться к врачу')
        self.button1 = QPushButton('Начать')
        self.linev1.addWidget(self.text1, alignment = Qt.AlignCenter)
        self.linev1.addWidget(self.text2, alignment = Qt.AlignCenter)
        self.linev1.addWidget(self.button1, alignment = Qt.AlignCenter)
        self.setLayout(self.linev1)
    def button_click(self):
        self.hide()
        # SecondWin()
    def connects(self):
        pass
        # self.button1.clicked.connect(self.button_click)
MainWin()
# main_win.show()
app.exec_()
