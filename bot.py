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
def getRandomTime():
        randTime = randint(50, 65)
        return randTime 
def getRandomime():
        randTime1 = randint(5, 10)
        return randTime1
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.get('''https://www.youtube.com/results?search_query=Nxt+Level+Gaming+CRIMINALS+VS+HIPHOP+%7C%7C+FREE+FIRE+3D+ANIMATION''')
time.sleep(getRandomime())
a=driver.find_element_by_xpath('//*[@id="dismissible"]/div')
a.click()
while True:
     
     time.sleep(getrandomTime())
     
     driver.refresh()
     a = 0
     
    
     
     print('done',+a,'Times')
     a+=1
     time.sleep(361)
     driver.get('''https://www.youtube.com/results?search_query=Nxt+Level+Gaming+CRIMINALS+VS+HIPHOP+%7C%7C+FREE+FIRE+3D+ANIMATION''')
     a=driver.find_element_by_xpath('//*[@id="dismissible"]/div')
     a.click()
