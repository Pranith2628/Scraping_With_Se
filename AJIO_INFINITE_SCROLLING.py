from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service('C:/Users/Prani/Downloads/Selenium/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.ajio.com/s/footwear-4792-56591?query=%3Arelevance%3Apricerange%3ARs.500-1000%3Apricerange%3ABelow%20Rs.500%3Al1l3nestedcategory%3AMen%20-%20Formal%20Shoes%3Averticalcolorfamily%3ABlack&curated=true&curatedid=footwear-4792-56591&gridColumns=3&segmentIds=")
time.sleep(5)
while True:
    height = driver.execute_script("return document.body.scrollHeight")
    print(height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break