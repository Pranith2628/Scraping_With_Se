from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service('C:/Users/Prani/Downloads/Selenium/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://online.kfc.co.in/")
# driver.save_screenshot("C:/Users/Prani/Downloads/Selenium/chromedriver_win32/KFC-page.png")
time.sleep(10)
driver.find_element_by_xpath("""/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[4]/a[5]/img""").screenshot("C:/Users/Prani/Downloads/Selenium/chromedriver_win32/Meal-Box.png")