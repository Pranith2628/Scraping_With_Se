from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:/Users/Prani/Downloads/Selenium/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.tutorialsfreak.com/')
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div/div/div/section[1]/div/div[1]/div/div/div/div[2]/button""").click()
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div/div/div/section/div/div[2]/div[1]/div/ul/li[7]/a""").click()
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div/div/div/section/div/div[2]/div[2]/div/div/a/div/div[2]""").click()
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div/div/div/section[1]/div/div/div[2]/div/div/p[2]/a/strong""").click()