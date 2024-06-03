from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel
from PyQt5.QtCore import Qt
import sys
from gpiozero import PWMLED

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("Control LED Intensity")
        self.initUI()

    def initUI(self):
        # Slider for White LED
        self.white_label = QLabel("White LED", self)
        self.white_label.setGeometry(50, 50, 100, 20)

        self.white_slider = QSlider(Qt.Horizontal, self)
        self.white_slider.setGeometry(50, 80, 300, 20)
        self.white_slider.setMinimum(0)
        self.white_slider.setMaximum(100)
        self.white_slider.valueChanged.connect(self.white_slider_changed)

        # Slider for Blue LED
        self.blue_label = QLabel("Blue LED", self)
        self.blue_label.setGeometry(50, 110, 100, 20)

        self.blue_slider = QSlider(Qt.Horizontal, self)
        self.blue_slider.setGeometry(50, 140, 300, 20)
        self.blue_slider.setMinimum(0)
        self.blue_slider.setMaximum(100)
        self.blue_slider.valueChanged.connect(self.blue_slider_changed)

        # Slider for Red LED
        self.red_label = QLabel("Red LED", self)
        self.red_label.setGeometry(50, 170, 100, 20)

        self.red_slider = QSlider(Qt.Horizontal, self)
        self.red_slider.setGeometry(50, 200, 300, 20)
        self.red_slider.setMinimum(0)
        self.red_slider.setMaximum(100)
        self.red_slider.valueChanged.connect(self.red_slider_changed)

        # Exit button
        self.exit_button = QtWidgets.QPushButton("EXIT", self)
        self.exit_button.setGeometry(150, 300, 100, 30)
        self.exit_button.clicked.connect(self.close)

        # Initialize PWMLED objects
        self.white_led = PWMLED(17)
        self.blue_led = PWMLED(27)
        self.red_led = PWMLED(22)

    def white_slider_changed(self):
        value = self.white_slider.value() / 100
        self.white_led.value = value
        print(f"White LED Intensity: {value}")

    def blue_slider_changed(self):
        value = self.blue_slider.value() / 100
        self.blue_led.value = value
        print(f"Blue LED Intensity: {value}")

    def red_slider_changed(self):
        value = self.red_slider.value() / 100
        self.red_led.value = value
        print(f"Red LED Intensity: {value}")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
