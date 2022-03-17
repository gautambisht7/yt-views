from selenium import webdriver
import time
from random import seed
from random import randint
from selenium.webdriver.common.keys import Keys
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
class InstaBot:
    def __init__(self, username, password):
        driver.implicitly_wait(30)
        driver.get("https://instagram.com")      
        time.sleep(getRandomTime())
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys('test_python_11')
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys('e8c2cadf2149')
        time.sleep(getRandomTime())      
        driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()


         try:
             driver.implicitly_wait(30)
             notifications = driver.find_element_by_xpath('//button[text()="Not Now"]')
             notifications.click()
             time.sleep(1)
         except:
             pass
  
        time.sleep(getRandomTime())
        driver.implicitly_wait(30)
        driver.find_element_by_xpath('//button[text()="Not Now"]')\
            .click()
        time.sleep(getRandomTime())
        search_2 = driver.find_element_by_xpath('//input[@placeholder="Search"]')
        search_2.send_keys('virat.kohli')
        time.sleep(6)
        search_2.send_keys(Keys.ENTER)   
        count = 0
        while count <2:
             search_2.send_keys(Keys.ENTER)
             count +=1 # count = count +1
             time.sleep(1)
      
        time.sleep(getRandomTime())
        driver.implicitly_wait(30)
        follow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
def getRandomTime():
        randTime = randint(3, 5)
        return randTime      
InstaBot("your_usernmae", "your_password")   

while (True):  
        follow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button').click()
        print('Following')
        time.sleep(7)
        driver.implicitly_wait(30)
        unfollow1 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button').click()
        time.sleep(getRandomTime())
        unfollow2 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
        print('Unfollowed')
        time.sleep(6)

        
