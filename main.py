from PIL import Image
from PySide6.QtCore import Qt
from ui_main_fixed import Ui_MainWindow
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton, QWidget
import sys
import requests
import json
from datetime import datetime
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QIcon
from io import BytesIO
from PySide6.QtWidgets import QLabel


class MyUI(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Weather App")
        self.icon_name_widget.setHidden(True)
        self.btn_search.clicked.connect(self.search_city)

    def resize_image(self,image_path, width, height):
        """
        Resize the image to the specified width and height using PIL.

        Parameters:
        - image_path: Path to the image file or image data.
        - width: Desired width of the resized image.
        - height: Desired height of the resized image.

        Returns:
        - Resized image data.
        """
        image = Image.open(image_path)
        resized_image = image.resize((width, height), Image.ANTIALIAS)
        
        # Save the resized image to a BytesIO buffer
        resized_buffer = BytesIO()
        resized_image.save(resized_buffer, format="PNG")
        
        # Get the content of the BytesIO buffer
        resized_data = resized_buffer.getvalue()

        return resized_data
   
    def search_city(self):
        city=self.lineEdit.text()
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?&city={city}&key=2effe1f9f06e40cc8ef77eb5be376022"
        response = requests.request("GET", url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            date_time = json_data["data"][0]["datetime"]
            normal_date = datetime.strptime(date_time, '%Y-%m-%d')
            date = normal_date.strftime('%A, %d %B')
            description_weather = json_data["data"][0]["weather"]["description"]
            wind_speed = json_data["data"][0]["wind_spd"]
            today_temp = json_data["data"][0]["temp"]


            if "Clear" in description_weather:
                img = "images/clear.png"
            elif "Few clouds" in description_weather: 
                img = "images/few_cloudes.png"
            elif "Mix snow/rain" in description_weather: 
                img = "images/rain_snow.png"
            elif "rain" in description_weather: 
                img = "images/rain.png"
            elif "snow" in description_weather: 
                img = "images/snow.png"
            else : 
                img = "images/cludy.png"
            # today inqueries
            self.lbl_description.setText(description_weather)
            self.lbl_today_wind.setText(str(wind_speed))
            self.lbl_today_temp.setText(str(today_temp))
            resized_img = self.resize_image(img, 181, 141)
            pixmap = QPixmap()
            pixmap.loadFromData(resized_img)
            self.condition_img.setPixmap(pixmap)
            
            # tomorrow inqueries
            
            self.lbl_tomorrow_temp.setText(str(json_data["data"][1]["temp"]))
            self.lbl_tomorrow_wind.setText(str(json_data["data"][0]["wind_spd"]))
        else:
            print("API does not Working!")


        
        
if __name__ == "__main__":
    
    App=QApplication(sys.argv)
    
    window=MyUI()
    window.show()
    App.exec()