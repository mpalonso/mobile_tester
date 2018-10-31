from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import hashlib
import time


# Mobile Tester (Emular Movil con Chrome)
# author: mrb0b0t
# TODO: Firefox

url = input("Insert url: ")

mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
chrome_options = Options()
chrome_driver_path = "./chromedriver"
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_driver_path, chrome_options = chrome_options)
driver.get(url)
salt = str(time.time())
file_name = hashlib.md5(salt).hexdigest() + ".png"
driver.save_screenshot(file_name)
time.sleep(5)
driver.quit()
