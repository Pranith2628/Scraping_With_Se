from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

s = Service('C:/Users/Prani/Downloads/Selenium/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
time.sleep(1)
search = driver.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input""")
search.send_keys("The Irishman")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[7]/div/div[11]/div[4]/div[3]/div/div/div[2]/div/div/div/div[6]/div/div/div/span[2]/span/a""").click()
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[7]/div/div[11]/div[5]/div[2]/div/div/div[2]/div/div/div/div[5]/div/div/div/span[2]/span/a""").click()
time.sleep(6)
driver.find_element_by_xpath("""/html/body/div[7]/div/div[11]/div[3]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[15]/div/div/div/div/div/div[5]/div/div[2]/div[4]/a/div[2]""").click()
