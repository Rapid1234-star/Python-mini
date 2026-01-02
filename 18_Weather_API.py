#API-44a8b7ab1b48bc3fda90f8aa8ba4a1c9
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("70", self)
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Sunny", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_Label")
        self.city_input.setObjectName("city_Input")
        self.temperature_label.setObjectName("temperature_Label")
        self.emoji_label.setObjectName("emoji_Label")
        self.description_label.setObjectName("description_Label")
        self.get_weather_button.setObjectName("get_Weather_Button")

        self.setStyleSheet("""
    QWidget {
        background-color: #eef2f7;
        font-family: Arial, Helvetica, sans-serif;
    }

    QLabel#city_Label {
        font-size: 22px;
        font-weight: bold;
        color: #333333;
        margin-top: 15px;
    }

    QLineEdit#city_Input {
        font-size: 20px;
        padding: 10px;
        border: 2px solid #4a90e2;
        border-radius: 10px;
        background-color: white;
        margin: 10px 30px;
    }

    QLineEdit#city_Input:focus {
        border: 2px solid #2c6ed5;
    }

    QPushButton#get_Weather_Button {
        font-size: 22px;
        padding: 12px;
        margin: 15px 40px;
        background-color: #4a90e2;
        color: white;
        border: none;
        border-radius: 12px;
    }

    QPushButton#get_Weather_Button:hover {
        background-color: #357abd;
    }

    QPushButton#get_Weather_Button:pressed {
        background-color: #2c6ed5;
    }

    QLabel#temperature_Label {
        font-size: 64px;
        font-weight: bold;
        color: #222222;
        margin-top: 20px;
    }

    QLabel#emoji_Label {
        font-size: 72px;
        margin: 10px 0px;
    }

    QLabel#description_Label {
        font-size: 26px;
        color: #555555;
        margin-bottom: 20px;
    }
""")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
