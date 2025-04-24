from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

class ChromeManager:
    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        # Dynamically resolve path to chromedriver
        driver_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            "drivers",
            "chromedriver.exe"
        )
        service = Service(driver_path)
        return webdriver.Chrome(service=service, options=chrome_options)
