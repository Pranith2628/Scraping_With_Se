from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service('C:/Users/Prani/Downloads/Selenium/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
search = driver.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input""")
search.send_keys("House of the dragon")
time.sleep(2)
search.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[7]/div/div[11]/div[3]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[3]/div/div/div/div/div/div[1]/div/a/h3""").click()
time.sleep(2)
driver.save_screenshot("C:/Users/Prani/Downloads/Selenium/chromedriver_win32/HBO.png")