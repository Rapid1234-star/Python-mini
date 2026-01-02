import os
import sys

import requests
from dotenv import load_dotenv
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

load_dotenv()


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.setGeometry(600, 300, 400, 500)
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

        self.setStyleSheet(
            """
QWidget {
    background-color: #eef2f7;
    font-family: 'Segoe UI', Arial, sans-serif;
}

/* ---- City Label ---- */
QLabel#city_Label {
    font-size: 20px;
    font-weight: 600;
    color: #333333;
    margin-top: 20px;
}

/* ---- Input ---- */
QLineEdit#city_Input {
    font-size: 18px;
    padding: 10px 12px;
    border: 2px solid #c7d6eb;
    border-radius: 8px;
    background-color: white;
    margin: 10px 50px 15px 50px;
}

QLineEdit#city_Input:focus {
    border: 2px solid #4a90e2;
}

/* ---- Button ---- */
QPushButton#get_Weather_Button {
    font-size: 18px;
    padding: 10px 15px;
    margin: 10px 60px 20px 60px;
    background-color: #4a90e2;
    color: white;
    border: none;
    border-radius: 10px;
}

QPushButton#get_Weather_Button:hover {
    background-color: #357abd;
}

QPushButton#get_Weather_Button:pressed {
    background-color: #2c6ed5;
}

/* ---- Temperature ---- */
QLabel#temperature_Label {
    font-size: 64px;
    font-weight: bold;
    color: #222222;
    margin-top: 20px;
}

/* ---- Emoji ---- */
QLabel#emoji_Label {
    font-size: 64px;
    margin: 10px 0px;
}

/* ---- Description ---- */
QLabel#description_Label {
    font-size: 24px;
    color: #555555;
    margin-bottom: 20px;
}
"""
        )

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = os.getenv("OPENWEATHER_API_KEY")
        city = self.city_input.text()
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        )

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request: The request was invalid.")
                case 401:
                    self.display_error("Unauthorized: Check your API key.")
                case 403:
                    self.display_error(
                        "Forbidden: You don't have access to this resource."
                    )
                case 404:
                    self.display_error("City not found. Please check the city name.")
                case 500:
                    self.display_error("Server Error: Try again later.")
                case 502:
                    self.display_error("Bad Gateway: Invalid response from the server.")
                case 503:
                    self.display_error("Service Unavailable: Try again later.")
                case 504:
                    self.display_error("Gateway Timeout: Try again later.")
                case _:
                    self.display_error(f"HTTP Error: {http_error}")

        except requests.exceptions.RequestException as req_error:
            print(f"Request Error: {req_error}")
        except requests.exceptions.ConnectionError:
            print("Network error. Please check your internet connection.")
        except requests.exceptions.Timeout:
            print("The request timed out. Please try again later.")
        except requests.exceptions.TooManyRedirects:
            print("Too many redirects. Check the URL.")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 22px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 64px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_c * 9 / 5) + 32
        weather_description = data["weather"][0]["description"].capitalize()
        weather_id = data["weather"][0]["id"]

        self.temperature_label.setText(f"{temperature_f:.0f} °F")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if weather_id >= 200 and weather_id <= 232:
            return "⛈️"
        elif weather_id >= 300 and weather_id <= 321:
            return "☁️"
        elif weather_id >= 500 and weather_id <= 531:
            return "🌦️"
        elif weather_id >= 600 and weather_id <= 622:
            return "❄️"
        elif weather_id >= 701 and weather_id <= 741:
            return "💨"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌪️"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif weather_id >= 801 and weather_id <= 804:
            return "☁️"
        else:
            return "🌡️"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
