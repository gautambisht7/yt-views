from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os

from random import seed
from random import randint

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.get('''https://www.youtube.com/results?search_query=Nxt+Level+Gaming+CRIMINALS+VS+HIPHOP+%7C%7C+FREE+FIRE+3D+ANIMATION''')
time.sleep(10)
a=driver.find_element_by_xpath('//*[@id="dismissible"]/div')
a.click()
while True:
     time.sleep(66)
     
     driver.refresh()
     a = 0
     
    
     
     print('done',+a,'Times')
     a=a+1
     driver.get('''https://www.youtube.com/results?search_query=Nxt+Level+Gaming+CRIMINALS+VS+HIPHOP+%7C%7C+FREE+FIRE+3D+ANIMATION''')
     time.sleep(5)
     a=driver.find_element_by_xpath('//*[@id="dismissible"]/div')
     a.click()


