import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QGridLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Weather Forecasting App')

        self.city_input = QLineEdit(self)
        self.search_button = QPushButton('Search', self)
        self.search_button.clicked.connect(self.get_weather)

        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)

        layout = QGridLayout()
        layout.addWidget(self.city_input, 0, 0, 1, 2)
        layout.addWidget(self.search_button, 0, 2)
        layout.addWidget(self.result_label, 1, 0, 1, 3)

        self.setLayout(layout)

    def get_weather(self):
        city = self.city_input.text()
        url = f"https://goweather.herokuapp.com/weather/{city}"

        payload = {}
        headers = {}

        response = requests.get(url, headers=headers, data=payload)
        data = response.json()

        if response.status_code == 200:
            forecast_today = data.get("forecast", [])

            if forecast_today:
                today_text = f"Today:\nTemperature: {forecast_today[0].get('temperature', 'N/A')}\nWind: {forecast_today[0].get('wind', 'N/A')}\nDescription: {forecast_today[0].get('description', 'N/A')}"
                tomorrow_text = f"Tomorrow:\nTemperature: {forecast_today[1].get('temperature', 'N/A')}\nWind: {forecast_today[1].get('wind', 'N/A')}"

                self.show_forecast(today_text, tomorrow_text, forecast_today[0].get('description', 'N/A'))
            else:
                self.show_error("No forecast data available")
        else:
            self.show_error("City not found")

    def show_forecast(self, today_text, tomorrow_text, description):
        self.result_label.setText(f"{today_text}\n\n{tomorrow_text}")

        image_path = self.get_image_path(description)
        pixmap = QPixmap(image_path)

        image_label = QLabel(self)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        layout = self.layout()
        layout.addWidget(image_label, 2, 0, 1, 3)

    def show_error(self, message):
        self.result_label.setText(f"Error: {message}")

    def get_image_path(self, description):
        if "clear" in description.lower():
            return "clear_sky.png"  # Replace with the path to your clear sky image
        elif "cloud" in description.lower():
            return "cloudy.png"  # Replace with the path to your cloudy image
        else:
            return "unknown.png"  # Replace with the path to your default image

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec())
