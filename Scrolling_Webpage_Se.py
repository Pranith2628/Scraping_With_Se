from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service('C:/Users/Prani/Downloads/Selenium/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/search?q=penguins&sxsrf=APwXEdfzFmavj1t5G0u4Oj1RRz3suCMwFA:1680692480940&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiKhLayy5L-AhWf6jgGHboNA1IQ_AUoAXoECAEQAw&biw=1536&bih=746&dpr=1.25")
height = driver.execute_script("return document.body.scrollHeight")
print(height)
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")